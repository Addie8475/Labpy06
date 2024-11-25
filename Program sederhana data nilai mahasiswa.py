# List untuk menyimpan data mahasiswa
data_mahasiswa = []

# Fungsi untuk menambah data
def tambah(nama, nilai):
    data_mahasiswa.append({"nama": nama, "nilai": nilai})
    print(f"Data untuk {nama} telah ditambahkan.")

# Fungsi untuk menampilkan semua data
def tampilkan():
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
    else:
        print("\nDaftar Nilai Mahasiswa:")
        for i, mhs in enumerate(data_mahasiswa, 1):
            print(f"{i}. Nama: {mhs['nama']}, Nilai: {mhs['nilai']}")
        print()

# Fungsi untuk menghapus data berdasarkan nama
def hapus(nama):
    global data_mahasiswa
    for mhs in data_mahasiswa:
        if mhs['nama'] == nama:
            data_mahasiswa.remove(mhs)
            print(f"Data untuk {nama} telah dihapus.")
            return
    print(f"Data untuk {nama} tidak ditemukan.")

# Fungsi untuk mengubah data berdasarkan nama
def ubah(nama, nilai_baru):
    for mhs in data_mahasiswa:
        if mhs['nama'] == nama:
            mhs['nilai'] = nilai_baru
            print(f"Data untuk {nama} telah diperbarui.")
            return
    print(f"Data untuk {nama} tidak ditemukan.")

# Menu utama
def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            nama = input("Masukkan nama: ")
            nilai = input("Masukkan nilai: ")
            tambah(nama, nilai)
        elif pilihan == "2":
            tampilkan()
        elif pilihan == "3":
            nama = input("Masukkan nama yang akan dihapus: ")
            hapus(nama)
        elif pilihan == "4":
            nama = input("Masukkan nama yang akan diubah: ")
            nilai_baru = input("Masukkan nilai baru: ")
            ubah(nama, nilai_baru)
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Menjalankan program
menu()
