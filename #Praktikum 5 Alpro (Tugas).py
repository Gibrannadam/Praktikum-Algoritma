#Praktikum 5 Alpro

def hitung_tiket():
    total_harga = 0

    print("Masukkan umur untuk setiap pengunjung. Ketik 'selesai' jika sudah selesai memasukkan data.\n")

    while True:
        umur_input = input("Masukkan umur pengunjung: ")

        # Memeriksa apakah input adalah perintah 'selesai'
        if umur_input.lower() == 'selesai':
            break

        try:
            umur = int(umur_input)

            # Menentukan harga tiket berdasarkan umur
            if umur <= 2:
                harga = 0
            elif 3 <= umur <= 12:
                harga = 14
            elif umur >= 65:
                harga = 18
            else:
                harga = 23

            total_harga += harga
            print(f"Harga tiket untuk umur {umur} tahun adalah ${harga}\n")

        except ValueError:
            print("Umur tidak valid. Harap masukkan angka yang benar.\n")

    print(f"Total harga tiket untuk semua pengunjung adalah ${total_harga}")

    # Memasukkan pembayaran
    try:
        pembayaran = float(input("Masukkan jumlah uang yang dibayarkan: $"))

        if pembayaran < total_harga:
            print("Uang tidak cukup. Harap bayar dengan jumlah yang sesuai.")
        else:
            kembalian = pembayaran - total_harga
            print(f"Kembalian Anda: ${kembalian:.2f}")

    except ValueError:
        print("Jumlah uang tidak valid. Harap masukkan angka yang benar.")

# Memanggil fungsi untuk menjalankan program
hitung_tiket()
