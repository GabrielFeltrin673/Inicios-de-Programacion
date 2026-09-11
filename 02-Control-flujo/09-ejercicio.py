# crear una aplicacion interactiva
# esta aplicacion tiene que verificar si ya ingresamos un numero
# si no lo ingreso hay que pediirle que lo ingrese. Luego de eso hay
#  que pedirle que ingrese una operacion
# si ya lo ingreso, hay qu epedirle que ingrese una operacion
# ona vez que ingresa la operacion hay que pedirle que ingrese un
#  segundo numero.
# una vez que hace eso, debemos mostrar el resultado, cuando esto su
# ceda, la guardamos como el primer
# numero y le pedimos que ingrese otra operacion

# mi calculadora interactiva

n1 = input("Ingrese un numero: ")

while n1 != "salir":
    if n1 == "":
        n1 = input("Ingrese un numero: ")
    else:
        operacion = input("Ingrese una operacion (+, -, *, /): ")
        n2 = input("Ingrese un segundo numero: ")

        if operacion == "+":
            resultado = float(n1) + float(n2)
        elif operacion == "-":
            resultado = float(n1) - float(n2)
        elif operacion == "*":
            resultado = float(n1) * float(n2)
        elif operacion == "/":
            if float(n2) != 0:
                resultado = float(n1) / float(n2)
            else:
                print("Error: Division por cero")
                continue
        else:
            print("Operacion no valida")
            continue

        print(f"El resultado es: {resultado}")
        n1 = str(resultado)  # Guardamos el resultado como el primer numero
