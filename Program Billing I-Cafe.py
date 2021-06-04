# Variabel Global
## Variabel Menu Awal
data_nama = ["Test Login"]
data_email = ["testlogin@gmail.com"]
data_password = ["test12345"]
## Variabel Membership
data_namalengkap = []
data_notelpon = []
data_kodeunik = []
## Variabel Loop
keluar = False


# Menu Awal
def menu_awal():
    print("[1] Login")
    print("[2] Daftar")
    print("[3] Keluar")

# Menu Registrasi
def daftar():
    print("---------- Daftar ----------")
    print("\nSilakan Mengisi Data yang Diperlukan")
    
    nama = input("Masukkan Nama Anda \n>> ")
    data_nama.append(nama)

    email = input("Masukkan email Anda \n>> ")
    harus_ada1 = "@gmail.com"
    while not (harus_ada1 in email):
        print("Masukkan email Google yang benar!")
        email = input("\nMasukkan email Google Anda \n>> ")
    data_email.append(email)
    
    password = input("Masukkan Password Anda \n>> ")
    while not (len(password) >= 8 and password.isalnum()):
        print("Masukkan password dengan minimal 8 karakter dengan kombinasi angka dan huruf")
        password = input("\nMasukkan password Anda \n>> ")
    data_password.append(password)

    print("Terima kasih, Data Anda Sudah Terdaftar")
    print("Silakan Login di Menu Awal")
    menu_awal()

# Menu Login
def masuk():
    print("---------- Login ----------")
    print("\nSilakan Masukkan Akun Anda yang telah terdaftar ")
    
    email_login = input("Email: ")
    
    password_login = input("Password: ")
    validasi = False
    while not validasi:
        for i in range(len(data_email)):
            if (email_login == data_email[i]) and (password_login == data_password[i]):
                validasi = True
                print("Login berhasil! \n")
                return data_nama[i]
        if validasi:
            break
        else:
            print("Email atau Password salah!")
            email_login = input("Email: ")
            password_login = input("Password: ")

# Menu Utama setelah Login
def menu_utama(name):
    print("===== Selamat Datang", nama, " =====")
    print("---------- MENU ----------")
    print("[1] Membership")
    print("[2] Transaksi")
    print("[3] Pengaturan Akun")
    print("[4] Keluar")

# Menu Membership
def member():

    def riwayat():
        print("Bentar dulu")
    
    def daftar_member():
        print("Silakan masukkan data diri Anda!")
        nama_member = input("Nama Lengkap:\n>> ")
        data_namalengkap.append(nama_member)

        notelpon = int(input("Nomor Telepon:\n>> "))
        data_notelpon.append(notelpon)

        kode_unik = int(input("Kode Unik:\n>> "))
        data_kodeunik.append(kode_unik)


    def cek_member():
        cek_kode = input("Masukkan kode unik membership Anda:\n>> ")
        validasi = False
        while not validasi:
            for i in range(len(data_kodeunik)):
                if (cek_kode == data_kodeunik[i]):
                    validasi = True
                    print("Anda Mempunyai Membership!\n")
                    print("----- Membership Menu ------")
                    print("[1.] Cek Riwayat Transaksi")
                    print("[2.] Kembali")
                    riwayat_transaksi = int(input("Pilih Menu\n>> "))
                    if riwayat_transaksi == 1:
                        riwayat()
                    elif riwayat_transaksi == 2:
                        menu_utama()
        
            if validasi:
                break
            else:
                print("Kode Unik salah!")
                cek_kode = input("Kode Unik:\n>> ")
                
                print("\nAtau apakah Anda belum medaftar sebagai member?")
                choice = input("Anda ingin mendaftar menjadi member? [Y/N]")
                print("Pendaftaran member dikenakan biaya Rp30.000")
                if choice == "Y":
                    daftar_member()
                else:
                    menu_utama()


    print("Apakah Anda ingin Cek Membership? [Y/N]")
    ini = input().upper()
    if ini == "Y":
        cek_member()
    else:
        menu_utama()


        
    

# Menu Transaksi
def transaksi():
    def billing():
        print("Silakan pilih paket yang Anda inginkan\n>>")
        print("1. Standar (Rp4000/jam)")
        print("2. VIP (Rp6000/jam)")
        print("3. VVIP (Rp9000/jam)")
        print("4. Kembali")
    
    print
    billing()
    while 3:
        pilih3 = int(input("Silakan pilih\n>> "))

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

# Perintah Run
print("===== Internet Billing Cafe =====")
print()
menu_awal()

while 1:
    pilih1 = int(input("Silakan pilih\n>> "))

    if pilih1 == 1:
        nama = masuk()
        break
    elif pilih1 == 2:
        daftar()
    elif pilih1 == 3:
        print("\n"*100)
        keluar = True
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

if keluar:
    print("Terima kasih telah menggunakan program ini!")

else:
    print("===== Internet Billing Cafe =====")
    print()
    menu_utama(nama)

    while 2:
        pilih2 = int(input("Silakan pilih\n>> "))

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

