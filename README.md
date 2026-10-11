# InventarisKu
Sistem Inventaris Barang Laboratorium menggunakan Python.

## Deskripsi
InventarisKu adalah program sederhana untuk membantu pengelolaan
data barang laboratorium. Program ini menggunakan function,
class, modularisasi, validasi input, dan file handling.

## Fitur
- Menambahkan data barang.
- Menampilkan seluruh data barang.
- Mencari barang berdasarkan ID, nama, atau kategori.
- Menghitung total stok barang.
- Mengurutkan barang berdasarkan stok.
- Menghitung stok berdasarkan kategori.
- Membuat laporan inventaris dalam file teks.
- Memvalidasi data dan melewati baris file yang rusak.

## Struktur Proyek
- `main.py`: program utama.
- `inventaris/validasi.py`: validasi data barang.
- `inventaris/processing.py`: class dan pengolahan data.
- `inventaris/fileio.py`: penyimpanan, pembacaan, dan laporan.
- `tests/test_inventaris.py`: pengujian program.
- `data/barang.txt`: file data inventaris yang dibuat otomatis.
- `laporan/laporan_inventaris.txt`: laporan yang dibuat otomatis.

## Cara Menjalankan
1. Pastikan Python sudah terpasang.
2. Buka terminal pada folder proyek.
3. Jalankan perintah:

   `python main.py`

## Cara Menjalankan Pengujian
Jalankan perintah:

`python -m unittest -v`

## Teknologi
- Python
- File Handling
- Object-Oriented Programming
- Unit Testing dengan unittest
