# Fungsi untuk memeriksa data barang inventaris.

def validasi_barang(id_barang, nama, kategori, stok):
    # Memeriksa apakah identitas barang sudah diisi.
    if not id_barang or not nama or not kategori:
        raise ValueError("ID, nama, dan kategori tidak boleh kosong.")

    # Mengubah input stok menjadi bilangan bulat.
    try:
        stok = int(stok)
    except ValueError:
        raise ValueError("Stok harus berupa bilangan bulat.")

    # Memeriksa agar stok tidak bernilai negatif.
    if stok < 0:
        raise ValueError("Stok tidak boleh negatif.")

    # Memastikan stok memenuhi aturan yang ditentukan.
    assert stok >= 0, "Stok tidak boleh negatif."

    return True


# Pengujian lokal fungsi validasi.
if __name__ == "__main__":
    try:
        validasi_barang("B001", "Laptop", "Elektronik", 10)
        print("Data barang valid.")
    except ValueError as error:
        print("Validasi gagal:", error)