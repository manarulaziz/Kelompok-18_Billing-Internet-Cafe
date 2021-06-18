## Variabel Menu Awal
data_nama = ["Test Login"]
data_email = ["testlogin@gmail.com"]
data_password = ["test12345"]
data_riwayat = [[]]
user_id = 0
nama = None
## Variabel Membership
data_namalengkap = ["Aji Manarul"]
data_notelpon = ["08123456789"]
data_kodeunik = [12345]

fnb = [
    ["Roti",5000],
    ["Mi Goreng",5000],
    ["Mi Kuah",5000],
    ["Nugget",7000],
    ["Kentang",6000],
    ["Es Teh", 3000],
    ["Es Jeruk", 3000],
    ["Susu", 5000]
]


def run():
    print("===== Internet Billing Cafe =====")
    print()
    menu_awal()


# Menu Awal
def menu_awal():
    print('------------------------------')
    print("[1] Login")
    print("[2] Daftar")
    print("[3] Keluar Program")
    pilih1 = int(input("Silakan pilih\n>> "))
    if pilih1 == 1:
        nama = masuk()
        menu_utama(nama)
    elif pilih1 == 2:
        daftar()
    elif pilih1 == 3:
        keluar()
    else:
        print("Maaf pilihan yang dimasukkan tidak terdaftar")
        print("Coba lagi [Y/N] ?")
        coba = input().upper()
        if coba == "Y":
            menu_awal()
        else:
            keluar()


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
                user_id = i
                return data_nama[i]
        if validasi:
            break
        else:
            print("Email atau Password salah!")
            email_login = input("Email: ")
            password_login = input("Password: ")


def menu_utama(name):
    print("===== Selamat Datang", name, " =====")
    print("---------- MENU ----------")
    print("[1] Membership")
    print("[2] Transaksi")
    print("[3] Pengaturan Akun")
    print("[4] Keluar")

    pilih2 = int(input("Silakan pilih\n>> "))
    if pilih2 == 1:
        member()
    elif pilih2 == 2:
        transaksi()
    elif pilih2 == 3:
        akun()
    elif pilih2 == 4:
        menu_awal()
    else:
        print("Maaf pilihan yang dimasukkan tidak terdaftar")
        print("Coba lagi [Y/N] ?")
        coba = input().upper()
        if coba == "Y":
            menu_utama(name)
        else:
            menu_awal()


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
    data_riwayat.append([])
    data_namalengkap.append("")
    data_notelpon.append("")
    data_kodeunik.append("")

    print("Terima kasih, Data Anda Sudah Terdaftar")
    print("Silakan Login di Menu Awal")
    menu_awal()

def keluar():
    print("===========================================")
    print("Terima kasih telah menggunakan program ini!")
    print("===========================================")
    exit()


def riwayat():
    total = 0
    for i in range(len(data_riwayat[user_id])):
        print("[{}] {:<9s} : Rp{},00".format(i + 1, data_riwayat[user_id][i][0], data_riwayat[user_id][i][1]))
        total += data_riwayat[user_id][i][1]

    print(f"Total harga: {total}")
    menu_utama(nama)

# Membership
def daftar_member():
    print("Silakan masukkan data diri Anda!")
    nama_member = input("Nama Lengkap:\n>> ")
    data_namalengkap[user_id] = nama_member

    notelpon = int(input("Nomor Telepon:\n>> "))
    data_notelpon[user_id] = notelpon

    kode_unik = int(input("Kode Unik:\n>> "))
    data_kodeunik[user_id] = kode_unik
    print("\n Pendaftaran Member berhasil! \n")
    data_riwayat[user_id].append(["Pendaftaran Member", 30000])
    menu_utama(nama)


def cek_member():
    cek_kode = int(input("Masukkan kode unik membership Anda:\n>> "))
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
                    menu_utama(nama)
        
        if validasi:
            break
        else:
            print("Kode Unik salah!")
            cek_kode = input("Kode Unik:\n>> ")
                
            print("\nAtau apakah Anda belum mendaftar sebagai member?")
            choice = input("Anda ingin mendaftar menjadi member? [Y/N]").upper()
            print("Pendaftaran member dikenakan biaya Rp30.000")
            if choice == "Y":
                daftar_member()
            else:
                menu_utama(nama)


def member():
    print("Apakah Anda mempunyai Membership? [Y/N]")
    itu = input().upper()
    if itu == "Y":
        print("Apakah Anda ingin Cek Membership? [Y/N]")
        ini = input().upper()
        if ini == "Y":
            cek_member()
        elif ini == "N":
            menu_utama(nama)
    elif itu == "N":
        print("Apakah Anda ingin mendaftar Membership? [Y/N]")
        print("Pendaftaran member dikenakan biaya Rp30.000")
        iniitu = input().upper()
        if iniitu == "Y":
            daftar_member()
        elif iniitu == "N":
            menu_utama(nama)

