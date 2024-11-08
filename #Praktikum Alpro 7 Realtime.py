#Praktikum Alpro 7 Realtime

# Fungsi untuk memeriksa apakah sebuah bilangan adalah bilangan prima
def is_prime(n):
    if n <= 1:
        return False  # Bilangan kurang dari atau sama dengan 1 bukan bilangan prima
    for i in range(2, int(n**0.5) + 1):  # Cek pembagi dari 2 hingga akar kuadrat n
        if n % i == 0:  # Jika ada pembagi selain 1 dan n, maka n bukan bilangan prima
            return False
    return True  # Jika tidak ditemukan pembagi, maka n adalah bilangan prima

# Fungsi untuk meminta input dari pengguna dan mengecek apakah bilangan tersebut prima
def check_prime():
    try:
        # Meminta input dari pengguna
        num = int(input("Masukkan sebuah bilangan: "))
        # Memanggil fungsi is_prime untuk mengecek apakah bilangan tersebut prima
        if is_prime(num):
            print(f"{num} adalah bilangan prima.")
        else:
            print(f"{num} bukan bilangan prima.")
    except ValueError:
        print("Input tidak valid! Masukkan angka yang benar.")

# Memanggil fungsi check_prime untuk menjalankan program
check_prime()