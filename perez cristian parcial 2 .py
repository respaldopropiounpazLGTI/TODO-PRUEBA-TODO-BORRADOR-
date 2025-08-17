#Escribir un algoritmo que permita cargar un vector de 10 numeros enteros
# (positivos o negativos) entre -100 y 100.
# No debe aceptar .

import array as a
CANT_NUMEROS = 3
numeros = a.array("i", range(CANT_NUMEROS))
for numeros in range(CANT_NUMEROS):
    numero_ingresado=int(input(f" ingrese numero {numeros+1}: "))
    if numero_ingresado >=-100:
     if numero_ingresado <= 100:
        print("numeros)"

































