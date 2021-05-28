# Tahap 1
def menu_awal():
    print("[1] Login")
    print("[2] Daftar")
    print("[3] Keluar")

def masuk():
    print("---------- Login ----------")
    print("\nSilakan Masukkan Akun Anda yang telah terdaftar ")
    email_login = input("Email: ")
    password_login = input("Password: ")

def daftar():
    print("---------- Daftar ----------")
    print("\nSilakan Mengisi Data yang Diperlukan")
    nama = input("Nama: ")
    email_daftar = input("Email: ")
    password_daftar = input("Password:")
    print("Terima kasih, Data Anda Sudah Terdaftar")
    print("Silakan Login di Menu Awal")
    menu_awal()

def menu_utama():
    print("===== Selamat Datang =====")
    print("---------- MENU ----------")
    print("[1] Membership")
    print("[2] Transaksi")
    print("[3] Pengaturan Akun")
    print("[4] Keluar")

def member():
    print("Anda belum terdaftar sebagai member")
    choice = input("Anda ingin mendaftar menjadi member? [Y/N]")
    if choice == "Y":
        print()
    else:
        menu_utama()

def transaksi():
    def billing():
        print("1. Standar (Rp4000/jam)")
        print("2. VIP (Rp6000/jam)")
        print("3. VVIP (Rp9000/jam)")
        print("4. Kembali")
    
    print
    billing()
    while 3:
        pilih3 = int(input("Silakan pilih: "))

        if pilih3 == 1:
            standar = 4000
            durasi = int(input("Input durasi (jam): "))
            net = durasi * standar
        elif pilih3 == 2:
            vip = 6000
            durasi = int(input("Input durasi (jam): "))
            net = durasi * vip
        elif pilih3 == 3:
            vvip = 4000
            durasi = int(input("Input durasi (jam): "))
            net = durasi * vvip
        elif pilih3 == 4:
            menu_utama()

# fnb dimasukin ke menu billing terus ditotal


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

def akun(): # tahap 2
    print("")

print("===== Internet Billing Cafe =====")
print
menu_awal()

while 1:
    pilih1 = int(input("Silakan pilih \n>> "))

    if pilih1 == 1:
        masuk()
    elif pilih1 == 2:
        daftar()
    elif pilih1 == 3:
        print("\n"*100)
        break
    else:
        print("Maaf pilihan yang dimasukkan tidak terdaftar")
        print("Coba lagi [Y/N] ?")
        coba = input().upper()
        if coba == "Y":
            menu_awal()
        else:
            print("\n")*100
            break

print("===== Internet Billing Cafe =====")
print
menu_utama()

while 2:
    pilih2 = int(input("Silakan pilih: \n>>"))

    if pilih2 == 1:
        member()
    elif pilih2 == 2:
        transaksi()
    elif pilih2 == 3:
        akun()
    elif pilih2 == 4:
        menu_awal()
    elif pilih2 == 5:
        print("Maaf pilihan yang dimasukkan tidak terdaftar")
        print("Coba lagi [Y/N] ?")
        coba = input().upper()
        if coba == "Y":
            menu_utama()
        else:
            print("\n")*100
            break
