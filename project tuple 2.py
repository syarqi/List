# Daftar transaksi
transaksi_penjualan = []

# Fungsi untuk mencatat transaksi
def catat_transaksi(id_transaksi, id_produk, jumlah):
    transaksi = (id_transaksi, id_produk, jumlah)
    transaksi_penjualan.append(transaksi)
    print("Transaksi berhasil dicatat: ID Transaksi: {}, ID Produk: {}, Jumlah: {}".format(id_transaksi, id_produk, jumlah))