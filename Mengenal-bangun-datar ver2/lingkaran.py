#module lingkaran
from math import pi
def lingkaran(r):
    luas = (r * r) * pi
    kel = 2 * pi * r
    print("Kelling : ", float(kel), "cm")
    print("Luas : ", float(luas), "cm persegi")
    print("catatan ! menggunakan pi : ", pi)
