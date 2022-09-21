from asyncio import sleep


def llenar(x):
    a = int(input('Escirbe un numero: '))
    arr.append(a)
    x += 1
    if x < 10:
        llenar(x)
    
def mostrar():
    for x in range(0,len(arr)):
        print(x," ",arr[x],"\n")


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
        
        

def  liberarArreglo():
    valor = int(input("Escribe el valor a eliminar: "))
    if valor>=0 and valor<len(arr):
        arr.pop(valor)
    else:
        print("Posicion incorrecta")
        
x = 0
arr = []
res = "si"
llenar(x)
mostrar()
pila()

'''while(res=="si"):
    liberarArreglo()
    mostrar()
    res = input('Deseas otra ejecucion si/no : ')'''
