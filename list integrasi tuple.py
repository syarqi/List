# Loop utama yang diperbarui
while True:
    loading2("")
    print("===============================")
    print("MENU:")
    print("1. Tambah Item")
    print("2. Lihat Daftar")
    print("3. Hapus Item")
    print("4. Catat Transaksi")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")
    print("===============================")

    if pilihan == "1":
        pilihan1 = "Menambah Item"
    elif pilihan == "2":
        pilihan1 = "Melihat Daftar"
    elif pilihan == "3":
        pilihan1 = "Menghapus Item"
    elif pilihan == "4":
        pilihan1 = "Mencatat Transaksi"
    elif pilihan == "5":
        pilihan1 = "Keluar"
    else:
        pilihan1 = ""

    loading2("'{}', mohon tunggu".format(pilihan1))

    if pilihan == "1":
        item = input("Masukkan nama item: ")
        tambah_item(item)
    elif pilihan == "2":
        tampilkan_daftar()
    elif pilihan == "3":
        tampilkan_daftar()
        if daftar_belanja:
            try:
                nomor = int(input("Masukkan nomor item yang mau dihapus: "))
                hapus_item(nomor - 1)
            except ValueError:
                print("Masukkan angka yang valid!\n")
    elif pilihan == "4":
        id_transaksi = input("Masukkan ID Transaksi: ")
        id_produk = input("Masukkan ID Produk: ")
        jumlah = int(input("Masukkan Jumlah: "))
        catat_transaksi(id_transaksi, id_produk, jumlah)
    elif pilihan == "5":
        print("\nTerima kasih sudah menggunakan aplikasi belanja!\n")
        break
    else:
        print("Pilihan tidak valid! Coba lagi.\n")