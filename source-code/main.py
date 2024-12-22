# Author : Kelompok 7
# Tanggal Pengerjaan : 
# - Tugas Besar 1 (3-10 November 2024)                 
# - Tugas Besar 2 (7-22 Desember 2024)

# Program Manajemen Sistem Pintu Tol Lanjutan
# Deskripsi : Menghitung tarif tol berdasarkan jarak dan golongan kendaraan dari pintu masuk gerbang tol dan pintu keluar gerbang tol yang diinput oleh user

# KAMUS
# pintu: array of string
# jarakPintu: array of array of float
# jenisKendaraan, pintuMasuk, pintuKeluar, pilihan, saldoAwal, biaya: integer
# daftarPintu, opsi_saldo: array of integer
# saldo, jarak, tarif, saldoTerakhir: float
# exclude: integer or None
# poin: integer
# pilihan: prosedur untuk menampilkan daftar pintu tol yang tersedia
# tarifTol: fungsi untuk menghitung tarif tol berdasarkan jarak dan golongan kendaraan
# pilihPintuMasuk: fungsi untuk memilih pintu masuk tol
# pilihPintuKeluar: fungsi untuk memilih pintu keluar tol
# hitungJarak: fungsi untuk menentukan jarak antara pintu masuk dan pintu keluar menggunakan for loop
# inputJenisKendaraan: fungsi untuk memasukkan jenis kendaraan
# simulasiWaktuTempuh: fungsi untuk mensimulasikan waktu tempuh kendaraan berdasarkan jarak dan jenis kendaraan
# inputSaldo: fungsi untuk memasukkan saldo e-toll
# cekSaldo: fungsi untuk mengecek apakah saldo mencukupi
# pilihanSaldo: prosedur untuk menampilkan opsi isi ulang saldo dan memproses input pengguna
# hitungPoin: fungsi untuk menghitung poin berdasarkan tarif transaksi
# poinDiskon: fungsi untuk memberikan opsi penukaran poin untuk diskon tarif tol
# tampilkanRingkasan: prosedur untuk menampilkan ringkasan transaksi
# main: prosedur utama untuk mengelola alur program


# Perubahan yang dilakukan
# - Perbaikan alur logika algoritma
# - Menambah simulasi waktu tempuh kendaraan
# - Menambah fitur poin 

# Algoritma
import os
import time

# Daftar pintu tol yang tersedia
pintu = ["Cikampek Utama", "Palimanan", "Kanci", "Brebes Timur", "Pemalang"]

# Fungsi untuk menampilkan daftar pilihan pintu tol
def pilihan(pintu1, pintu2, pintu3, pintu4, pintu5, exclude=None):
    daftarPintu = [pintu1, pintu2, pintu3, pintu4, pintu5]
    for i, pintu in enumerate(daftarPintu, start=1):
        if i != exclude:  # Berguna untuk menghindari menampilkan pintu yang sudah dipilih
            print(f"    [{i}] {pintu}")
    print("    Masukkan pilihan Anda: ", end="")

# Fungsi untuk menghitung tarif tol berdasarkan jarak dan golongan kendaraan
def tarifTol(jarak, golongan):
    tarif = (jarak * 500) + (golongan * 1000)
    return tarif

# Fungsi untuk memilih pintu masuk tol
def pilihPintuMasuk():
    print("    Silakan Pilih Pintu Masuk Tol:")
    pilihan(*pintu)
    try:
        pintuMasuk = int(input())
        while pintuMasuk < 1 or pintuMasuk > 5:
            print("    Silakan input angka antara 1 sampai 5.")
            pintuMasuk = int(input("Masukkan pilihan: "))
        return pintuMasuk
    except:
        print("    Input tidak valid. Silakan coba lagi.")
        return pilihPintuMasuk()  

# Fungsi untuk memilih pintu keluar tol
def pilihPintuKeluar(pintuMasuk):
    print("\n    Silakan Pilih Pintu Keluar Tol:")
    pilihan(*pintu, exclude=pintuMasuk)  # Tidak menampilkan pintu yang sama dengan pintu masuk
    try:
        pintuKeluar = int(input())
        
        # Validasi agar pintu keluar tidak sama dengan pintu masuk
        while pintuKeluar < 1 or pintuKeluar > 5 or pintuKeluar == pintuMasuk:
            if pintuKeluar == pintuMasuk:
                print(f"    Pilih pintu keluar tol selain pintu {pintu[pintuMasuk - 1]}.")
            else:
                print("    Silakan input angka antara 1 sampai 5.")
            pintuKeluar = int(input("Tuliskan angka pilihan Anda: "))
        return pintuKeluar
    except:
        print("     Input tidak valid. Silakan coba lagi.")
        return pilihPintuKeluar(pintuMasuk)