# Transaksi
def billing():
    print("Silakan pilih paket yang Anda inginkan")
    print("1. Standar (Rp4000/jam)")
    print("2. VIP (Rp6000/jam)")
    print("3. VVIP (Rp9000/jam)")
    print("4. Kembali")


def transaksi():
    billing()
    pilih3 = int(input("Silakan pilih\n>> "))
    if pilih3 == 1:
        standar = 4000
        durasi = int(input("Input durasi (jam): "))
        net = durasi * standar
        data_riwayat[user_id].append(["Standar", net])
        inifnb()
    elif pilih3 == 2:
        vip = 6000
        durasi = int(input("Input durasi (jam): "))
        net = durasi * vip
        data_riwayat[user_id].append(["VIP", net])
        inifnb()
    elif pilih3 == 3:
        vvip = 9000
        durasi = int(input("Input durasi (jam): "))
        net = durasi * vvip
        data_riwayat[user_id].append(["VVIP", net])
        inifnb()
    elif pilih3 == 4:
        menu_utama(nama)
    else:
        transaksi()


def inifnb():
    while True:
        pilihan = input("Apakah anda ingin memesan makanan/minuman ? [y/n] ").upper()
        if pilihan == 'Y':
            isPesan = 'Y'
            while True:
                if isPesan == 'Y':
                    print("Daftar Harga")
                    for i, j in enumerate(fnb):
                        print("[{}] {:<9s} : Rp{},00".format(i, j[0], j[1]))

                    input_menu = int(input("Silahkan pilih menu makanan atau minuman:"))
                    while (input_menu < 0 or input_menu > 7):
                        print("Input tidak valid")
                        input_menu = int(input("Silahkan pilih menu makanan atau minuman:"))

                    data_riwayat[user_id].append([fnb[input_menu][0], fnb[input_menu][1]])
                    isPesan = input("Apakah anda ingin memesan makanan/minuman yang lain? [Y/N] ").upper()
                    # masih error saat memilih menu yang nomor 8
                elif isPesan == 'N':
                    print(riwayat())
                    menu_utama(nama)
                else:
                    print("Input tidak valid.")
                    menu_utama(nama)

            break
        elif pilihan == 'N':
            print(riwayat())
            menu_utama(nama)
        else:
            print("Input salah.")
            menu_utama(nama)

# Pengaturan Akun
def ubahpass():
    pass_lama = input("Masukkan Password Lama Akun Anda\n>> ")
    if pass_lama in data_password:
        pass_baru = input("Masukkan Password Baru\n>> ")
        while not (len(pass_baru) >= 8 and pass_baru.isalnum()):
            print("Masukkan password dengan minimal 8 karakter dengan kombinasi angka dan huruf")
            pass_baru = input("\nMasukkan password Anda \n>> ")
    data_password[user_id] = pass_baru
    print("Password akun Anda sudah diubah!")
    menu_utama(nama)

def ubahemail():
    email_lama = input("Masukkan Email Lama Akun Anda\n>> ")
    if email_lama in data_email:
        email_baru = input("Masukkan Email Baru\n>> ")
        harus_ada1 = "@gmail.com"
        while not (harus_ada1 in email_baru):
            print("Masukkan email Google yang benar!")
            email_baru = input("\nMasukkan email Google Anda \n>> ")
    data_email[user_id] = email_baru
    print("Email akun Anda sudah diubah!")
    menu_utama(nama)

def hapusakun():
    data_email.pop(user_id)
    data_password.pop(user_id)
    data_nama.pop(user_id)
    data_namalengkap.pop(user_id)
    data_notelpon.pop(user_id)
    data_kodeunik.pop(user_id)
    data_riwayat.pop(user_id)
    print("Akun Anda sudah dihapus!")
    menu_awal()


def akun():
    print("---------- PENGATURAN AKUN ----------")
    print("[1] Ubah Kata Sandi")
    print("[2] Ubah Email")
    print("[3] Hapus Akun")
    print("[4] Kembali")

    pilih4 = int(input("Silakan pilih\n>> "))
    while 4:
        if pilih4 == 1:
            ubahpass()
        elif pilih4 == 2:
            ubahemail()
        elif pilih4 == 3:
            hapusakun()
        elif pilih4 == 4:
            menu_utama(nama)

#----Run Program----
run()