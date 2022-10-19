from ast import If


def validarnumero(op):
    con = 0
    if op.isdigit():
         return True
    else:
        return False
             
def crearPila():
    print('La pila fue creada')

def ingresar():
    valor = input('Escribe un valor a la pila:')
    if validarnumero(valor):
        pila.append(valor)
    else:
        print('Error de datos')
        ingresar()
        
    
def mostrar():
    print(pila)
    
def menu():  
    print('1.- Crear Pila')
    print('2.- Ingresar elemento a la pila: ')
    print('3.- Eliminar elemento de una pila')
    print('4.- Vaciar pila')
    print('5.- Mostrar pila')
    print('6.- Salir')
    op = input('Elige una opcion: \n')
    if (validarnumero(op)):
        o = int(op)
        if o>=1 and o<=6:
            if 0==1:
                crearPila()
            if o==2:
                ingresar()
            if o==3:
                eliminar()
            if o==4:
                vaciarPila() 
            if o==5:
                mostrar()
            if o==6:
                return op
                 
    else:
        print('Error al ingresar, porfavor vuelva a ingresar')
        menu()

pila=[]      
op = '1'  
while(op!='6'):     
    op = menu()