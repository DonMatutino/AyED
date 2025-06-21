import_random

palabras = ['harry', 'azkaban', 'dumbledore', 'hipogrifo', 'transfiguración']
secreta = random.choice(palabras)
cadena = "-" * len(secreta)
print("Bienvenido al juego del ahorcado")
intentos = 0

while_true:
    print(cadena)
    letra = input("Ingrese una letra: ")
    if letra in secreta:
         for i in range(len(secreta)):
              if secreta[i] == letra:
                   cadena = cadena[:i] + letra + cadena[i+1:]
    else:
        if intentos
