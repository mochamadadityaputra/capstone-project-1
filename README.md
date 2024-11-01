# CRUD Program: List Data Gudang (Retail Clothing) 
Additional Portofolio Capstone Project Modul 1 Purwadhika Job Connector Data Science Online Batch 15 (JCDSOL-015):
- Mochamad Aditya Putra
- Link Drive untuk penjelasan code:
- https://drive.google.com/file/d/1z318UUGnm0g1b7colMBPpSx_F_lKK-t2/view?usp=sharing

# Data Description

Data berisi field berikut:

| Field                   | Description                      |
|-------------------------|----------------------------------|
| `kode`                  | Kode unik untuk item tersebut    |
| `nama barang`           | Nama dari item tersebut          |
| `stok barang`           | Jumlah stok barang               |
| `harga jual satuan`     | Harga jual per satuan            |
| `harga produksi satuan` | Biaya produksi per unit          |

## Data Dummy
-Berikut Data Dummy:
                                                           List Data Gudang Retail Clothing

| `kode`                 | `nama barang`                    | `stok barang`           | `harga jual satuan`              | `harga produksi satuan`                 |
|------------------------|----------------------------------|-------------------------|----------------------------------|-----------------------------------------|
| 1                      | Long Sleeve Shirt                |    700                  |     Rp 399.000                   |   Rp 150.000                            |
| 2                      | Linen Shirt                      |    100                  |     Rp 599.000                   |   Rp 400.000                            |
| 3                      | Smart Angkle Pants               |    500                  |     Rp 499.000                   |   Rp 200.000                            |
| 4                      | Cargo Pants                      |    300                  |     Rp 699.000                   |   Rp 450.000                            |



# Main Menu
Pada main menu user akan menginput nomor pada menu untuk menjalankan fungsi yang terdapat pada menu. Setiap Menu memanggil fungsi yang sesuai untuk operasi yang diinginkan. Kode ini akan terus berjalan dalam loop sampai user memilih opsi untuk keluar atau exit (6). 
## Sub Menu 1: Read
Sub-menu ini akan menampilkan List Data Gudang Retail Clothing. Fungsi `read_data(data_base)` menggunakan tabulate library untuk menampilkan data barang dalam format tabel yang rapi.
## Sub Menu 2: Create
Sub-menu ini akan menambahkan data dalam List Data Gudang Retail Clothing. Fungsi `create_data(data_base)` memungkinkan user untuk menambah data barang baru ke `data_base` dengan input dari user. Lalu untuk memastikan input yang dimasukkan oleh user valid, kita memiliki beberapa fungsi validasi seperti `num(prompt)` untuk input angka, `stri(prompt)` untuk input huruf, `code(prompt)` untuk memastikan input kode adalah numerik atau akan otomatis mengisi kode dengan kode terakhir dalam daftar, serta `fortmat_rupiah(prompt)` untuk memformat angka ke dalam mata uang Rupiah.
## Sub Menu 3: Update
Sub-menu ini akan memperbaharui data dalam List Data Gudang Retail Clothing. Fungsi `update_data(data_base)` memungkinkan user untuk memperbarui data barang yang sudah ada berdasarkan input dari user. Pada fungsi ini user tidak harus menginput baris yang ingin diperbaharui berdasarkan index, cukup input nomor baris yang sesuai pada table. Lalu setelah itu pilih antara `kode` , `nama barang` , `stok barang` , `harga jual satuan` , atau `harga produksi satuan` yang ingin diperbaharui, dan untuk memastikan input yang dimasukkan oleh user valid, kita memiliki beberapa fungsi validasi seperti `num(prompt)` untuk input angka, `stri(prompt)` untuk input huruf, `code(prompt)` untuk memastikan input kode adalah numerik atau akan otomatis mengisi kode dengan kode terakhir dalam daftar, serta `fortmat_rupiah(prompt)` untuk memformat angka ke dalam mata uang Rupiah.
## Sub Menu 4: Delete
Sub-menu ini akan menghapus data dalam List Data Gudang Retail Clothing. Fungsi `delete_data(data_base)` memungkinkan user untuk Menampilkan data yang ada, Meminta pengguna memilih kode untuk dihapus, dan menghapus baris dari kode yang dipilih dari `data_base`.
## Sub Menu 5: Sort
Sub-menu ini akan mengurutkan data dalam List Data Gudang Retail Clothing. Fungsi `sort_data(data_base)` akan memninta user memasukkan data yang akan diurutkan berdasarkan Descending atau Ascending. Dan juga akan divalidasi dengan fungsi `custom_sort(item)` dan Mengurutkan `data_base` menggunakan fungsi sorted dan menampilkan hasilnya.
## Sub Menu 6: Filter
Sub-menu ini akan memfilter data dalam List Data Gudang Retail Clothing. Fungsi `filter_data(data_base)` akan memninta user memasukkan data yang akan difilter berdasarkan kode/nama barang/stok barang/harga jual satuan/harga produksi satuan.
## Sub Menu 7: Take Things
Sub-menu ini akan mengurangi jumlah stok barang dalam List Data Gudang Retail Clothing. Fungsi `ambil_barang(data_base)` akan memninta user memasukkan data yang akan dikurangi berdasarkan kode atau nama barang.
## Sub Menu 8: Quit
Sub-menu ini akan membuat keluar dari program Data list Gudang Retail Clothing.

# Validasi Input
input dari user juga akan divalidasi menggunakan beberapa fungsi dibawah ini:
## Validasi input numeric function
Fungsi ini memvalidasi input user untuk memastikan input tersebut adalah angka. Fungsi ini diberi nama `num(prompt)`. Untuk stok barang nilai yang diinput tidak boleh 0.
## Validasi input string function
Fungsi ini memvalidasi input user untuk memastikan input tersebut adalah string yang hanya terdiri dari huruf dan special characters/symbols. Fungsi ini diberi nama `stri(prompt)`.
## Validasi input code function
Fungsi ini memvalidasi input pengguna untuk memastikan input tersebut adalah kode numerik atau kosong. Fungsi ini diberi nama `code(prompt)`. Dan untuk kode yang diinput tidak boleh 0.
## Validasi format rupiah function
Fungsi ini memformat input angka menjadi format mata uang Rupiah. Fungsi ini diberi nama `fortmat_rupiah(prompt)`.
## Custom sort function
Fungsi ini digunakan sebagai kunci pengurutan dalam fungsi `sorted`. Fungsi ini akan mengembalikan nilai dari kolom yang ditentukan oleh `sort_by` untuk setiap item dalam `data_base`. Fungsi ini diberi nama `custom_sort(item)`.


