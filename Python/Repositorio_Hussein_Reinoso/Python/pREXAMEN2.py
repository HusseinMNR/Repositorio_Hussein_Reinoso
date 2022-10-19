'''
Hacer un programa que llene dos arreglos exclusivamente con números pero con un solo digito, el programa mostrara
por fila cuales son los trios pitagoricos
'''
from turtle import onkeypress


def validar(a,b,c):
    if a>=0 and a<=9 and b>=0 and b<=9 and c>=0 and c<=9:
        return True
    else:
        return False
        
def llenar():
    a = int(input("Escribe un numero: "))
    b = int(input("Escribe un numero: "))
    c = int(input("Escribe un numero: "))
    if validar(a,b,c):
        arr.append(int(a))
        arr1.append(int(b))
        arr2.append(int(c))
        print(arr," ",arr1,"",arr2)
    else:
        print("El valor es incorrecto")
    print(arr," ",arr1,"",arr2)
        
def comprobar():
    for x in range (0,len(arr)):
        a=0
        b=0
        c=0
        res=0
        a=arr[x]*2
        b=arr1[x]*2
        c=arr2[x]*2
        res=a+b
        if (res==c):
            print("La fila ",x,"es un trio pitagorico")
            print(arr," ",arr1," ",arr2)
        else:
            print("No es un trio pitagorico")
            print(arr," ",arr1," ",arr2)
            
arr = []
arr1 = []
arr2 = []
numero1 = []
numero2 = []
numero3 = []
d ="s"
while d=='si' or d=='s':
    llenar()
    d = input("¿Quieres ingresar mas numeros?")
comprobar()