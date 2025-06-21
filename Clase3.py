class Pila:
    '''Estructura Pila implementada con una lista de Python'''
    def __init__(self):
        'Inicializa una pila vacia'
        self.elementos = []

    def len(self):
        '''Devuelve la cantidad de elementos de la pila'''
        return len(self.elementos)
    
    def is_empty(self): -> bool:
        return len(self.elementos) == 0
