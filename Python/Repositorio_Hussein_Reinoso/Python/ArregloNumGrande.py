'''Hacer un programa que en un matriz de 4x4 se llene exclusivamente con numeros y exclusivamente con dos digitos,
despues mostrara el numero mas grande introducido'''


def validar():
    a = input('Escribe un numero: ')
    if len(a)==2:
        if a.isdigit():
            return a
        else:
            print('Error')
            return validar()
    else:
        print('Error')
        return validar()

def llenar():
    for x in range(4):
        for y in range(4):
            ar[x][y]=int(validar())
                    
def mayor():
    aux = 0
    for x in range(4):
        for y in range(4):
            if aux<ar[x][y]:
                aux = ar[x][y]
    print('El mayor es: ',aux)
    



ar = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]  
llenar()
for i in ar:
    print(i)
mayor()
    