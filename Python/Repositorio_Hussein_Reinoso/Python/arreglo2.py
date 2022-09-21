'''
Hacer un programa que muestre el siguiente menu
1.-Llenar
2.-Pila
3.-Cola
4.-Salir
El programa pedira una opcion del menu con las siguientes restricciones
1.-Si el arreglo esta vacio no se puede elegir ni la opcion 1 ni la opcion 2
2.-Una vez llenado el arreglo no se puede elegir la opcion 1
3.-El programa no termina hasta que el usuario lo desee
'''

from asyncio import sleep

def menu():
    print("1.-Llenar\n")
    print("2.-Pila\n")
    print("3.-Cola\n")
    print("4.- Salir\n")
    op = input("Escoje una opcion a realiza: ")
    if op == "1":
        llenar(x)
    if op == "2":
        pila()
    if op == "3":
        cola()
    if op == "4":
        salir()
        
def salir():
    quit()

def llenar(x):
    a = int(input('Escirbe un numero: '))
    arr.append(a)
    x += 1
    if x < 10:
        llenar(x)       


def pila():
    aux = len(arr) -1
    for x in range(0,len(arr)):
        sleep(3)
        arr.pop(aux)
        aux -=1
        print("Cola")
        print(arr)

def cola():
    for x in range(0,len(arr)):
        print("x: ",x," ",len(arr))
        sleep(2)
        arr.pop(0)
        print('Cola')
        print(arr)
    
  
x = 0
arr = []
menu()
llenar(x)
pila()
cola()
salir()
