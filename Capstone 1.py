import tabulate
import re

data_base = [
    {"kode": 1, "nama barang": "Long Sleeve Shirt", "stok barang": 700, "harga jual satuan": "Rp 399.000", "harga produksi satuan": "Rp 150.000"},
    {"kode": 2, "nama barang": "Linen Shirt", "stok barang": 100, "harga jual satuan": "Rp 599.000", "harga produksi satuan": "Rp 400.000"},
    {"kode": 3, "nama barang": "Smart Angkle Pants", "stok barang": 500, "harga jual satuan": "Rp 499.000", "harga produksi satuan": "Rp 200.000"},
    {"kode": 4, "nama barang": "Cargo Pants", "stok barang": 300, "harga jual satuan": "Rp 699.000", "harga produksi satuan": "Rp 450.000"}
]

# Read data
def read_data(data_base):  # data_base disini sebagai input
    print(tabulate.tabulate(data_base, headers="keys", tablefmt="pretty"))

# Validate numeric input
def num(prompt):  
       while True:
           value = input(prompt)
           if value.isdigit():
               if int(value) == 0:  # Tambahkan validasi stok
                   print("Stok barang tidak boleh 0, silakan input lagi.")
               else:
                   return int(value)
           else:
               print("Input yang anda masukkan bukan nomor, silakan input lagi.")

# Validate string input
def stri(prompt):  
    while True:
        value = input(prompt)
        # Izinkan huruf, spasi, tanda hubung, dan tanda kutip
        if re.match(r"^[a-zA-Z0-9\s\"-]+$", value):  
            return value.title()
        else:
            print("Input yang anda masukkan mengandung karakter yang tidak diizinkan, silakan input lagi.")

#Validate Code input
def code(prompt):  
    while True:
        value = input(prompt)
        if value.isdigit():
            if int(value) == 0:
                print("Kode tidak boleh 0, silakan masukkan kode lain.")
            # Cek duplikat kode
            elif any(item["kode"] == int(value) for item in data_base):
                print("Kode sudah ada, silakan masukkan kode lain.")
            else:
                return int(value)
        elif value == "":
            return None
        else:
            print("Input yang anda masukkan bukan kode nomor, silakan input lagi.")

# Format number to Rupiah currency
def format_rupiah(prompt): # input berupa prompt
    while True:
        value = input(prompt)
        if value.isdigit():
            value = int(value)
            return f"Rp {value:,.0f}".replace(',', '.')
            #,: Menambahkan koma sebagai pemisah seribu.
            # .0f: Memastikan tidak ada tempat desimal.
        else:
            print("Input bukan angka, silakan masukkan angka.")

# Create data
def create_data(data_base):  # input berupa data_base
    kode = code("Masukkan kode (biarkan kosong untuk kode otomatis): ")
    if kode is None:
        if data_base:
            kode = max(item["kode"] for item in data_base) + 1
        else:
            kode = 1
    nama_barang = stri("Masukkan nama barang: ")
    # Validasi nama barang (cek duplikat)
    while any(item["nama barang"].lower() == nama_barang.lower() for item in data_base):
        print("Nama barang sudah ada, silakan masukkan nama lain.")
        nama_barang = stri("Masukkan nama barang: ")  # Minta input lagi

    stok_barang = num("Masukkan stok barang: ")
    harga_jual_satuan = format_rupiah("Masukkan harga jual satuan: ")
    harga_produksi_satuan = format_rupiah("Masukkan harga produksi satuan: ")
    new_data = {
        "kode": kode,
        "nama barang": nama_barang,
        "stok barang": stok_barang,
        "harga jual satuan": harga_jual_satuan,
        "harga produksi satuan": harga_produksi_satuan
    }
    data_base.append(new_data)
    print("Data berhasil ditambahkan!")

# Update data
def update_data(data_base):  # data_base disini sebagai input
    read_data(data_base)
    while True:
        row = num("Masukkan nomor baris data yang ingin diupdate (dimulai dari 1): ") - 1
        # Pengguna memasukkan indeks berbasis 1, sehingga fungsinya mengurangi 1 untuk mengubahnya menjadi indeks berbasis 0.
        if 0 <= row < len(data_base):
            break
        else:
            print("Nomor baris tidak valid.")

    while True:
        column = input(
            "Masukkan kolom yang ingin diupdate pilih salah satu (kode/nama barang/stok barang/harga jual satuan/harga produksi satuan): ").lower()
        if column in data_base[row].keys():
            if column == "kode":
                data_base[row][column] = code(f"Masukkan {column} baru: ")
            elif column == "nama barang":
                data_base[row][column] = stri(f"Masukkan {column} baru: ")
            elif column == "stok barang":
                data_base[row][column] = num(f"Masukkan {column} baru: ")
            elif column == "harga jual satuan":
                data_base[row][column] = format_rupiah(f"Masukkan {column} baru: ")
            elif column == "harga produksi satuan":
                data_base[row][column] = format_rupiah(f"Masukkan {column} baru: ")
            print("Data berhasil diupdate!")
            break
        else:
            print("Kolom tidak ditemukan.")

