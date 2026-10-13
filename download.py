import re, csv, os, sys, time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "pdf")
os.makedirs(OUT, exist_ok=True)

html = open(os.path.join(BASE, "page.html"), encoding="utf-8", errors="replace").read()

pairs = []
for m in re.finditer(
    r'href="(https://assets\.education\.lego\.com[^"]+?\.pdf\?locale=en-us)"[^>]*>\s*<h3[^>]*>(.*?)</h3>',
    html, re.S):
    url = m.group(1)
    title = re.sub(r"<[^>]+>", "", m.group(2)).strip()
    pairs.append((title, url))

# dedupe by url, preserve page order
seen, items = set(), []
for title, url in pairs:
    if url in seen:
        continue
    seen.add(url)
    items.append((title, url))

print(f"found {len(items)} pdf links")

HDRS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept": "application/pdf,*/*",
    "Referer": "https://education.lego.com/en-us/product-resources/wedo-2/downloads/building-instructions/",
}


def safe(name):
    return re.sub(r'[<>:"/\\|?*]', "_", name).strip().rstrip(".")


def fetch(idx_item):
    i, (title, url) = idx_item
    orig = url.split("?")[0].rsplit("/", 1)[-1]
    fname = f"{i:02d} - {safe(title)}.pdf"
    dest = os.path.join(OUT, fname)
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        return (i, title, orig, url, fname, os.path.getsize(dest), "cached")
    last = ""
    for attempt in range(1, 5):
        try:
            req = urllib.request.Request(url, headers=HDRS)
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            if not data.startswith(b"%PDF"):
                last = f"not a PDF (head={data[:8]!r})"
                raise ValueError(last)
            with open(dest, "wb") as f:
                f.write(data)
            return (i, title, orig, url, fname, len(data), "ok")
        except Exception as e:
            last = f"{type(e).__name__}: {e}"
            time.sleep(1.5 * attempt)
    return (i, title, orig, url, fname, 0, "FAIL " + last)


results = []
with ThreadPoolExecutor(max_workers=5) as ex:
    for r in ex.map(fetch, list(enumerate(items, 1))):
        results.append(r)
        print(f"[{r[6]}] {r[4]}  {r[5]} bytes")

results.sort()
with open(os.path.join(BASE, "_index.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["no", "title", "file", "bytes", "status", "original_filename", "source_url"])
    for i, title, orig, url, fname, size, st in results:
        w.writerow([i, title, fname, size, st, orig, url])

ok = sum(1 for r in results if r[6] in ("ok", "cached"))
print(f"\nDONE: {ok}/{len(results)} ok, total {sum(r[5] for r in results)/1e6:.1f} MB")
