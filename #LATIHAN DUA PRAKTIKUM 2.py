#LATIHAN DUA PRAKTIKUM 2


from math import *
lintang1 = math.radians(float(input("Lintang Kota 1 = ")))
bujur1 = math.radians(float(input("Bujur Kota 1 = ")))
lintang2 = math.radians(float(input("Lintang Kota 2 = ")))
bujur2 = math.radians(float(input("Bujur Kota 2 = ")))
R = 6371

lat = lintang2-lintang1
long = bujur2-bujur1
a = math.sin(lat/2)**2 + math.cos(lintang1)*math.cos(lintang2)*math.sin(long/2)**2
c = 2*math.atan2(sqrt(a), sqrt(1-a))
d = R*c
print(d)
