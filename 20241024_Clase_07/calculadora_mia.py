def monstra_menu():
    print(" BIENVENIDO A CALCULADORA ")
    print("ingrese  1/suma ")
    print("ingrese  2/resta ")
    print("ingrese  3/multiplicacion ")
    print("ingrese  4/dividion ")
    opcion=input("que desea hacer ? " )
    return opcion

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b


def mi_main():
    opcion_selecionada=monstra_menu()
    if opcion_selecionada=="1" or opcion_selecionada=="suma":
        numero1=int(input("ingrese  numero 1"))
        numero2=int(input("ingrese  numero 2"))
        print(" la suma es : ",suma(numero1,numero2))
    elif opcion_selecionada=="2" or opcion_selecionada=="resta":
        numero1=int(input("ingrese valor 1"))
        numero2=int(input("ingrese valor 2"))
        print(" la resta es ",resta(numero1,numero2))
    elif opcion_selecionada=="3" or opcion_selecionada=="multiplicacion":
        numero1=int(input("ingrese valor 1"))
        numero2=int(input("ingrese valor 2"))
        print("la multiplicacion es ",multiplicacion(numero1,numero2))
    elif opcion_selecionada=="4"or opcion_selecionada=="division":
        numero1=int(input("ingrese valor 1"))
        numero2=int(input("ingrese valor 2"))
        if numero2==0:
            print("no se puede dividir por 0 fin del programa ")
        else:
            print("la division es ",division(numero1,numero2))
    else:
        print(" opcion equivocada ")

mi_main()
