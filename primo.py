a=0
n=int(input("Ingrese un numero: "))
for i in range(1,n+1):
 if(n % i==0):
  a=a+1
if(a!=2):
 print("No es primo")
else:
 print("Es primo") 