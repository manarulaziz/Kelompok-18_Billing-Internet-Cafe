# Variabel Global
## Variabel Menu Awal
data_nama = ["Test Login"]
data_email = ["testlogin@gmail.com"]
data_password = ["test12345"]
data_riwayat = [[]]
user_id = 0
## Variabel Membership
data_namalengkap = ["Aji Manarul"]
data_notelpon = ["08123456789"]
data_kodeunik = ["12345"]
## Variabel Loop
keluar = False

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

dictFnb = {
	"Roti":5000,
	"Mi Goreng":5000,
	"Mi Kuah":5000,
	"Nugget":7000,
	"Kentang":6000,
    "Es Teh": 3000,
    "Es Jeruk": 3000,
    "Susu": 5000
}

formatRupiah = lambda angka : "Rp {:0,.0f}".format(angka)


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
    data_riwayat.append([])
    data_namalengkap.append("")
    data_notelpon.append("")
    data_kodeunik.append("")

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
                user_id = i
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
        total = 0
        for i in range(len(data_riwayat[user_id])):
            print("[{}] {:<9s} : Rp{},00".format(i+1, data_riwayat[user_id][i][0], data_riwayat[user_id][i][1]))
            total += data_riwayat[user_id][i][1]

        print(f"Total harga: {total}")
        # masih belum ada fungsi untuk balik ke menu utama secara baik
    
    def daftar_member():
        print("Silakan masukkan data diri Anda!")
        nama_member = input("Nama Lengkap:\n>> ")
        data_namalengkap[user_id](nama_member) # masih error

        notelpon = int(input("Nomor Telepon:\n>> "))
        data_notelpon[user_id](notelpon) # masih error

        kode_unik = int(input("Kode Unik:\n>> "))
        data_kodeunik[user_id](kode_unik) # masih error


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
                        menu_utama(nama)
        
            if validasi:
                break
            else:
                print("Kode Unik salah!")
                cek_kode = input("Kode Unik:\n>> ")
                
                print("\nAtau apakah Anda belum mendaftar sebagai member?")
                choice = input("Anda ingin mendaftar menjadi member? [Y/N]")
                print("Pendaftaran member dikenakan biaya Rp30.000")
                if choice == "Y":
                    daftar_member()
                else:
                    menu_utama(nama)


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


def inifnb():
    while True:
        pilihan = input("Apakah anda ingin memesan makanan/minuman ? [y/n] ")
        if pilihan == 'y':
            isPesan = 'y'
            while True:
                if isPesan == 'y':
                    print("Daftar Harga")
                    for i, j in enumerate(fnb):
                        print("[{}] {:<9s} : Rp{},00".format(i + 1, j[0], j[1]))

                    input_menu = int(input("Silahkan pilih menu makanan atau minuman:"))
                    while (input_menu < 1 or input_menu > 8):
                        print("Input tidak valid")
                        input_menu = int(input("Silahkan pilih menu makanan atau minuman:"))
                        #

                    data_riwayat[user_id].append([fnb[input_menu][0], fnb[input_menu][1]])
                    isPesan = input("Apakah anda ingin memesan makanan/minuman yang lain? [y/n] ")
                    # masih error saat memilih menu yang nomor 8
                elif isPesan == 'n':
                    break
                else:
                    print("Input tidak valid.")

                break
                elif pilihan == 'n':
                # masih ada banyak tambahan harusnya misal total harga dan keterangan lainnya
                break
            else:
                print("Input salah.")
                break


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


def akun(): # cek lagi logikanya belum masuk

    def ubahpass():
        pass_lama = input("Masukkan Password Lama Akun Anda\n>> ")
        if pass_lama is data_password:
            pass_baru = input("Masukkan Password Baru\n>> ")
            while not (len(pass_baru) >= 8 and pass_baru.isalnum()):
                print("Masukkan password dengan minimal 8 karakter dengan kombinasi angka dan huruf")
                pass_baru = input("\nMasukkan password Anda \n>> ")
        data_password[0] = pass_baru
    def ubahemail():
        email_lama = input("Masukkan Email Lama Akun Anda\n>> ")
        if email_lama is data_email:
            email_baru = input("Masukkan Email Baru\n>> ")
            harus_ada1 = "@gmail.com"
            while not (harus_ada1 in email):
                print("Masukkan email Google yang benar!")
                email = input("\nMasukkan email Google Anda \n>> ")
        data_email[0] = email_baru
    def hapusakun():
        print("")

    print("---------- PENGATURAN AKUN ----------")
    print("[1] Ubah Kata Sandi")
    print("[2] Ubah Email")
    print("[3] Hapus Akun")
    print("[4] Keluar")

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
