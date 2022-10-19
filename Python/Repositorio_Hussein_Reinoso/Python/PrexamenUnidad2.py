'''
Hacer un programa que llene una matriz de 3x3 exclusivamente de numeros pares, y otra 
matriz exclusivamente de numeros impares,
el programa mostrara la multiplicacion del valor mayor y menor de las dos matrices y 
ademas guardara en un arreglo los numeros primos que existan en las dos matrices.
'''

a = [[0,0],
     [0,0]]
b = [[0,0],
     [0,0]]

def validarPares():
    p = int(input("Escribe un numero par: "))
    if p%2==0:
        return p
    else:
            print('Error')
            return validarPares()
        
def validarImpares():
    i = int(input('Escriba un numero impar: '))
    if i%2!=0:
            return i
    else:
            print('Error')
            return validarImpares()
    
def llenarPares():
    for x in range(2):
        for y in range(2):
            a[x][y]=int(validarPares())
            
def llenarImpares():
    for w in range(2):
        for z in range(2):
            b[w][z]=int(validarImpares())

def mayorPar():
    mayPar = 0
    for x in range(2):
        for y in range(2):
            if mayPar<a[x][y]:
                mayPar = a[x][y]
    print('El mayor es: ',mayPar)

def mayorImpar():
    mayImpar = 0
    for w in range(2):
        for z in range(2):
            if mayImpar<b[w][z]:
                mayImpar = b[w][z]
    print('El mayor es: ',mayImpar)
    
def menorPar():
    menPar = 10000000000000000000000000000000
    for x in range(2):
        for y in range(2):
            if menPar>a[x][y]:
                menPar = a[x][y]
    print('El menor es: ',menPar)
    
def menorImpar():
    menImpar = 100000000000000000
    for w in range(2):
        for z in range(2):
            if menImpar>b[w][z]:
                menImpar = b[w][z]
    print('El menor es: ',menImpar)
    
def is_prime(a):
  for x in range(2,a):
    if (a%x) == 0:
                                                                                                                        return False
  return True
    
validarPares()
llenarPares()
validarImpares()
llenarImpares() 

for m in a:
    print(a)
    
for e in b:
    print(b)

mayorPar()
menorPar()
mayorImpar()
menorImpar()
is_prime()