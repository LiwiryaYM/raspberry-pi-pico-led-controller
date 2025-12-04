# 🕹️ Raspberry Pi Pico LED Controller

![Project Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Language](https://img.shields.io/badge/Language-MicroPython-blue)
![Hardware](https://img.shields.io/badge/Hardware-Raspberry_Pi_Pico-C51A4A)
![License](https://img.shields.io/badge/License-MIT-yellow)

Project sederhana berbasis **Raspberry Pi Pico** untuk mengontrol dua grup LED dengan pola berkedip sekuensial. Project ini disimulasikan menggunakan Wokwi dan diprogram dengan **MicroPython**.

Interaksi pengguna dilakukan melalui tombol (push button) yang berfungsi sebagai *switch* untuk mengubah grup LED yang aktif.

---

## 📑 Daftar Isi
- [Fitur Utama](#-fitur-utama)
- [Teknologi yang Digunakan](#-teknologi-yang-digunakan)
- [Struktur Project](#-struktur-project)
- [Skema Rangkaian](#-skema-rangkaian)
- [Prasyarat & Instalasi](#-prasyarat--instalasi)
- [Cara Penggunaan](#-cara-penggunaan)
- [Kontribusi](#-kontribusi)
- [Lisensi](#-lisensi)

---

## ✨ Fitur Utama

* **Dual Group Control**: Mengontrol dua grup LED yang berbeda (Grup 1 & Grup 2).
* **Sequential Blinking**: LED menyala secara bergantian (running LED) di dalam grup yang aktif.
* **Interactive Switching**: Menggunakan tombol fisik untuk berpindah antar grup LED secara *real-time*.
* **Console Logging**: Menampilkan status grup dan warna lampu yang menyala pada Serial Monitor/Console.
* **Debounce Logic**: Logika sederhana untuk membaca perubahan status tombol.

---

## 🛠 Teknologi yang Digunakan

### Perangkat Lunak (Software)
* **MicroPython**: Bahasa pemrograman utama untuk logika mikrokontroler.
* **Wokwi**: Platform simulasi elektronik online.
* **VS Code (Opsional)**: Untuk editing kode lokal.

### Perangkat Keras (Hardware / Simulasi)
* 1x Raspberry Pi Pico
* 6x LED (Biru, Kuning, Hijau, Putih, Merah, Ungu)
* 6x Resistor (330Ω)
* 1x Push Button

---

## 📂 Struktur Project

Berikut adalah susunan file dalam repositori ini:

```text
raspberry-pi-pico-led-controller/
├── .vscode/               # Konfigurasi editor VS Code
├── .gitignore             # File yang diabaikan oleh Git
├── LICENSE                # Lisensi MIT
├── README.md              # Dokumentasi project ini
├── diagram.json           # Konfigurasi skematik untuk Wokwi
├── main.py                # Kode sumber utama (Logika MicroPython)
└── wokwi-project.txt      # Link referensi project Wokwi
````

-----

## ⚡ Skema Rangkaian

Berdasarkan file `main.py` dan `diagram.json`, berikut adalah pemetaan pin (Pin Mapping) yang digunakan:

| Komponen | Warna LED | Pin Pico (GP) | Grup |
| :--- | :--- | :---: | :---: |
| **LED 1** | 🔵 Biru | `GP2` | 1 |
| **LED 2** | 🟡 Kuning | `GP1` | 1 |
| **LED 3** | 🟢 Hijau | `GP0` | 1 |
| **LED 4** | ⚪ Putih | `GP26` | 2 |
| **LED 5** | 🔴 Merah | `GP27` | 2 |
| **LED 6** | 🟣 Ungu | `GP28` | 2 |
| **Tombol** | - | `GP15` | Input |

> **Catatan:** Tombol dikonfigurasi dengan `PULL_DOWN`, artinya akan bernilai `1` (High) saat ditekan.

-----

## 🚀 Prasyarat & Instalasi

Anda dapat menjalankan project ini melalui simulasi online atau perangkat keras fisik.

### Opsi 1: Simulasi Online (Direkomendasikan)

Cara termudah untuk mencoba project ini tanpa instalasi apapun.

1.  Buka browser Anda.
2.  Kunjungi tautan project Wokwi berikut:
    👉 **[Simulasi Wokwi: Raspberry Pi Pico LED Controller](https://wokwi.com/projects/446769242396018689)**
3.  Klik tombol **Play** (▶️) berwarna hijau di tengah layar.

### Opsi 2: Instalasi Lokal (Hardware Fisik)

Jika Anda ingin mengunggah ke Raspberry Pi Pico asli:

1.  Pastikan Anda telah menginstal **Python** dan **Thonny IDE**.
2.  Flash firmware **MicroPython** terbaru ke dalam Raspberry Pi Pico Anda.
3.  Clone repositori ini:
    ```bash
    git clone [https://github.com/liwiryaym/raspberry-pi-pico-led-controller.git](https://github.com/liwiryaym/raspberry-pi-pico-led-controller.git)
    ```
4.  Buka file `main.py` menggunakan Thonny IDE.
5.  Sambungkan Pico ke komputer, lalu klik **Run** atau simpan file tersebut sebagai `main.py` di dalam Pico agar berjalan otomatis saat dinyalakan.

-----

## 🎮 Cara Penggunaan

1.  **Start**: Saat simulasi dimulai, **Grup 1** akan aktif secara default.
2.  **Pola Grup 1**: Lampu Biru ➡ Kuning ➡ Hijau akan menyala bergantian.
3.  **Ganti Grup**: Tekan **Tombol (Push Button)** satu kali.
4.  **Respon**:
      * Sistem akan mendeteksi penekanan tombol.
      * Console akan mencetak: `Tombol ditekan! Ganti ke Grup 2`.
      * Lampu Grup 1 akan mati.
5.  **Pola Grup 2**: Lampu Putih ➡ Merah ➡ Ungu akan menyala bergantian.
6.  Tekan tombol lagi untuk kembali ke Grup 1.

-----

## 🤝 Kontribusi

Kontribusi selalu diterima\! Jika Anda ingin meningkatkan fitur atau memperbaiki *bug*:

1.  **Fork** repositori ini.
2.  Buat **Branch** baru (`git checkout -b fitur-keren`).
3.  **Commit** perubahan Anda (`git commit -m 'Menambahkan fitur keren'`).
4.  **Push** ke Branch (`git push origin fitur-keren`).
5.  Buat **Pull Request**.

-----

## 📝 Lisensi

Project ini didistribusikan di bawah lisensi **MIT**. Lihat file `LICENSE` untuk informasi lebih lanjut.

```text
MIT License
Copyright (c) 2025 CherryYume夢
```

-----

*Dibuat dengan oleh [Liwirya](https://www.google.com/search?q=https://github.com/liwiryaym)*
