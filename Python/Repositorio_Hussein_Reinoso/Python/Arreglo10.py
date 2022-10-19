from curses.ascii import isdigit
def menu():  
    print('1.- Encontrar el valor mas grande del arreglo')
    print('2.- Encontrar la cantidad de numeros pares: ')
    print('3.- Encontrar la cantidad de numeros primos')
    print('4.- Calcular el promedio')
    op = input('Elige una opcion: \n')
    if (validarnumeros(op)):
        o = int(op)
        if o>=1 and o<=4:
            if 0==1:
                mayor()
            if o==2:
                pares()
            if o==3:
                primos()
            if o==4:
                promedio() 
                return op
            
def mayor():
    p=0
    ma=0
    for x in ar:
        p=x
        if p>=ma:
        ma = p
    

def pares():
    pa = 0
    for x in ar:
        p=x%2
        if p ==0:
            pa+=1
    print(f"El numero par es: {pa}")
    

def primos():
    conp = 0
    cp = 0
    for y in ar:
        cp = 0
        for x in range(1,y):
            if (y%x)==0:
                cp +=1
        if cp == 2:
            conp+=1
    print(f"Los primos son {conp}")
            
                
def promedio():
    suma = 0
    for x in ar:
        suma +=x
    prom = suma/5
    print(f"El promedio es {prom}")    

def validarnumeros(ar):
    for x in ar:
        if isdigit(x):
            c +=1
    if c == len(ar):
        return True
    else:
        return False
        
             
ar = []     
b = 0
con = 0
while(con<10):  
  a = input("Escribe un numero: ")
  if (validarnumeros(a)):
      print("Solo son numeros",con)
      b = int[a]
      ar.append(b)
      con += 1
  else:
      print("No son numeros")

menu()
promedio()
primos()
pares()
mayor()
'''
1.-Encontrar el valor mas grande del arreglo
2.-Encontrar la cantidad de numeros pares
3.-Encontrar la cantidad de numeros primos
4.-Calcular el promedio
'''