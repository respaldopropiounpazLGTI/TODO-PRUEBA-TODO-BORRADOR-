def udf_duplica(pmiNumero):
    return pmiNumero*2

def udf_triplica(pmiNumero):
    return pmiNumero*3

def udf_cuatriplica(pmiNumero):
    return pmiNumero*4

def def_quint_sextiplica(pmiNumero):
    mi5tuple=pmiNumero*5
    mi6tuple=pmiNumero*6

    return mi5tuple,mi6tuple

def miMenu():
    opcion=0
    print("1-Duplica")
    print("2-Triplica")
    print("3-Cuatriplica")
    print("4- Quintu y Sextuplica")
    print("5-Salir")
    opcion=int(input("Ingrese una opcion"))
    return opcion

def mimain():
    numero_atrabajar=int(input("Ingrese un numero"))
    while True:
        opcion_recibida=miMenu()
        if opcion_recibida==1:
            print(f"El resultado de duplicar {numero_atrabajar} es: {udf_duplica(numero_atrabajar)}")
        elif opcion_recibida==2:
            print(f"El resultado de triplicar {numero_atrabajar} es: {udf_triplica(numero_atrabajar)}")
        elif opcion_recibida==3:
            result=udf_cuatriplica(numero_atrabajar)
            print(f"El resultado de cuatriplicar {numero_atrabajar} es: {result}")
        elif opcion_recibida == 4:
            result1,result2=def_quint_sextiplica(numero_atrabajar)
            print(f"El resultado de quintuplicar {numero_atrabajar} es: {result1}")
            print(f"El resultado de sextuplicar {numero_atrabajar} es: {result2}")
        else:
            print("Adios")
            break


#Programa Principal
mimain()