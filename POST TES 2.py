from prettytable import PrettyTable

# MEMBUAT LIST BARANG DAN HARGA
barang = ['PENSIL', 'PULPEN', 'BUKU', 'PENGHAPUS', 'STIP X']
harga = [4000, 4500, 5500, 3000, 4200]

# MEMBUAT LIST MENGGUNAKAN P
atk = PrettyTable()
atk.field_names = ['Barang', 'Harga']
atk.add_rows([
    ['Pensil', 4000],
    ['Pulpen', 4500],
    ['Buku', 5500],
    ['Penghapus', 3000],
    ['Stip X', 4200]
])

# MEMBUAT FUNGSI UNTUK MENU ADMIN
def tambah_barang():
    nama_barang = input("Masukkan nama barang: ")
    harga_barang = int(input("Masukkan harga barang: "))
    atk.add_row([nama_barang, harga_barang])
    print(f"Barang {nama_barang} telah ditambahkan.")

def barui_barang():
    nama_barang = input("Masukkan nama barang yang ingin diperbarui: ")
    harga_barang = int(input("Masukkan harga barang baru: "))
    for row in atk._rows:
        if row[0].lower() == nama_barang.lower():
            row[1] = harga_barang
            print(f'Harga {nama_barang} telah diubah menjadi Rp. {harga_barang}')
            print(f"Harga barang {nama_barang} telah diperbarui.")
            return
    print(f"Barang {nama_barang} tidak ditemukan.")

def hapus_barang():
    nama_barang = input("Masukkan nama barang yang ingin dihapus: ")
    for i, row in enumerate(atk._rows):
        if row[0].lower() == nama_barang.lower():
            atk.del_row(i)
            print(f"Barang {nama_barang} telah dihapus.")
            return
    print(f"Barang {nama_barang} tidak ditemukan.")

# Display the main menu
while True:
    print("======================================================")
    print("|      ----------------------------------------      |")
    print("|      SELAMAT DATANG DI TOKO ATK SHOPIEE PARIS      |")
    print("|      ----------------------------------------      |")
    print("======================================================")
    print("                                                      ")
    print("+----------------------------------------------------+")
    print("|         >|SILAHKAN PILIH ROLE ANDA|<               |")
    print("+----------------------------------------------------+")
    print("|[1] PEMBELI                                         |")
    print("|[2] ADMIN                                           |")
    print("|[3] KELUAR                                          |")
    print("+----------------------------------------------------+")

    # USER MEMILIH ROLE
    role = int(input("Masukkan pilihan 1/2/3: "))
    if role == 1:
        print("SELAMAT DATANG DI TOKO KAMI. SELAMAT MENGHABISKAN UANG ANDA")
        print("=====================")
        print("|      TERSEDIA     |")
        print("=====================")
        print(atk)
        print("=====================")
        print("|[1] TRANSAKSI       |")
        print("|[2] KELUAR          |")
        print("=====================")
        # PEMBELI MELAKUKAN PILIHAN
        pembeli = int(input("Masukkan pilihan 1/2: "))
        # PEMBELI MELAKUKAN TRANSAKSI
        if pembeli == 1:
            keranjang = {}
            while True:
                print("+-------------------+")
                print("|      TRANSAKSI    |")
                print("+-------------------+")
                print("|[1] TAMBAH BARANG  |")
                print("|[2] CHECKOUT       |")
                print("|[3] KELUAR         |")
                print("+--------------------+")
                lakukan = int(input("Masukkan pilihan 1/2/3: "))
                # BARIS CODE UNTUK MENJALANKAN MENU PEMBELI
                if lakukan == 1:
                    nama_barang = input("Masukkan nama barang yang ingin ditambahkan ke keranjang: ")
                    if nama_barang.lower() in [item.lower() for item in barang]:
                        jumlah_barang = int(input("Masukkan jumlah barang: "))
                        if nama_barang in keranjang:
                            keranjang[nama_barang] += jumlah_barang
                        else:
                            keranjang[nama_barang] = jumlah_barang
                        print(f"{jumlah_barang} {nama_barang} telah ditambahkan ke keranjang.")
                    else:
                        print(f"Barang {nama_barang} tidak ditemukan.")
                elif lakukan == 2:
                    total_harga = 0
                    print("+--------------------+")
                    print("| KERANJANG BELANJA  |")
                    print("+--------------------+")
                    for item, jumlah in keranjang.items():
                        for row in atk._rows:
                            if row[0].lower() == item.lower():
                                subtotal = jumlah * row[1]
                                total_harga += subtotal
                                print(f"{item} x{jumlah}: Rp. {subtotal}")
                    print("============================")
                    print(f"TOTAL HARGA: Rp. {total_harga}")
                    print("============================")
                    print("TERIMA KASIH SUDAH MENGHABISKAN UANG ANDA SAMAPI JUMPA LAGI :) ")
                    break
                elif lakukan == 3:
                    break
                else:
                    print("MAAF KAMI TIDAK DAPAT MEMBANTU ANDA.")

    elif role == 2:
        # Admin
        print("SELAMAT DATANG MIMIN")
        # MENU ADMIN
        print(atk)
        print("=======================")
        print("|      OPSI ADMIN      |")
        print("=======================")
        print("|[1] MENAMBAHKAN BARANG|")
        print("|[2] MENAMPILKAN BARANG|")
        print("|[3] MEMPERBARUI BARANG|")
        print("|[4] MENGHAPUS BARANG  |")
        print("|[5] KELUAR            |")
        print("=======================")

        while True:
            # ADMIN MENENTUKAN PILIHAN
            menu_admin = int(input("Masukkan pilihan 1/2/3/4/5: "))

            if menu_admin == 1:
                tambah_barang()
            elif menu_admin == 2:
                print(atk)
            elif menu_admin == 3:
                barui_barang()
            elif menu_admin == 4:
                hapus_barang()
            elif menu_admin == 5:
                break
            else:
                print("MAAF KAMI TIDAK DAPAT MEMBANTU MIN.")
    elif role == 3:
        break
    else:
        print("MAAF KAMI TIDAK DAPAT MEMBANTU ANDA.")
