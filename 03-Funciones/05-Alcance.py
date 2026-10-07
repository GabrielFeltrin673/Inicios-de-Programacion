saludo = "Hola global"

def saludar():
    saludo = "Hola"
    print(saludo)  # This will print "Hola"
def saludar2():
    saludo = "Hola 2"
    print(saludo)  # This will print "Hola 2"

print(saludo)  # This will print "Hola global"
saludar()
saludar2()

#El docente recomienda no utilizar variables globales, ya que pueden generar errores en el código.