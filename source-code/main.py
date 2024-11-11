# Author : Kelompok 7
# Tanggal Pengerjaan : 3 November 2024

# Program Manajemen Sistem Pintu Tol
# Deskripsi : Menghitung tarif tol berdasarkan jarak dan golongan kendaraan dari pintu masuk gerbang tol dan pintu keluar gerbang tol yang diinput oleh user

# KAMUS
# pintu: array of string
# jenis_kendaraan, pintu_masuk, pintu_keluar, pilihan, saldo_awal, biaya: integer
# daftar_pintu, opsi_saldo: array of integer
# saldo, jarak, tarif, saldo_terakhir: float
# exclude: integer or None
# pilihan: prosedur untuk menampilkan daftar pintu tol yang tersedia
# tarif_tol: fungsi untuk menghitung tarif tol berdasarkan jarak dan golongan kendaraan
# pilih_pintu_masuk: fungsi untuk memilih pintu masuk tol
# pilih_pintu_keluar: fungsi untuk memilih pintu keluar tol
# hitung_jarak: fungsi untuk menentukan jarak antara pintu masuk dan pintu keluar
# input_jenis_kendaraan: fungsi untuk memasukkan jenis kendaraan
# input_saldo: fungsi untuk memasukkan saldo e-toll
# cek_saldo: fungsi untuk mengecek apakah saldo mencukupi
# pilih_isi_saldo: prosedur untuk menampilkan opsi isi ulang saldo dan memproses input pengguna
# tampilkan_ringkasan: prosedur untuk menampilkan ringkasan transaksi
# main: prosedur utama untuk mengelola alur program

# Algoritma
# Daftar pintu tol yang tersedia
import time

# Daftar pintu tol sebagai contoh
intu = ["Cikampek", "Sadang", "Padalarang", "Cileunyi", "Pasteur"]

# Fungsi untuk menampilkan pilihan pintu tol dengan format struk
def pilihan(*pintu, exclude=None):
    print("\n===============================")
    for i, nama_pintu in enumerate(pintu, start=1):
        if exclude and i == exclude:
            continue  # Skip pilihan jika sama dengan pintu masuk
        print(f"{i}. {nama_pintu}")
    print("===============================")

# Fungsi untuk memilih pintu masuk tol
def pilih_pintu_masuk():
    print("Silakan Pilih Pintu Masuk Tol:")
    pilihan(*pintu)
    try:
        pintu_masuk = int(input("Masukkan angka pilihan: "))
        while pintu_masuk < 1 or pintu_masuk > len(pintu):
            print("Silakan input angka antara 1 sampai 5.")
            pintu_masuk = int(input("Masukkan angka pilihan: "))
        return pintu_masuk
    except ValueError:
        print("Input tidak valid. Silakan coba lagi.")
        return pilih_pintu_masuk()

# Fungsi untuk memilih pintu keluar tol
def pilih_pintu_keluar(pintu_masuk):
    print("\nSilakan Pilih Pintu Keluar Tol:")
    pilihan(*pintu, exclude=pintu_masuk)  # Tidak menampilkan pintu yang sama dengan pintu masuk
    try:
        pintu_keluar = int(input("Masukkan angka pilihan: "))
        
        # Validasi agar pintu keluar tidak sama dengan pintu masuk
        while pintu_keluar < 1 or pintu_keluar > len(pintu) or pintu_keluar == pintu_masuk:
            if pintu_keluar == pintu_masuk:
                print(f"Pilih pintu keluar tol selain pintu {pintu[pintu_masuk - 1]}.")
            else:
                print("Silakan input angka antara 1 sampai 5.")
            pintu_keluar = int(input("Masukkan angka pilihan: "))
        return pintu_keluar
    except ValueError:
        print("Input tidak valid. Silakan coba lagi.")
        return pilih_pintu_keluar(pintu_masuk)

# Contoh pemanggilan fungsi
pintu_masuk = pilih_pintu_masuk()
pintu_keluar = pilih_pintu_keluar(pintu_masuk)

print(f"\nAnda memilih Pintu Masuk: {pintu[pintu_masuk - 1]} dan Pintu Keluar: {pintu[pintu_keluar - 1]}")
# Contoh pemanggilan fungsi
pintu_masuk = pilih_pintu_masuk()
pintu_keluar = pilih_pintu_keluar(pintu_masuk)

print(f"\nAnda memilih Pintu Masuk: {pintu[pintu_masuk - 1]} dan Pintu Keluar: {pintu[pintu_keluar - 1]}")

# Fungsi untuk menentukan jarak antara pintu masuk dan keluar
def hitung_jarak(pintu_masuk, pintu_keluar):
    if pintu_masuk == 1:
        if pintu_keluar == 2:
            return 17.4
        elif pintu_keluar == 3:
            return 66
        elif pintu_keluar == 4:
            return 98.1
        else:
            return 75.9
    elif pintu_masuk == 2:
        if pintu_keluar == 1:
            return 41.0
        elif pintu_keluar == 3:
            return 65.6
        elif pintu_keluar == 4:
            return 65.6
        else:
            return 17.5
    elif pintu_masuk == 3:
        if pintu_keluar == 1:
            return 87.8
        elif pintu_keluar == 2:
            return 50.3
        elif pintu_keluar == 4:
            return 21.7
        else:
            return 17.5
    elif pintu_masuk == 4:
        if pintu_keluar == 1:
            return 121.4
        elif pintu_keluar == 2:
            return 87.2
        elif pintu_keluar == 3:
            return 20.1
        else:
            return 39.2
    else:
        if pintu_keluar == 1:
            return 97.1
        elif pintu_keluar == 2:
            return 62.8
        elif pintu_keluar == 3:
            return 18.0
        else: 
            return 39.2

