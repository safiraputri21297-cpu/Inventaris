# Pengujian fungsi dan class pada sistem InventarisKu.

import unittest

from inventaris.processing import Barang, Inventaris
from inventaris.validasi import validasi_barang


class TestInventaris(unittest.TestCase):
    # Menguji pembuatan objek barang.
    def test_buat_barang(self):
        barang = Barang("B001", "Laptop", "Elektronik", 10)

        self.assertEqual(barang.id_barang, "B001")
        self.assertEqual(barang.nama, "Laptop")
        self.assertEqual(barang.stok, 10)

    # Menguji penambahan barang ke inventaris.
    def test_tambah_barang(self):
        inventaris = Inventaris()
        barang = Barang("B001", "Laptop", "Elektronik", 10)

        inventaris.tambah_barang(barang)

        self.assertEqual(inventaris.hitung_jenis_barang(), 1)

    # Menguji perhitungan total stok.
    def test_hitung_total_stok(self):
        inventaris = Inventaris()
        inventaris.tambah_barang(
            Barang("B001", "Laptop", "Elektronik", 10)
        )
        inventaris.tambah_barang(
            Barang("B002", "Mouse", "Aksesori", 5)
        )

        self.assertEqual(inventaris.hitung_total_stok(), 15)

    # Menguji pencarian barang berdasarkan nama.
    def test_cari_barang(self):
        inventaris = Inventaris()
        inventaris.tambah_barang(
            Barang("B001", "Laptop", "Elektronik", 10)
        )

        hasil = inventaris.cari_barang("laptop")

        self.assertEqual(len(hasil), 1)
        self.assertEqual(hasil[0].nama, "Laptop")

    # Menguji penolakan stok negatif.
    def test_stok_negatif_ditolak(self):
        with self.assertRaises(ValueError):
            validasi_barang("B001", "Laptop", "Elektronik", -5)

    # Menguji penolakan input stok berupa teks.
    def test_stok_teks_ditolak(self):
        with self.assertRaises(ValueError):
            validasi_barang("B001", "Laptop", "Elektronik", "banyak")


# Menjalankan pengujian jika file dibuka langsung.
if __name__ == "__main__":
    unittest.main()
