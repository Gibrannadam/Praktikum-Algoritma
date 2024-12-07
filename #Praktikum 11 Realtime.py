#Praktikum 11 Realtime

kelas Mahasiswa:
    def __init__(self, nama, nim, angkatan):
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan

    def tampilkan_biodata(self):
        print("\n=== Biodata Mahasiswa ===")
        print(f"Nama       : {self.nama}")
        print(f"NIM        : {self.nim}")
        print(f"Angkatan   : {self.angkatan}")

# Program utama
print("Input Biodata Mahasiswa")
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
angkatan = input("Masukkan Angkatan: ")

# Membuat objek dari kelas Mahasiswa
mahasiswa = Mahasiswa(nama, nim, angkatan)

# Menampilkan biodata mahasiswa
mahasiswa.tampilkan_biodata()