# Fungsi untuk input jenis kendaraan
def input_jenis_kendaraan():
    print("\n--- Daftar Golongan Kendaraan ---")
    print("Golongan I   : Sedan, Jip, Pick Up/Truk Kecil, dan Bus")
    print("Golongan II  : Truk dengan 2 (dua) gandar")
    print("Golongan III : Truk dengan 3 (tiga) gandar")
    print("Golongan IV  : Truk dengan 4 (empat) gandar")
    print("Golongan V   : Truk dengan 5 (lima) gandar")
    while True:  # Loop untuk memastikan input valid
        try:
            jenis = int(input("Masukkan jenis kendaraan Anda (1/2/3/4/5): "))
            if 1 <= jenis <= 5:
                return jenis
            else:
                print("Golongan kendaraan harus antara 1 dan 5. Silakan pilih ulang.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka yang sesuai daftar.")



# Fungsi untuk input saldo
def input_saldo():
    try:
        saldo = int(input("Silahkan input saldo e-toll Anda: "))
        if saldo >= 0:
            return saldo
        else:
            print("Input tidak valid. Saldo harus berupa angka positif.")
            return input_saldo()
    except:
        print("Input tidak valid. Harap masukkan angka yang benar.")
        return input_saldo()

# Fungsi untuk mengecek apakah saldo dari pengguna cukup
def cek_saldo(saldo, biaya):
    return saldo >= biaya

# Fungsi untuk menampilkan opsi isi ulang saldo dan memproses input pengguna
def pilih_isi_saldo(saldo_awal, biaya):
    print("\nSaldo Anda tidak mencukupi. Pilih jumlah isi ulang:")
    opsi_saldo = [50000, 100000, 200000, 300000, 500000, 1000000, biaya - saldo_awal]
    
    for i, opsi in enumerate(opsi_saldo, 1):
        if opsi == biaya - saldo_awal:
            print(f"[{i}] Isi saldo otomatis sebesar Rp {opsi} (sesuai tarif)")
        else:
            print(f"[{i}] Rp {opsi}")
    
    try:
        pilihan = int(input("Pilih opsi isi saldo: "))
        if 1 <= pilihan <= len(opsi_saldo):
            saldo_awal += opsi_saldo[pilihan - 1]
            print(f"Isi saldo berhasil. Saldo saat ini: Rp {saldo_awal}")
            return saldo_awal
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            return pilih_isi_saldo(saldo_awal, biaya)
    except:
        print("Input tidak valid. Silakan coba lagi.")
        return pilih_isi_saldo(saldo_awal, biaya)

# Fungsi untuk menampilkan ringkasan transaksi
Contoh daftar pintu tol
pintu = ["Pintu 1", "Pintu 2", "Pintu 3", "Pintu 4"]

# Fungsi untuk menampilkan ringkasan dengan jeda antar huruf
def tampilkan_ringkasan(pintu_masuk, pintu_keluar, jenis_kendaraan, jarak, tarif, saldo_terakhir):
    teks_list = [
        f"""
    ===============================
           RINGKASAN TRANSAKSI
    ===============================
    Pintu Masuk     : {pintu[pintu_masuk - 1]}
    Pintu Keluar    : {pintu[pintu_keluar - 1]}
    Golongan Kendaraan : {jenis_kendaraan}
    Jarak Tempuh    : {jarak} km
    -------------------------------
    Tarif Tol       : Rp {tarif}
    Sisa Saldo      : Rp {saldo_terakhir}
    ===============================
    Terima kasih atas kunjungan Anda
    Selamat melanjutkan perjalanan!
    ===============================
    """
    ]

    for teks in teks_list:
        for huruf in teks:
            print(huruf, end='', flush=True)
            time.sleep(0.05)  # Jeda 0,05 detik antar huruf
        print()  # Pindah ke baris berikutnya setelah satu kalimat selesai
        
# Fungsi utama
def main():
    print("=== Selamat datang di Gerbang Pintu Tol ===")
    
    # Memilih pintu masuk tol
    pintu_masuk = pilih_pintu_masuk()
    
    # Memilih pintu keluar tol
    pintu_keluar = pilih_pintu_keluar(pintu_masuk)
    
    # Meminta input jenis kendaraan 
    jenis_kendaraan = input_jenis_kendaraan()
    
    # Menghitung jarak antara pintu masuk dan keluar
    jarak = hitung_jarak(pintu_masuk, pintu_keluar)
    
    # Menghitung tarif berdasarkan jarak dan golongan kendaraan pengguna
    tarif = tarif_tol(jarak, jenis_kendaraan)
    
    # Input saldo e-toll pengguna
    saldo = input_saldo()
    
    # Cek saldo, jika saldo kurang, maka akan langsung ditawarkan opsi untuk isi ulang saldo
    if not cek_saldo(saldo, tarif):
        saldo = pilih_isi_saldo(saldo, tarif)
    
    # Menampilkan ringkasan transaksi dengan sisa saldo pengguna
    tampilkan_ringkasan(pintu_masuk, pintu_keluar, jenis_kendaraan, jarak, tarif, saldo - tarif)

# Untuk menjalankan program
if __name__ == "__main__":
    main()
