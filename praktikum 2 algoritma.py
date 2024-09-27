import math
a = float(input("Masukkan bilangan bulat a: "))
b = float(input("Masukkan bilangan bulat b: "))

# menghitung hasil perhitungan
jumlah = a + b
selisih =  b - a
kali = a + b
sisa_pembagian = a % b
pembagian = a / b
log_a = math.log10(a)
pangkat = a ** b 

#output
print (f"jumlah a dan b: {jumlah}")
print (f"selisih b-a: {selisih}")
print (f"hasil kali a * b: {kali}")
print (f"hasil jumlah sisa_pembagian: {sisa_pembagian}")
print (f"hasil jumlah pembagian: {pembagian}")
print (f"hasil dari math.log: {log_a}")
print (f"hasil jumlah pangkat: {pangkat}")

