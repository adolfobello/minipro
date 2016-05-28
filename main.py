# Este es el punto de entrada al sistema
# Se supone que al menos da una letra.
nombre = input("Por favor, cual es su nombre? ")
# print("Hola %s" % nombre)
# Pide un numero. Supone que lo es.
n = int(input("Hola %s. Que numero quiere saber si es par: " % nombre ))
if (n%2) == 0:
    print("%s, el numero %s es par" % (nombre, n) )
else:
    print("%s, el numero %s es impar" % (nombre, n) )
