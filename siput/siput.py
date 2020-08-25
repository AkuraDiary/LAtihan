print("Seekor siput terjatuh dalam sumur....\n")
"""
Kasus 

seekor siput terjebak di dalam sumur dengan kedalaman 30 Meter

jika
saat siang hari ia naik 3 meter,
sedangkan malam hari ia turun 2 Meter

berapa hari kah dia akan keluar dari sumur itu?

~ 1 hari = 1 siang + 1 malam

"""

"""
n= naik
t= turun
j= ketinggian
p= progres
i=hari ke...(mungkin)
"""

#input
h=int(input("kedalaman sumur(m) : "))
n=int(input("merambat naik saat siang sebanyak(m) : "))
t=int(input("terpeleset turun saat malam sebanyak(m) : "))


#proses
def progress(h, n, t):
  d=1
  i=0
  while i < h:
     p=n-t
     
     print("hari ke:", d, ", naik :", n, ", turun :", t, ",ketinggian awal:",i, ", ketinggian akhir :", i+p, "m\n"  )
     d+=1
     i+=p
     
     
     if i + n >= h :
       print("hari ke:", d, ", naik :", n, ", turun :", t, ",ketinggian awal:",i, ", ketinggian akhir:", i+n, "m\n"  )
       return d
       break

 
  
#output
print("\nprogres : ", n-t,"m/hari\n")
print("Jadi, waktu yang dibutuhkan:", progress(h, n, t), "hari") 