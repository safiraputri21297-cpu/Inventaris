# Class untuk menyimpan data satu barang inventaris.

class Barang:
    def __init__(self, id_barang, nama, kategori, stok):
        # Menyimpan informasi barang ke dalam atribut.
        self.id_barang = id_barang
        self.nama = nama
        self.kategori = kategori
        self.stok = int(stok)

    def tampilkan_data(self):
        # Mengubah data barang menjadi satu baris teks.
        return f"{self.id_barang}|{self.nama}|{self.kategori}|{self.stok}"


# Class untuk mengelola kumpulan barang inventaris.

class Inventaris:
    def __init__(self):
        # Menyediakan list kosong untuk menyimpan barang.
        self.daftar_barang = []

    def tambah_barang(self, barang):
        # Menambahkan barang ke dalam list inventaris.
        self.daftar_barang.append(barang)

    def buat_barang(self, **kwargs):
        # Menerima data barang menggunakan keyword argument.
        barang = Barang(
            id_barang=kwargs["id_barang"],
            nama=kwargs["nama"],
            kategori=kwargs["kategori"],
            stok=kwargs["stok"]
        )

        self.tambah_barang(barang)
        return barang

    def tampilkan_semua(self):
        # Mengembalikan seluruh barang yang tersimpan.
        return self.daftar_barang

    def cari_barang(self, kata_kunci):
        # Mencari barang berdasarkan ID, nama, atau kategori.
        hasil = []

        for barang in self.daftar_barang:
            if (
                kata_kunci.lower() in barang.id_barang.lower()
                or kata_kunci.lower() in barang.nama.lower()
                or kata_kunci.lower() in barang.kategori.lower()
            ):
                hasil.append(barang)

        return hasil

    def hitung_total_stok(self, *stok_tambahan):
        # Menjumlahkan stok barang dan stok tambahan jika diberikan.
        total = sum(barang.stok for barang in self.daftar_barang)
        total += sum(stok_tambahan)

        return total

    def urutkan_berdasarkan_stok(self):
        # Mengurutkan barang berdasarkan stok terkecil.
        return sorted(
            self.daftar_barang,
            key=lambda barang: barang.stok
        )

    def hitung_jenis_barang(self):
        # Menghitung jumlah catatan barang dalam inventaris.
        return len(self.daftar_barang)

    def hitung_stok_kategori(self, kategori):
        # Menghitung total stok untuk kategori tertentu.
        total = 0

        for barang in self.daftar_barang:
            if barang.kategori.lower() == kategori.lower():
                total += barang.stok

        return total


# Pengujian lokal class dan fungsi pengolahan.
if __name__ == "__main__":
    inventaris = Inventaris()

    # Membuat barang dengan keyword argument.
    inventaris.buat_barang(
        id_barang="B001",
        nama="Laptop",
        kategori="Elektronik",
        stok=10
    )

    inventaris.buat_barang(
        id_barang="B002",
        nama="Mouse",
        kategori="Aksesori",
        stok=25
    )

    print("Jumlah jenis barang:", inventaris.hitung_jenis_barang())
    print("Total stok:", inventaris.hitung_total_stok())
    print("Total stok tambahan:", inventaris.hitung_total_stok(5))

    print("\nDaftar barang berdasarkan stok:")
    for barang in inventaris.urutkan_berdasarkan_stok():
        print(barang.tampilkan_data())