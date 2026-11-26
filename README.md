# port-scanner
Program ini menerima target berupa alamat IP (misalnya 127.0.0.1 untuk mengecek komputer sendiri atau IP router lokal) dan rentang nomor port yang ingin diperiksa, lalu mendeteksi port mana saja yang terbuka (OPEN).


# Simple TCP Port Scanner 🔍

Alat pemindai *port* TCP sederhana berbasis terminal (CLI) yang dibuat menggunakan Python dan modul bawaan `socket`. Proyek ini dikembangkan sebagai latihan pemrograman jaringan dan dasar keamanan siber (*network security*) untuk jurusan Teknik Komputer dan Jaringan (TKJ).

## 📋 Fitur Utama
- **Resolusi Hostname & IP:** Mendukung input berupa alamat IPv4 maupun nama domain (*hostname*).
- **Pemindaian Port Umum:** Mengecek status *port* layanan jaringan standar seperti FTP (21), SSH (22), Telnet (23), DNS (53), HTTP (80), HTTPS (443), MySQL (3306), dan HTTP Proxy (8080).
- **Manajemen Timeout:** Menggunakan batas waktu tunggu koneksi (`0.5` detik) agar proses pemindaian berjalan cepat dan tidak macet pada *port* yang difilter.
- **Tanpa Pustaka Eksternal:** Menggunakan 100% modul standar bawaan Python (`socket` dan `datetime`).

## 🚀 Cara Menjalankan
1. Pastikan **Python 3** sudah terinstal di komputer atau laptop kamu.
2. Unduh file `port_scanner.py` atau *clone* repositori ini:
   ```bash
   git clone https://github.com
   cd simple-port-scanner
   ```
3. Jalankan program melalui terminal atau Command Prompt:
   ```bash
   python port_scanner.py
   ```
4. Masukkan alamat IP target (contoh: `127.0.0.1` untuk mengecek komputer lokal).

## 💻 Contoh Tampilan Output
```text
=============================================
     SIMPLE TCP PORT SCANNER - TKJ PROJECT
=============================================
Masukkan IP Target (contoh: 127.0.0.1): 127.0.0.1

Memindai target: 127.0.0.1
Waktu mulai    : 01:15:30

[OPEN] Port 80    (HTTP (Web))
[OPEN] Port 3306  (MySQL Database)

Pemindaian selesai. Total port terbuka: 2
```

## 🛠️ Konsep Python yang Diterapkan
- **`socket.socket(AF_INET, SOCK_STREAM)`**: Membuat koneksi soket berbasis IPv4 dan protokol TCP.
- **`connect_ex()`**: Melakukan uji koneksi *TCP handshake* dan mengembalikan kode status tanpa memicu *crash* pada program.
- **Dictionary (`dict`)**: Memetakan nomor *port* dengan nama layanan jaringan agar mudah dibaca.
- **Exception Handling (`try-except`)**: Menangani kesalahan input *hostname* atau kegagalan resolusi DNS (`socket.gaierror`).

## ⚠️ Disclaimer (Catatan Etika)
Program ini dibuat **hanya untuk tujuan edukasi, pembelajaran jaringan, dan pengujian pada perangkat atau server milik sendiri** (seperti `127.0.0.1` atau lingkungan lab sekolah). Dilarang keras menggunakan alat ini untuk memindai jaringan atau sistem milik pihak lain tanpa izin resmi.
