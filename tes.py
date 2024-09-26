def hitung_luas(panjang, lebar):
    return panjang * lebar

def main():
    # Meminta input dari pengguna
    panjang = float(input("Masukkan Panjang Ruangan: "))
    lebar = float(input("Masukkan Lebar Ruangan: "))
    
    satuan = input("Masukkan Satuan (Meter/Inci): ").strip().capitalize()
    
    # Validasi satuan
    if satuan not in ['Meter', 'Inci']:
        print("Satuan tidak valid. Silakan masukkan 'Meter' atau 'Inci'.")
        return
    
    # Menghitung luas
    luas = hitung_luas(panjang, lebar)
    
    # Menampilkan hasil
    print(f"Luas ruangan dengan panjang {panjang} dan lebar {lebar} adalah {luas} {satuan}")

if __name__ == "__main__":
    main()





