from asyncio import sleep


a=[[0,0,0],
   [0,0,0],
   [0,0,0]]
res=[[0,0,0],
     [0,0,0],
     [0,0,0]]

for x in range(3):
    for y in range(3):
        b = int(input("Escribe un numero: "))
        a[x][y]=b
c=int(input("Escribe un escalar: "))
for x in range(3):
    for y in range(3):
        res[x][y]=a[x][y]*c

for x in range(3):
    for y in range(3):
        print(res[x][y])
        sleep(1)   
    print()     
        
for x in range(3):
    for y in range(3):
        print(res[x][y],end='')
    print()
    
'''for m in a:
    print(m)
    sleep(1)'''

"Investigar el algoritmo en python para la multiplicacion de matrices"