# Fungsi untuk menentukan jarak antara pintu masuk dan keluar
jarakPintu = [
    [0.0, 125.9, 137.5, 207.7, 257.4],  # Cikampek Utama (Pintu 1)
    [126, 0.0, 45.1, 88.9, 138.6],   # Palimanan (Pintu 2)
    [164.1, 78.8, 0.0, 37.8, 119.9],   # Kanci (Pintu 3)
    [203.5, 81.7, 66.7, 0.0, 56.2],   # Brebes Timur (Pintu 4)
    [257.1, 135.3, 120.2, 39.0, 0.0]  # Pemalang (Pintu 5)
]

def hitungJarak(pintuMasuk, pintuKeluar):
    # Loop melalui indeks baris
    for i in range(len(jarakPintu)):
        if i + 1 == pintuMasuk:  # PintuMasuk cocok dengan indeks baris + 1
            # Loop melalui indeks kolom
            for j in range(len(jarakPintu[i])):
                if j + 1 == pintuKeluar:  # PintuKeluar cocok dengan indeks kolom + 1
                    return jarakPintu[i][j]  # Kembalikan nilai berdasarkan jarak yang sesuai
    # Jika tidak ditemukan
    print(f"Jarak antara pintu {pintuMasuk} dan {pintuKeluar} tidak ditemukan. Silahkan ulangi lagi")
    return -1.0


# Fungsi untuk input jenis kendaraan
def inputJenisKendaraan():
    print("\n    ======================================================")
    print("                   DAFTAR GOLONGAN KENDARAAN   ")
    print("    ======================================================")
    print("    Golongan I   : Sedan, Jip, Pick Up/Truk Kecil, dan Bus")
    print("    Golongan II  : Truk dengan 2 (dua) gandar")
    print("    Golongan III : Truk dengan 3 (tiga) gandar")
    print("    Golongan IV  : Truk dengan 4 (empat) gandar")
    print("    Golongan V   : Truk dengan 5 (lima) gandar")
    print("    ======================================================")
    
    while True:  # Loop untuk memastikan input valid
        try:
            jenis = int(input("    Masukkan jenis kendaraan Anda (1/2/3/4/5): "))
            if 1 <= jenis <= 5:
                return jenis
            else:
                print("   Golongan kendaraan harus antara 1 dan 5. Silakan pilih ulang.")
        except ValueError:
            print("    Input tidak valid. Harap masukkan angka yang sesuai daftar.")

# Fungsi untuk menyimulasikan waktu yang diperlukan bagi kendaraan untuk menempuh jarak antar tol
def simulasiWaktuTempuh(jarak, golongan):
    kecepatan = {
        1: 100, # Golongan I
        2: 80, # Golongan II
        3: 60, # Golongan III
        4: 50, # Golongan IV
        5: 40, # Golongan V
    }

    # Waktu tempuh dalam jam
    waktu_tempuh = jarak / kecepatan[golongan]

    # Konversi ke jam dan menit
    jam = int(waktu_tempuh)
    menit = int((waktu_tempuh - jam) * 60)
    return jam, menit

# Fungsi untuk input saldo
def inputSaldo():
    try:
        saldo = int(input("    Silahkan input saldo e-toll Anda: "))
        if saldo >= 0:
            return saldo
        else:
            print("    Input tidak valid. Saldo harus berupa angka positif.")
            return inputSaldo()
    except:
        print("    Input tidak valid. Harap masukkan angka yang benar.")
        return inputSaldo()

# Fungsi untuk mengecek apakah saldo dari pengguna cukup
def cekSaldo(saldo, biaya):
    return saldo >= biaya

# Fungsi untuk menampilkan opsi isi ulang saldo dan memproses input pengguna
def pilihanSaldo(saldoAwal, biaya):
    print("\n    Saldo Anda tidak mencukupi. Pilih jumlah isi ulang:")
    opsi_saldo = [50000, 100000, 200000, 300000, 500000, 1000000, biaya - saldoAwal]
    
    for i, opsi in enumerate(opsi_saldo, 1):
        if opsi == biaya - saldoAwal:
            print(f"    [{i}] Isi saldo otomatis sebesar Rp {opsi} (sesuai tarif)")
        else:
            print(f"    [{i}] Rp {opsi}")
    
    try:
        pilihan = int(input("    Pilih opsi isi saldo: "))
        if 1 <= pilihan <= len(opsi_saldo):
            saldoAwal += opsi_saldo[pilihan - 1]
            print(f"    Isi saldo berhasil. Saldo saat ini: Rp {saldoAwal}")
            return saldoAwal
        else:
            print("    Pilihan tidak valid. Silakan coba lagi.")
            return pilihanSaldo(saldoAwal, biaya)
    except:
        print("    Input tidak valid. Silakan coba lagi.")
        return pilihanSaldo(saldoAwal, biaya)

