edad = 55
if edad >= 54:
    print("Eres adulto mayor")
elif edad >= 18:
    print("Eres mayor de edad")

else: 
    print("Eres menor de edad")

print ("Fin del programa")



#if es una estructura de control que permite ejecutar un bloque de código si se cumple una condición. En este caso,
#se verifica si la variable edad es mayor o igual a 18. Si la condición es verdadera, se imprime "Eres mayor de edad
# ". Si la condición es falsa, se ejecuta el bloque dentro del else y se imprime "Eres menor de edad". Al final, se 
# imprime "Fin del programa" independientemente de la condición.
#identar es importante en Python para definir los bloques de código que pertenecen a cada estructura de control. 
# Se hace con tab o con 4 espacios.
#El operador elif permite agregar condiciones adicionales a la estructura if-else. En este caso, se verifica si la
# variable edad es mayor o igual a 54. Si la condición es verdadera, se imprime "Eres adulto mayor". Si la condición
#es falsa, se verifica la siguiente condición elif. Si ninguna de las condiciones se cumple, se ejecuta el bloque
#dentro del else.
#el orden de evaluacion es de arriba hacia abajo, es decir, primero se evalua la condicion if, luego elif y 
#finalmente else. Por eso el orden es importante, ya que si se cumple una condicion, las demas no se evaluaran.