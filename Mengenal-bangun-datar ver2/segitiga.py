#module segitiga
from math import sqrt
def segitiga(a, b, c):
    x = c > a and c > b
    y = a > c and a > b
    z = b > a and b > c

    if x == True:
        rumus = a**2 + b**2
        hipo = c
    else:
        if y == True:
            rumus = c**2 + b**2
            hipo = a
        elif z == True:
            rumus = a**2 + c**2
            hipo = b

    if rumus == hipo**2:
        jenis = "siku siku"
    else:
        if rumus > hipo**2:
            jenis = "lancip"
        elif rumus < hipo**2:
            jenis = "tumpul"

    keliling = a + b + c
    s = keliling / 2
    Luas = sqrt(s * (s - a) * (s - b) * (s - c))

    print("hipotenusa(sisi terpanjang)=", hipo, "cm")
    print("keliling=", keliling, "cm")
    print("luas=", Luas, "cm2")
    print("jenis segitiga=", jenis)

