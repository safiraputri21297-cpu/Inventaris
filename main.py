# Program utama Sistem Inventaris Barang Laboratorium.

from inventaris.processing import Barang, Inventaris
from inventaris.validasi import validasi_barang
from inventaris.fileio import (
    buat_file_awal,
    baca_data,
    tambah_data,
    tulis_laporan
)


def muat_inventaris():
    # Membaca data dari file dan memasukkannya ke dalam objek Inventaris.
    inventaris = Inventaris()
    daftar_data = baca_data()

    for data in daftar_data:
        barang = Barang(
            data["id_barang"],
            data["nama"],
            data["kategori"],
            data["stok"]
        )
        inventaris.tambah_barang(barang)

    return inventaris


def tampilkan_menu():
    # Menampilkan pilihan menu kepada pengguna.
    print("\n===== INVENTARISKU =====")
    print("1. Tambah barang")
    print("2. Tampilkan semua barang")
    print("3. Cari barang")
    print("4. Hitung total stok")
    print("5. Urutkan barang berdasarkan stok")
    print("6. Hitung stok berdasarkan kategori")
    print("7. Buat laporan inventaris")
    print("0. Keluar")


def tambah_barang_baru():
    # Meminta data barang baru dan menyimpannya ke file.
    try:
        id_barang = input("Masukkan ID barang: ").strip()
        nama = input("Masukkan nama barang: ").strip()
        kategori = input("Masukkan kategori: ").strip()
        stok = input("Masukkan stok: ").strip()

        validasi_barang(id_barang, nama, kategori, stok)

        inventaris = muat_inventaris()

        # Memeriksa agar ID barang tidak digunakan dua kali.
        for barang in inventaris.tampilkan_semua():
            if barang.id_barang == id_barang:
                raise ValueError("ID barang sudah digunakan.")

        barang_baru = Barang(id_barang, nama, kategori, stok)
        tambah_data(barang_baru)

        print("Barang berhasil ditambahkan.")

    except ValueError as error:
        # Menangani input yang tidak sesuai aturan.
        print("Data tidak valid:", error)

    except OSError as error:
        # Menangani masalah saat mengakses file.
        print("Terjadi masalah pada file:", error)


def tampilkan_semua_barang():
    # Menampilkan semua barang yang tersimpan di file.
    inventaris = muat_inventaris()
    daftar_barang = inventaris.tampilkan_semua()

    if not daftar_barang:
        print("Belum ada data barang.")
        return

    print("\n--- Daftar Barang ---")

    for barang in daftar_barang:
        print(
            f"ID: {barang.id_barang} | "
            f"Nama: {barang.nama} | "
            f"Kategori: {barang.kategori} | "
            f"Stok: {barang.stok}"
        )


def cari_barang():
    # Mencari barang berdasarkan ID, nama, atau kategori.
    kata_kunci = input("Masukkan kata kunci pencarian: ").strip()
    inventaris = muat_inventaris()
    hasil = inventaris.cari_barang(kata_kunci)

    if hasil:
        print("\n--- Hasil Pencarian ---")

        for barang in hasil:
            print(barang.tampilkan_data())
    else:
        print("Barang tidak ditemukan.")


def tampilkan_total_stok():
    # Menghitung dan menampilkan total seluruh stok.
    inventaris = muat_inventaris()
    total = inventaris.hitung_total_stok()

    print("Total seluruh stok:", total)


def urutkan_barang():
    # Menampilkan barang berdasarkan stok terkecil.
    inventaris = muat_inventaris()
    daftar_barang = inventaris.urutkan_berdasarkan_stok()

    print("\n--- Barang Berdasarkan Stok ---")

    for barang in daftar_barang:
        print(barang.tampilkan_data())


def tampilkan_stok_kategori():
    # Menghitung stok berdasarkan kategori yang dimasukkan.
    kategori = input("Masukkan kategori barang: ").strip()
    inventaris = muat_inventaris()
    total = inventaris.hitung_stok_kategori(kategori)

    print(f"Total stok kategori {kategori}: {total}")


def buat_laporan():
    # Membaca data dan menyimpan laporan inventaris ke file.
    daftar_data = baca_data()
    tulis_laporan(daftar_data)


def jalankan_program():
    # Menjalankan menu utama sampai pengguna memilih keluar.
    buat_file_awal()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tambah_barang_baru()
        elif pilihan == "2":
            tampilkan_semua_barang()
        elif pilihan == "3":
            cari_barang()
        elif pilihan == "4":
            tampilkan_total_stok()
        elif pilihan == "5":
            urutkan_barang()
        elif pilihan == "6":
            tampilkan_stok_kategori()
        elif pilihan == "7":
            buat_laporan()
        elif pilihan == "0":
            print("Program InventarisKu selesai.")
            break
        else:
            print("Pilihan tidak tersedia. Silakan coba lagi.")


# Menjalankan program hanya saat main.py dibuka langsung.
if __name__ == "__main__":
    jalankan_program()