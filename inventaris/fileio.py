# Modul untuk menyimpan, membaca, dan membuat laporan inventaris.

import os

# Menentukan lokasi file data dan laporan.
FOLDER_DATA = "data"
FOLDER_LAPORAN = "laporan"
FILE_DATA = os.path.join(FOLDER_DATA, "barang.txt")
FILE_LAPORAN = os.path.join(FOLDER_LAPORAN, "laporan_inventaris.txt")


def siapkan_folder():
    # Membuat folder penyimpanan jika belum tersedia.
    os.makedirs(FOLDER_DATA, exist_ok=True)
    os.makedirs(FOLDER_LAPORAN, exist_ok=True)


def buat_file_awal():
    # Mode x membuat file baru tanpa menimpa file yang sudah ada.
    siapkan_folder()

    try:
        with open(FILE_DATA, "x", encoding="utf-8") as file:
            file.write("B001|Laptop|Elektronik|10\n")
            file.write("B002|Mouse|Aksesori|25\n")

        print("File data awal berhasil dibuat.")

    except FileExistsError:
        # Menangani kondisi ketika file sudah tersedia.
        print("File data sudah tersedia.")


def tambah_data(barang):
    # Mode a menambahkan data di akhir file.
    siapkan_folder()

    with open(FILE_DATA, "a", encoding="utf-8") as file:
        file.write(barang.tampilkan_data() + "\n")


def baca_data():
    # Mode r membaca file baris demi baris.
    daftar_data = []

    try:
        with open(FILE_DATA, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()

                # Melewati baris kosong.
                if not baris:
                    continue

                try:
                    bagian = baris.split("|")

                    # Memastikan data memiliki empat kolom.
                    if len(bagian) != 4:
                        raise ValueError("Jumlah kolom tidak sesuai.")

                    id_barang, nama, kategori, stok = bagian
                    stok = int(stok)

                    # Memastikan kolom teks tidak kosong.
                    if not id_barang or not nama or not kategori:
                        raise ValueError("Data barang tidak lengkap.")

                    # Memastikan stok tidak negatif.
                    if stok < 0:
                        raise ValueError("Stok tidak boleh negatif.")

                    daftar_data.append({
                        "id_barang": id_barang,
                        "nama": nama,
                        "kategori": kategori,
                        "stok": stok
                    })

                except ValueError:
                    # Melewati baris rusak dan melanjutkan pembacaan.
                    print("Baris rusak dilewati:", baris)

    except FileNotFoundError:
        # Memberikan pesan jika file data belum tersedia.
        print("File data belum ditemukan.")

    return daftar_data


def tulis_laporan(daftar_data):
    # Mode w membuat atau menimpa laporan dengan hasil terbaru.
    siapkan_folder()
    total_stok = 0

    with open(FILE_LAPORAN, "w", encoding="utf-8") as file:
        file.write("LAPORAN INVENTARIS BARANG\n")
        file.write("=========================\n\n")

        for barang in daftar_data:
            file.write(
                f"ID: {barang['id_barang']}\n"
                f"Nama: {barang['nama']}\n"
                f"Kategori: {barang['kategori']}\n"
                f"Stok: {barang['stok']}\n\n"
            )
            total_stok += barang["stok"]

        # Menuliskan ringkasan inventaris.
        file.write(f"Jumlah jenis barang: {len(daftar_data)}\n")
        file.write(f"Total seluruh stok: {total_stok}\n")

    print("Laporan berhasil disimpan.")


# Pengujian lokal modul file handling.
if __name__ == "__main__":
    buat_file_awal()
    data_barang = baca_data()
    tulis_laporan(data_barang)