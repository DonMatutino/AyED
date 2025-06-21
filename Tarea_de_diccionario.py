# USO DE DICCIONARIOS

# Pedir el usuario 10 DNI y sus correspondientes NOMBRES

# Guardarlo en un diccionario 

personas = {
    "12345678": "Ana Gómez",
    "23456789": "Bruno Díaz",
    "34567890": "Camila Torres",
    "45678901": "Diego Fernández",
    "56789012": "Elena Rodríguez",
    "67890123": "Facundo Herrera",
    "78901234": "Gabriela López",
    "89012345": "Hernán Pérez",
    "90123456": "Ivana Méndez",
    "01234567": "Julián Castro"
}

while True:
    dni_buscado = input("\nIngresá el DNI que querés buscar -->")
    if dni_buscado.lower() == 'salir':
        print("Saliendo del buscador.")
        break
    if dni_buscado in personas:
        print("DNI:", dni_buscado)
        print("Nombre:", personas[dni_buscado])
    else:
        print("DNI no encontrado en la base de datos.")
