# Praktikum 9 Tugas

def buat_file(nama_file):
    try:
        with open(nama_file, 'w') as file:
            file.write("")  # Membuat file kosong
        print(f"File '{nama_file}' berhasil dibuat.")
    except Exception as e:
        print(f"Terjadi kesalahan saat membuat file: {e}")

def baca_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            isi = file.read()
        print(f"Isi file '{nama_file}':\n{isi}")
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file: {e}")

def tambah_text(nama_file, teks):
    try:
        with open(nama_file, 'a') as file:
            file.write(teks + '\n')  # Menambahkan teks dengan baris baru
        print("Teks berhasil ditambahkan ke file.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menambahkan teks: {e}")

def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Membuat Dan Menulis File")
        print("2. Membaca File")
        print("3. Menambahkan Teks ke File")
        print("4. Keluar Dari Program")
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            nama_file = input("Masukkan nama file (dengan ekstensi): ")
            buat_file(nama_file)
        elif pilihan == "2":
            nama_file = input("Masukkan nama file yang ingin dibaca: ")
            baca_file(nama_file)
        elif pilihan == "3":
            nama_file = input("Masukkan nama file yang ingin ditambahkan teks: ")
            teks = input("Masukkan teks yang ingin ditambahkan: ")
            tambah_text(nama_file, teks)
        elif pilihan == "4":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

# Jalankan program
menu()
