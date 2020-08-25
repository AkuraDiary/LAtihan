#mengenal bangun datar(with while loop)

#ini mengimport module
import lingkaran
import persegi
import persegi_pjg
import segitiga

#ini input
while True:
    bentuk = str(input("\n masukkan nama bangun datar : "))

    #ini proses
    if bentuk == "lingkaran":
        R = int(input("Jari-jari linkaran(cm) : "))
        lingkaran.lingkaran(R)

    elif bentuk == "persegi":
        S = int(input("Sisi persegi(cm) : "))
        persegi.persegi(S)

    elif bentuk == "persegi_panjang":
        P = int(input("panjang(cm) : "))
        L = int(input("Lebar(cm) : "))
        persegi_pjg.persegi_pjg(P, L)

    elif bentuk == "segitiga":
        c = int(input("sisi a(cm) : "))
        b = int(input("sisi b(cm) : "))
        a = int(input("sisi c(cm) : "))
        segitiga.segitiga(a, b, c)

    elif bentuk == "stop":
        break

    else:
        print("error \n", "nama bangun datar tidak terdefinisi")
        print("atau")
        print("ketik 'stop' untuk berhenti")
        print("bangun datar : \n",
              "lingkaran, persegi, persegi_panjang, segitiga")
#end
