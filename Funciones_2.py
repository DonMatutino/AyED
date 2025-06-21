def funcion(**kwargs):
    print(type(kwargs))
    for k, v in kwargs.items():
        print(F"A la clave {k} les corresponde el valor {v}")

funcion(matias=100, nahuel=100)