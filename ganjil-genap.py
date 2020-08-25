print("""
mengecek bilangan ganjil genap
masukkan bilangan anda
lalu enter

untuk berhenti ketik "stop"
""")

while True :
  x=str(input("masukkan bilangan : "))
  if x == "stop":
      break
  a=int(x)
  def gg(a):
      if a%2 == 0:
         print(" genap")
      elif a%2 != 0:
         print(" ganjil")
     

  print(a, ":", end="")
  gg(a)
  print("\n")
  
