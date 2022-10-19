'''
1.-Hacer  un programa que llene una matriz de 3x3, exclusivamente con letras con longitud 1, el espacio,.,','.
El programa contabilisara cuantas letras mayusculas,minusculas y vocales tiene la matriz.
El programa no termina hasta que el usuario lo desie.
'''
from itertools import count


a=[[0,0,0],
   [0,0,0],
   [0,0,0]
   ]

def ValidarLetras():
    c=input("Escribe una letra: ")
    if c.isalpha() and len(c)==1 or c==',' or c==' ' or c=='.':
        #if len(c)==1:
            return c
        #else:
            print("Error")
            return ValidarLetras()
    else:
        print("Error")
        return ValidarLetras()
    
    
def llenarArreglo():
    for x in range(3):
        for y in range(3):
            a[x][y]=str(ValidarLetras())
            print(a)

def contarSignos():
    a.count('.')
    #print(a.count('.'))
    

ValidarLetras()
llenarArreglo()
contarSignos()
            