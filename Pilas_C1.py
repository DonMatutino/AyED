class Nodo:
    '''Clase que representa un Nodo para construir una Pila'''
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

    def __repr__(self):
        # Si el dato es None, muestra None, si tiene dato muestra el dato
        return str(self.dato) if self.dato is not None else "None"


class Pila:
    '''Implementación de una Pila en Python'''
    def __init__(self):
        self.cima = None
        self.tamanio = 0


nodo1 = Nodo()
nodo2 = Nodo(1)
nodo3 = Nodo(2)

nodo1.siguiente = nodo2
nodo1.siguiente.siguiente = nodo3

print(nodo1)  # Ahora imprime None
print(nodo1.siguiente.dato)  # 1
print(nodo1.siguiente.siguiente.dato)  # 2

def push(pila, dato_nuevo):
    '''Agrega un nuevo nodo a la cima de la Pila'''
    nodo_a_apilar = Nodo(dato_nuevo)
    nodo_a_apilar.siguiente = pila.cima
    pila.cima = nodo_a_apilar
    pila.tamanio += 1

def pop(pila): # desapila
    '''Devuelve el último nodo ingresado LIFO, y lo remueve de la Pila'''
    nodo_a_retornar = pila.cima
    pila.cima = nodo_a_retornar.siguiente
    pila.tamanio -= 1
    return nodo_a_retornar


pila1 = Pila()
push(pila1, 'A')
push(pila1, 'B')
push(pila1, 'C')
print(pila1.cima.dato)
print(pila1.tamanio)
resultado = pop(pila1)
print(dato)