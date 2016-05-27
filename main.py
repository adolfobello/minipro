# Este es el punto de entrada al sistema
print("Hello world")
# Pide un numero. Supone que lo es.
n = int(input("Que numero quiere saber si es par: "))
if (n%2) == 0:
    print("El numero %s es par" % n )
else:
    print("El numero %s es impar" % n )
