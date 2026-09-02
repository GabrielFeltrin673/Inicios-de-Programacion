n1 = input("Digite o primeiro número: ")
n2 = input("Digite o segundo número: ")

n1  = int(n1)
n2  = int(n2)

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
div = n1 / n2

mensaje = f"""
PAra los numeros {n1} y {n2}, la suma es {suma}, la resta es {resta}, la multiplicación es {multiplicacion}
y la división es {div}."""

print (mensaje)
