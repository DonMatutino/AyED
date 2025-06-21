def modulo_signo_dividendo(a, b):
    r = a % b
    if a < 0 and r != 0:
        return r - b
    return r

entero1 = -900
resultado = modulo_signo_dividendo(entero1, 78971)
print("Resultado:", resultado)
