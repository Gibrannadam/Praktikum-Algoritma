#Praktikum Alpro 3

# Fungsi untuk mencari akar persamaan kuadrat
def cari_akar(a, b, c):
    # Hitung determinan
    determinan = (b**2) - (4*a*c)
    
    print(f"Persamaan kuadrat {a}x^2 + {b}x + {c}")
    print(f"Determinan = {determinan}")

    # Jika nilai A adalah nol, itu bukan persamaan kuadrat
    if a == 0:
        print("Bukan merupakan persamaan kuadrat, karena nilai A = 0")
    else:
        # Jika determinan lebih besar dari 0, akar berbeda
        if determinan > 0:
            akar1 = (-b + (determinan)) / (2*a)
            akar2 = (-b - (determinan)) / (2*a)
            print("Memiliki Akar Berbeda")
            print(f"Akar x1 = {akar1}")
            print(f"Akar x2 = {akar2}")
        
        # Jika determinan sama dengan 0, akar kembar
        elif determinan == 0:
            akar = -b / (2*a)
            print("Merupakan Akar Kembar")
            print(f"Akar = {akar}")
        
        # Jika determinan kurang dari 0, akar imaginer
        else:
            real_part = -b / (2*a)
            imaginer_part = (-determinan) / (2*a)
            print("Merupakan Akar Imaginer")
            print(f"Akar x1 = {real_part} + {imaginer_part}i")
            print(f"Akar x2 = {real_part} - {imaginer_part}i")

# Program utama
print("=====Selamat Datang di Program Mencari Akar Persamaan Kuadrat dan Determinan=====")

# Input nilai a, b, dan c
a = float(input("Masukkan nilai A : "))
b = float(input("Masukkan nilai B : "))
c = float(input("Masukkan nilai C : "))

# Panggil fungsi untuk mencari akar
cari_akar(a, b, c)