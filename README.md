# Program sederhana data nilai mahasiswa menggunakan fungsi

**Kode Python**

![Screenshot_7](https://github.com/user-attachments/assets/71a18110-c0f1-4153-bf1f-b31cefb5ff09)
![Screenshot_8](https://github.com/user-attachments/assets/6d198343-6eb1-4f45-be47-cd268933e266)

**Input dan Output**

![Screenshot_9](https://github.com/user-attachments/assets/3b632a71-2e54-4dce-b8cb-d090811fec80)
![Screenshot_10](https://github.com/user-attachments/assets/68a9dfc2-89c8-42ed-aed1-7c76a246ffcb)
![Screenshot_11](https://github.com/user-attachments/assets/da5d44bc-008e-417f-b75c-06c9911cd367)

**Penjelasan**

1. Data Mahasiswa

Penjelasan:

Variabel data_mahasiswa adalah sebuah list kosong yang akan digunakan untuk menyimpan data mahasiswa dalam bentuk dictionary, di mana setiap dictionary berisi nama dan nilai.

2. Fungsi tambah(nama, nilai)

Fungsi: Menambahkan data mahasiswa ke dalam list data_mahasiswa.

Parameter:
	- nama: Nama mahasiswa yang akan ditambahkan.
	- nilai: Nilai mahasiswa yang akan ditambahkan.

Proses:

Data baru ditambahkan ke dalam list dalam bentuk dictionary { "nama": nama, "nilai": nilai }.

3. Fungsi tampilkan()

Fungsi: Menampilkan semua data mahasiswa yang tersimpan di dalam list.

Proses:
Memeriksa apakah data_mahasiswa kosong.
Jika kosong, menampilkan pesan "Belum ada data mahasiswa".
Jika ada data, melakukan iterasi dengan enumerate untuk menampilkan nomor, nama, dan nilai mahasiswa.

4. Fungsi hapus(nama)

Fungsi: Menghapus data mahasiswa berdasarkan nama.

Parameter:
nama: Nama mahasiswa yang akan dihapus.

Proses:

Mencari mahasiswa dalam data_mahasiswa dengan nama yang sesuai.
Jika ditemukan, data dihapus dengan remove().
Jika tidak ditemukan, menampilkan pesan bahwa data tidak ada.

5. Fungsi ubah(nama, nilai_baru)

Fungsi: Mengubah nilai mahasiswa berdasarkan nama.

Parameter:
	- nama: Nama mahasiswa yang datanya akan diubah.
	- nilai_baru: Nilai baru yang akan disimpan.

Proses:
Mencari mahasiswa dengan nama yang sesuai.
Jika ditemukan, nilai mahasiswa diubah.
Jika tidak ditemukan, menampilkan pesan bahwa data tidak ada.

6. Menu Utama (menu())

Fungsi: Menampilkan menu utama program dan menangani input pengguna.

Proses:
Menampilkan daftar menu:
1. Tambah Data
2. Tampilkan Data
3. Hapus Data
4. Ubah Data
5. Keluar
Meminta input pengguna untuk memilih opsi.
Menjalankan fungsi yang sesuai berdasarkan pilihan pengguna.
Jika pilihan adalah 5, program berhenti dengan perintah break.
