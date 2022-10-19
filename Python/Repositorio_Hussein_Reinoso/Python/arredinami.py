from asyncio import sleep
from curses.ascii import isalpha, isdigit
from os import O_SEQUENTIAL


def validarNumero(a):
    #print('Numeros')
    if a.isdigit():
        return True
    else:
        return False
    
def validarletras(a):
    #print('letras')
    c=0
    for x in a:
        if isalpha(x) or x=='':
            c+=1
    if c==len(a):
        return True
    else:
        return False
        

def validareales(a):
    #print('Numeros con decimales')
    c = 0
    cp = 0
    for x in a:
        print(x)
        if x =='.':
            cp+=1
        elif isdigit(x):
            c+=1
    if cp ==1:       
        if c+cp == len(a):
             return True
        else:
             return False
    else:
        return False
    
    
    
    

def llenar():
    a = input("Escribe un valor por dato: ")
    if validarNumero(a):
        numeros.append(int(a))
        print(numeros)
    elif(validarletras(a)):
        letras.append(a)
    elif(validareales(a)):
        flotantes.append(float(a))
    res = input('Desea otro valor: ')
    if (res=='s' or res=='si'):
        llenar()
        
def multiplicarNL():
    if len(numeros)==len(letras):
        for x in letras:
            letras2.append(len(x))
        for x in range(0,len(numeros)):
            print(letras2[x]," * ",numeros[x]," = ",letras2[x]*numeros[x])
    else:
        print("Los arreglos no son del mismo tamaño")
        sleep(1)

def multiplicarND():
    if len(numeros)==len(flotantes):
        for x in range(0,len(numeros)):
            print(flotantes[x]," * ",numeros[x]," = ",flotantes[x]*numeros[x])
    else:
        print("Los arreglos no son del mismo tamaño")
        sleep(1)

def multiplicarLD():
    if len(letras)==len(flotantes):
        for x in letras:
            letras3.append(len(x))
        for x in range(0,len(flotantes)):
            print()
            

        
            
letras3 = []        
letras2 = []       
numeros = []
letras = []
flotantes = []
llenar()
op = 1
while(op!=4):
    print("Menu")
    print("1.-N * L")
    print("2.-N * D")
    print("3.-L * D")
    print("4.-Salir")
    o = input("Elige una opcion")
    if (validarNumero(o)):
        op = int(o)
        if op==1:
            multiplicarNL()
        if op==2:
            multiplicarND()
        if op==3:
            multiplicarLD()