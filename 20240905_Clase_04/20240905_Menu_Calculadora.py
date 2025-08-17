
while True:
    print("1-Sumar")
    print("2-Restar")
    print("3-Multiplicar")
    print("4-Dividir")
    print("5-Salir")
    vi_opcion=int(input("Ingrese una opcion: "))
    if vi_opcion==5:
        break
    if vi_opcion<1 or vi_opcion>5:
        print("Opcion incorrecta")


print("Fin del programa")