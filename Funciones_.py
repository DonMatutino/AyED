def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma = numero 
    return suma

def funcion(multiplica, *args):
    for i in range(0, len(args)):
        if i % 2 == 0:
            print(F"El numero {args[i]} multiplicado por {multiplica} resulta {args[i]*multiplica}")
        else:
            print(F"El numero {args[i]} dividido por {multiplica} resulta {args[i]/multiplica}")


resultado = sumar_numeros(2, 2, 3, 4, 5, 9)
resultado1 = sumar_numeros(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
#12 en 1
print(resultado)
print(resultado1)

funcion(2, 1, 2, 3, 4, 5, 6, 7, 8, 9)

