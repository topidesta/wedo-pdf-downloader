# LEGO WeDo 2.0 — Building Instructions (PDF)

Arsip 40 panduan perakitan (*building instructions*) LEGO Education **WeDo 2.0**
(set 45300), dalam bahasa Inggris, diunduh dari halaman resmi LEGO Education:

<https://education.lego.com/en-us/product-resources/wedo-2/downloads/building-instructions/>

Total: **40 PDF / 195 MB** (186 MiB), semuanya terverifikasi sebagai berkas PDF valid
(`%PDF` header) dan tercatat di [`_index.csv`](_index.csv).

> **Disclaimer.** Semua berkas PDF di repo ini adalah materi berhak cipta milik
> **LEGO Education / The LEGO Group**. Repo ini tidak berafiliasi dengan,
> disponsori, atau didukung oleh LEGO. Arsip ini hanya disimpan untuk kemudahan
> akses offline; hak cipta tetap pada pemiliknya. Jika LEGO meminta, arsip akan
> dihapus.

---

## Isi repo

```
.
├── download.py       # scraper + downloader (stdlib Python, tanpa dependensi)
├── page.html         # snapshot halaman sumber (input untuk download.py)
├── all_assets.txt    # 307 URL aset di assets.education.lego.com (font, gambar, PDF)
├── _index.csv        # manifest hasil unduhan
├── pdf/              # 40 PDF, nama "<nn> - <Judul>.pdf"
└── README.md
```

| Berkas | Keterangan |
| --- | --- |
| `download.py` | Membaca `page.html`, mengekstrak pasangan judul ↔ URL PDF, mengunduh paralel (5 worker), lalu menulis `_index.csv`. |
| `page.html` | Salinan HTML halaman daftar building instructions. Ini yang di-parse, bukan jaringan. |
| `all_assets.txt` | Hasil enumerasi seluruh URL aset dari halaman (307 baris), termasuk 40 PDF — berguna kalau mau menambahkan aset lain (font/gambar). |
| `_index.csv` | Manifest: `no, title, file, bytes, status, original_filename, source_url`. |

## Daftar PDF

| No | Judul | Berkas | Ukuran | Nama asli |
| --- | --- | --- | --- | --- |
| 1 | Snail | 01 - Snail.pdf | 1.9 MB | `45300_easystart_m1_.pdf` |
| 2 | Fan | 02 - Fan.pdf | 2.0 MB | `45300_easystart_m2_.pdf` |
| 3 | Satellite | 03 - Satellite.pdf | 8.8 MB | `45300_easystart_m3_.pdf` |
| 4 | Spy Robot | 04 - Spy Robot.pdf | 6.1 MB | `45300_easystart_m4_.pdf` |
| 5 | MILO | 05 - MILO.pdf | 6.3 MB | `45300_16_milo.pdf` |
| 6 | MILO Arm 1 | 06 - MILO Arm 1.pdf | 3.4 MB | `45300_16a_milo_arm_1.pdf` |
| 7 | MILO Arm 2 | 07 - MILO Arm 2.pdf | 3.2 MB | `45300_16a_milo_arm_2.pdf` |
| 8 | MILO Twins 3 | 08 - MILO Twins 3.pdf | 8.9 MB | `45300_16a_milo_twins_3.pdf` |
| 9 | MILO Arm 1 Modified | 09 - MILO Arm 1 Modified.pdf | 8.2 MB | `45300_16a_milo_arm-1_modified_24102016_.pdf` |
| 10 | Alarm Device | 10 - Alarm Device.pdf | 5.7 MB | `45300_11a_alarm_device.pdf` |
| 11 | Cody | 11 - Cody.pdf | 2.1 MB | `45300_p01_cody_.pdf` |
| 12 | Cody Motion Sensor | 12 - Cody Motion Sensor.pdf | 2.4 MB | `45300_p01a_cody_with_motion_sensor_.pdf` |
| 13 | Cody Tilt Sensor | 13 - Cody Tilt Sensor.pdf | 2.4 MB | `45300_p01b_cody_with_tilt_sensor_.pdf` |
| 14 | Crank | 14 - Crank.pdf | 1.7 MB | `45300_03_crank.pdf` |
| 15 | Drive | 15 - Drive.pdf | 1.7 MB | `45300_02_drive.pdf` |
| 16 | Earthquake | 16 - Earthquake.pdf | 4.0 MB | `45300_03a_earthquake.pdf` |
| 17 | Flex | 17 - Flex.pdf | 4.8 MB | `45300_06_flex.pdf` |
| 18 | Floodgates | 18 - Floodgates.pdf | 4.9 MB | `45300_06a_floodgate.pdf` |
| 19 | Flower | 19 - Flower.pdf | 6.8 MB | `45300_05a_flower.pdf` |
| 20 | Grab | 20 - Grab.pdf | 4.4 MB | `45300_09_grab.pdf` |
| 21 | Helicopter | 21 - Helicopter.pdf | 14.1 MB | `45300_7a_helicopter.pdf` |
| 22 | Joystick | 22 - Joystick.pdf | 1.7 MB | `45300_15b_joystick.pdf` |
| 23 | Lift | 23 - Lift.pdf | 3.9 MB | `45300_08_lift.pdf` |
| 24 | Luna Rover | 24 - Luna Rover.pdf | 5.1 MB | `45300_16a_luna_rover.pdf` |
| 25 | Motion | 25 - Motion.pdf | 1.5 MB | `45300_14_motion.pdf` |
| 26 | Pull | 26 - Pull.pdf | 6.5 MB | `45300_01a_pull.pdf` |
| 27 | Push | 27 - Push.pdf | 7.0 MB | `45300_10_push.pdf` |
| 28 | Race Car | 28 - Race Car.pdf | 3.5 MB | `45300_02a_race_car.pdf` |
| 29 | Recycling Truck | 29 - Recycling Truck.pdf | 9.3 MB | `45300_08a_recycling_truck.pdf` |
| 30 | Reel | 30 - Reel.pdf | 12.0 MB | `45300_07_reel.pdf` |
| 31 | Revolve | 31 - Revolve.pdf | 7.2 MB | `45300_11_revolve.pdf` |
| 32 | Robotic Arm | 32 - Robotic Arm.pdf | 6.3 MB | `45300_09a_robotic_arm.pdf` |
| 33 | Steer | 33 - Steer.pdf | 6.4 MB | `45300_12_steer.pdf` |
| 34 | Spin | 34 - Spin.pdf | 3.0 MB | `45300_05_spin.pdf` |
| 35 | Sweep | 35 - Sweep.pdf | 2.6 MB | `45300_13_sweep.pdf` |
| 36 | Tilt | 36 - Tilt.pdf | 2.8 MB | `45300_15_tilt.pdf` |
| 37 | Turn | 37 - Turn.pdf | 3.2 MB | `45300_16_turn.pdf` |
| 38 | Walk | 38 - Walk.pdf | 2.7 MB | `45300_04_walk.pdf` |
| 39 | Wobble | 39 - Wobble.pdf | 3.1 MB | `45300_01_wobble.pdf` |
| 40 | Young Frog | 40 - Young Frog.pdf | 3.5 MB | `45300_04c_young_frog.pdf` |

