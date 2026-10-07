#def suma(a, b):
#    """Función que suma dos números."""
#   return a + b
# pero si quiero sumar  N numeros, puedo usar *args para recibir un número variable de argumentos


def suma(*numeros):
    """Función que suma N números."""
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(1, 2, 3, 4, 5)  # Esto imprimirá 15
suma(10, 20)        # Esto imprimirá 30
suma (2, 11,8,10)