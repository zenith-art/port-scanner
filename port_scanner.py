from datetime import datetime
import socket


def scan_port(target_ip, port):
    # Membuat objek socket menggunakan IPv4 (AF_INET) dan protokol TCP (SOCK_STREAM)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # Batas waktu tunggu 0.5 detik per port

    # connect_ex mengembalikan angka 0 jika koneksi berhasil (port terbuka)
    hasil = s.connect_ex((target_ip, port))
    s.close()
    return hasil == 0


def mulai_scan():
    print("=" * 45)
    print("     SIMPLE TCP PORT SCANNER - TKJ PROJECT")
    print("=" * 45)

    target = input("Masukkan IP Target (contoh: 127.0.0.1): ").strip()

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("[ERROR] Hostname atau IP tidak dapat ditemukan.")
        return

    # Daftar port umum yang sering digunakan pada server & jaringan
    port_umum = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        53: "DNS",
        80: "HTTP (Web)",
        443: "HTTPS (Web Aman)",
        3306: "MySQL Database",
        8080: "HTTP Proxy/Alt",
    }

    print(f"\nMemindai target: {target_ip}")
    print(f"Waktu mulai    : {datetime.now().strftime('%H:%M:%S')}\n")

    port_terbuka = 0
    for port, layanan in port_umum.items():
        if scan_port(target_ip, port):
            print(f"[OPEN] Port {port:<5} ({layanan})")
            port_terbuka += 1

    if port_terbuka == 0:
        print("Tidak ada port umum yang terbuka pada target ini.")

    print(f"\nPemindaian selesai. Total port terbuka: {port_terbuka}")


if __name__ == "__main__":
    mulai_scan()