## Cara mengunduh ulang

Butuh Python 3.8+. Tidak ada dependensi eksternal (hanya `urllib`, `re`, `csv`).

```bash
python download.py
```

Output yang diharapkan:

```
found 40 pdf links
[ok] 01 - Snail.pdf  1876931 bytes
...
DONE: 40/40 ok, total 195.0 MB
```

(Ukuran di `_index.csv` dan README ini memakai MB desimal, `bytes / 1e6` —
karena itu 195 MB di sini setara 186 MiB di `du`.)

Sifat script:

- **Idempoten.** Berkas yang sudah ada dan berukuran > 1 KB dianggap *cached* dan
  dilewati, jadi menjalankan ulang tidak mengunduh 187 MB lagi. Untuk memaksa
  unduh ulang, hapus isi `pdf/` lebih dulu.
- **Verifikasi isi.** Respons yang tidak diawali `%PDF` dianggap gagal, bukan
  disimpan sebagai berkas sampah.
- **Retry 4x** dengan backoff (`1.5 × percobaan`) per berkas; 5 unduhan paralel.
- **Header browser** dipasang (`User-Agent`, `Accept`, `Referer`) karena CDN LEGO
  menolak permintaan tanpa itu.
- Hasil akhir selalu ditulis ulang ke `_index.csv` dengan kolom `status`
  (`ok` / `cached` / `FAIL <alasan>`).

## Memperbarui daftar dari halaman sumber

`download.py` mem-parse `page.html` secara lokal — tidak menyentuh jaringan saat
mengumpulkan daftar. Kalau halaman LEGO berubah, simpan ulang HTML-nya ke
`page.html`, lalu jalankan script lagi.

Regex yang dipakai rapuh terhadap perubahan markup; ia mengasumsikan pola:

```html
<a href="https://assets.education.lego.com/.../<nama>.pdf?locale=en-us">
  <h3>Judul Model</h3>
</a>
```

Kalau jumlah yang ditemukan bukan 40, kemungkinan besar LEGO mengubah struktur
halaman atau format URL (mis. query `?locale=` hilang) — periksa regex di
`download.py` baris 12–14 sebelum menganggap ada berkas yang hilang.

## Catatan

- Penomoran berkas (`01`–`40`) mengikuti **urutan tampil di halaman sumber**,
  bukan nomor kode model LEGO. `original_filename` di `_index.csv` menyimpan
  nama asli dari CDN (mis. `45300_16a_milo_arm_1.pdf`) — itu yang lebih akurat
  untuk merujuk model tertentu.
- Beberapa entri adalah varian model yang sama: `MILO` (#5) punya 4 varian
  (#6–#9), `Cody` (#11) punya 2 varian sensor (#12–#13).
- Semua PDF berbahasa Inggris (`locale=en-us`). Versi bahasa lain tidak diunduh.
