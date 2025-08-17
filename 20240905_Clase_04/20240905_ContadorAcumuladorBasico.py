
cant_personas = int(input("Ingrese la cantidad de personas: "))
acum=0
contar=0
acum = 0
for i in range(cant_personas):

    edad=int(input("Ingrese la edad: "))
    print(f"Antes acum: {acum} y cuento: {contar}")
    acum=acum+edad
    contar=contar+1
    print(f"Despues acum: {acum} y cuento: {contar}")

print(f"El promedio de edades es: {acum/cant_personas}")

