#Bahasa Walikan 
"""ketik stop! untuk berhenti"""

#loop
while True:
#input
 x=input(str("masukkan kata : "))

#break
 if x == "stop!":
   break

#proses
 def walik(x) :
   for i in reversed(x):
     print(i, end="")

#output
 print("hasil walikan : ", end="")
 walik(x)
 print("\n")