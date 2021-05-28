def menu_utama():
    print("---------- MENU ----------")
    print("[1] Membership")
    print("[2] Transaksi")
    print("[3] Pengaturan Akun")
    print("[4] Keluar")

    menu = int(input(">> "))
    print("\n")

if __name__ == '__main__':
    menu_utama()

    
durasi = int(input("Input durasi (jam): "))


def fnb():
    print("Food and Beverage")
    print("[1] Roti      : Rp5.000,00")
    print("[2] Mi Goreng : Rp5.000,00")
    print("[3] Mi Kuah   : Rp5.000,00")
    print("[4] Nugget    : Rp7.000,00")
    print("[5] Kentang   : Rp8.000,00")
    print("[6] Es Teh    : Rp3.000,00")
    print("[7] Es Jeruk  : Rp3.000,00")
    print("[8] Susu      : Rp5.000,00")

    fnb = int(input("Pilih satu >> "))
    if fnb == 1:
        harga = 5000
    elif fnb == 2:
        harga = 5000
    elif fnb == 3:
        harga = 5000
    elif fnb == 4:
        harga = 7000
    elif fnb == 5:
        harga = 8000
    elif fnb == 6:
        harga = 3000
    elif fnb == 7:
        harga = 3000
    elif fnb == 8:
        harga = 3000
    else:
        while True:
            print("=====Menu Tidak Tersedia,Silahkan Pilih Menu Lainnya!!=====")
            fnb = int(input("Masukan menu pesanan (Nomer Menu) : "))
            if fnb == 1 or fnb == 2 or fnb == 3 or fnb == 4 or fnb == 5 or fnb == 6 or fnb == 7 or fnb == 8:
                if fnb == 1:
                    harga = 5000
                elif fnb == 2:
                    harga = 5000
                elif fnb == 3:
                    harga = 5000
                elif fnb == 4:
                    harga = 7000
                elif fnb == 5:
                    harga = 8000
                elif fnb == 6:
                    harga = 3000
                elif fnb == 7:
                    harga = 3000
                elif fnb == 8:
                    harga = 3000
                else:
                    break
    jumlah_pembelian = int(input("Masukan Jumlah Pembelian : "))

