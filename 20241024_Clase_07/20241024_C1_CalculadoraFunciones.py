def miMenu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion: "))
    return opcion

def udfSuma(pnuma,pnumb):
    return pnuma+pnumb

def udfResta(pnuma,pnumb):
    return pnuma-pnumb

def udfMultiplicacion(pnuma,pnumb):
    return pnuma*pnumb

def udfDivision(pnuma,pnumb):
    if pnumb==0:
        return print("no se puede dividir por 0"),-1
    else:
        return pnuma/pnumb



def udfMain():
    while True:
        opcionSeleccionada = miMenu()
        if opcionSeleccionada >=1 and opcionSeleccionada <=4:
            numa=int(input("Ingrese un numero: "))
            numb=int(input("Ingrese otro numero: "))

        match opcionSeleccionada:
            case 1:
                print("Suma",udfSuma(numa,numb))
            case 2:
                print("Resta",udfResta(numa,numb))
            case 3:
                print("Multiplicacion",udfMultiplicacion(numa,numb))
            case 4:
                print("Division",udfDivision(numa,numb))
            case 5:
                print("Salir")
                break
            case _: ##Es como un else
                print("Opcion incorrecta")



#-------Area publica de ejecucion
udfMain()



