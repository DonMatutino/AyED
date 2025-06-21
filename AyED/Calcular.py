# Pedimos al usuario que ingrese números separados por coma
entrada = input("Ingresa números separados por coma (ejemplo: 1,5,7,5) ")

# Convertimos la cadena en una lista de enteros
numeros = [int(x.strip()) for x in entrada.split(",")]

# Calculamos el promedio
promedio = sum(numeros) / len(numeros)

print("El promedio es:", promedio)
