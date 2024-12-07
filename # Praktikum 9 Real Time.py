# Praktikum 9 Real Time

def tulis_biodata(): 
 
    with open("Biodata.txt", "w") as file: 
 
        nama = input("Nama: ") 
        umur = input("Umur: ") 
        alamat = input("Alamat: ") 
        email = input("Email: ") 
        dosen_wali = input("Dosen Wali: ") 
 
        file.write("Nama: " + nama + "\n") 
        file.write("Umur: " + umur + "\n") 
        file.write("Alamat: " + alamat + "\n") 
        file.write("Email: " + email + "\n") 
        file.write("Dosen Wali: " + dosen_wali + "\n") 
 
    print("Biodata telah berhasil disimpan dalam Biodata.txt") 
 
def baca_biodata(): 
    try: 
 
        with open("Biodata.txt", "r") as file: 
 
            print("\nBerikut ini data kamu:") 
            print(file.read()) 
    except FileNotFoundError: 
        print("File Biodata.txt tidak ditemukan. Pastikan file sudah ada.") 
 
tulis_biodata()  
baca_biodata()  