def hitungPoin(tarif):
    # 1 poin = Rp 1.000
    return tarif // 1000

# Fungsi untuk menghitung jumlah poin 
def poinDiskon(poin, tarif):
    print("\n    Anda memiliki", poin, "poin.")
    print("    Tukarkan poin untuk diskon:")
    print("    [1] 10 poin = Diskon 5%")
    print("    [2] 20 poin = Diskon 10%")
    print("    [3] Lanjut tanpa menukarkan poin")

    pilihan = int(input("    Masukkan pilihan Anda: "))
    os.system('cls' if os.name == 'nt' else 'clear')

    if pilihan == 1 and poin >= 10:
        diskon = tarif * 0.05
        print(f"    Anda mendapatkan diskon 5%. Diskon: Rp {diskon:.0f}")
        return diskon, poin - 10
    elif pilihan == 2 and poin >= 20:
        diskon = tarif * 0.10
        print(f"    Anda mendapatkan diskon 10%. Diskon: Rp {diskon:.0f}")
        return diskon, poin - 20
    elif pilihan == 3:
        print("    Anda memilih untuk tidak menukarkan poin.")
        return 0, poin
    else:
        print("    Poin Anda tidak mencukupi untuk diskon ini.")
        return 0, poin

# Fungsi untuk menampilkan ringkasan transaksi
def tampilkanRingkasan(pintuMasuk, pintuKeluar, jenisKendaraan, jarak, tarif, saldoTerakhir):
    jam, menit = simulasiWaktuTempuh(jarak, jenisKendaraan)

    tampilanRingkasan = [
        f"""
    ===============================
          RINGKASAN TRANSAKSI
    ===============================
    Pintu Masuk     : {pintu[pintuMasuk - 1]}
    Pintu Keluar    : {pintu[pintuKeluar - 1]}
    Golongan Kendaraan : {jenisKendaraan}
    Jarak Tempuh    : {jarak:.2f} km
    Waktu Tempuh    : {jam} jam {menit} menit
    -------------------------------
    Tarif Tol       : Rp {tarif}
    Sisa Saldo      : Rp {saldoTerakhir}
    ===============================
    Terima kasih atas kunjungan Anda
    Selamat melanjutkan perjalanan!
    ===============================
    """
    ]

    for teks in tampilanRingkasan:
        for huruf in teks:
            print(huruf, end='', flush=True)
            time.sleep(0.03)  # Jeda 0,03 detik antar huruf
        print()  
        
# Fungsi utama
def main():
    print("    ===== Selamat datang di Gerbang Pintu Tol =====    ")

    global poin
    poin = 0

    while True:
        # Memilih pintu masuk tol
        pintuMasuk = pilihPintuMasuk()
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Memilih pintu keluar tol
        pintuKeluar = pilihPintuKeluar(pintuMasuk)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Meminta input jenis kendaraan 
        jenisKendaraan = inputJenisKendaraan()
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Menghitung jarak antara pintu masuk dan keluar
        jarak = hitungJarak(pintuMasuk, pintuKeluar)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Menghitung tarif berdasarkan jarak dan golongan kendaraan pengguna
        tarif = tarifTol(jarak, jenisKendaraan)

        # Menggunakan poin untuk menerapkan diskon pada tarif tol
        if poin > 0:
            diskon, poin = poinDiskon(poin, tarif)
            tarif -= diskon 
        else: 
            print("\n    Anda belum memiliki poin untuk ditukarkan.")

        # Input saldo e-toll pengguna
        saldo = inputSaldo()
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Cek saldo, jika saldo kurang, maka akan langsung ditawarkan opsi untuk isi ulang saldo
        if not cekSaldo(saldo, tarif):
            saldo = pilihanSaldo(saldo, tarif)

        # Menghitung total poin dari transaksi
        transaksi_poin = hitungPoin(tarif)
        poin += transaksi_poin  # Tambahkan poin ke total poin pengguna
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Menampilkan ringkasan transaksi dengan sisa saldo pengguna
        tampilkanRingkasan(pintuMasuk, pintuKeluar, jenisKendaraan, jarak, tarif, saldo - tarif)
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"\n    Anda mendapatkan {transaksi_poin} poin dari transaksi ini.")
        print(f"    Total poin Anda sekarang: {poin}")

        # Melanjutkan ke transaksi lain
        lanjut = input("\n    Apakah Anda ingin melakukan transaksi lain? (y/n): ").lower()
        os.system('cls' if os.name == 'nt' else 'clear')
        if lanjut != 'y':
            print("\n    Terima kasih telah menggunakan layanan tol kami!")
            break
        os.system('cls' if os.name == 'nt' else 'clear')

# Untuk menjalankan program
if __name__ == "__main__":
    main()
