vi_edad=int(input("Ingrese su edad: "))
vc_nacionalidad=input("Ingrese su nacionalidad: ")
if vc_nacionalidad=="AR" and vi_edad>=16:
    dni=input("Ingrese su DNI: ")
    print(f"Puede votar el DNI es: {dni}")
else:
    print("No puede votar")


print("Fin del Programa")