# Delete item by kode
def delete_data(data_base):
    read_data(data_base)
    kode = num("Masukkan kode barang yang ingin dihapus: ")
    for i, item in enumerate(data_base):
        if item['kode'] == kode:
            del data_base[i]
            print("Barang berhasil dihapus.")
            return
    print("Barang dengan kode tersebut tidak ditemukan.")

# Custom sort function
def custom_sort(item):
    return item[sort_by]
    # Fungsi custom_sort digunakan sebagai kunci pengurutan dalam fungsi sorted.
    # Fungsi ini mengembalikan nilai dari kolom yang ditentukan oleh sort_by untuk setiap item dalam data_base.

# Sort data
def sort_data(data_base): # data_base disini sebagai input
    global sort_by
    sort_by = input("Sorting berdasarkan (kode/nama barang/stok barang/harga jual satuan/harga produksi satuan): ").lower()
    if sort_by in data_base[0]:
        order = input("Urutkan secara ascending atau descending? (a/d): ").lower()
        reverse_order = True if order == "d" else False
        # Baris diatas menyetel variabel reverse_order ke True jika pengguna memilih urutan descending (d), dan False jika tidak (untuk urutan ascending).
        sorted_data = sorted(data_base, key=custom_sort, reverse=reverse_order)
        #Mengurutkan data_base menggunakan fungsi sorted. Key adalah fungsi custom_sort, dan urutan pengurutan ditentukan oleh reverse_order.
        # Fungsi custom_sort menggunakan nilai sort_by untuk menentukan kunci pengurutan.
        read_data(sorted_data)
    else:
        print("Kolom tidak ditemukan.")

# Filter data
def filter_data(data_base):
    while True:
        read_data(data_base)
        filter_by = input("Filter berdasarkan (kode/nama barang/stok barang/harga jual satuan/harga produksi satuan): ").lower()
        
        if filter_by in data_base[0]:
            filter_value = input(f"Masukkan nilai filter untuk {filter_by}: ")
            
            if filter_by == "nama barang":
                # Filter nama barang yang mengandung kata yang sama
                filtered_data = [item for item in data_base if filter_value.lower() in item[filter_by].lower()]
            else:
                # Filter data berdasarkan kolom lainnya
                filtered_data = [item for item in data_base if str(item[filter_by]).lower() == filter_value.lower()]
                
            if filtered_data:
                read_data(filtered_data)
                break  # Keluar dari loop jika data ditemukan
            else:
                print("Data tidak ditemukan. Silakan input ulang.") 
        else:
            print("Kolom tidak ditemukan. Silakan input ulang.")

# Take Things
def ambil_barang(data_base):
    read_data(data_base)
    while True:
        cari_berdasarkan = input("Cari barang berdasarkan (kode/nama barang): ").lower()  # Batasi pilihan di sini
        
        if cari_berdasarkan in ("kode", "nama barang"):  # Periksa pilihan yang valid
            cari_nilai = input(f"Masukkan nilai {cari_berdasarkan}: ")

            # Cari barang berdasarkan kriteria
            barang = next((item for item in data_base if str(item[cari_berdasarkan]).lower() == cari_nilai.lower()), None)
            
            if barang:
                while True:
                    jumlah_ambil = num(f"Masukkan jumlah {barang['nama barang']} yang ingin diambil: ")
                    
                    if jumlah_ambil <= barang["stok barang"]:
                        barang["stok barang"] -= jumlah_ambil
                        print(f"Stok {barang['nama barang']} berhasil dikurangi. Stok sekarang: {barang['stok barang']}")
                        break  
                    else:
                        print(f"Jumlah pengambilan melebihi stok. Stok {barang['nama barang']}: {barang['stok barang']}")
                break  
            else:
                print("Barang tidak ditemukan.")
        else:
            print("Kriteria pencarian tidak valid.")

# Main menu
def main():
    while True:
        print("""
        List Data Gudang Retail Clothing 
        Menu:
        1. Read Data
        2. Create Data
        3. Update Data
        4. Delete Data
        5. Sort Data
        6. Filter Data
        7. Take Things from Data
        8. Exit
        """)

        menu = input("Masukkan menu: ")
        if menu == "1":
            read_data(data_base)
        elif menu == "2":
            create_data(data_base)
        elif menu == "3":
            update_data(data_base)
        elif menu == "4":
            delete_data(data_base)
        elif menu == "5":
            sort_data(data_base)
        elif menu == "6":
            filter_data(data_base)
        elif menu == "7":
            ambil_barang(data_base)
        elif menu == "8":
            break
        else:
            print("Kode menu tidak ditemukan.")

main()