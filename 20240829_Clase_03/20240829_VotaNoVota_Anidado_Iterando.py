# -*- coding: utf-8 -*-
'''
vi_edad=int(input("Ingrese su edad: "))
vc_nacionalidad=input("Ingrese su nacionalidad: ")
if vc_nacionalidad=="AR" and vi_edad>=16:
    dni=input("Ingrese su DNI: ")
    print(f"Puede votar el DNI es: {dni}")
else:
    print("No puede votar")
print("Fin del Programa")
'''
print (list(range(1,3)))
vi_cantidad_votantes=int(input("Ingrese la cantidad de votantes: "))
for cp in range(1,vi_cantidad_votantes+1,1):
    vi_edad=int(input(f"Ingrese  la edad del votante {cp}: "))
    vc_nacionalidad=input(f"Ingrese la nacionalidad de {cp}: ")

    if vi_edad >= 16:
        if vc_nacionalidad=="AR":
            dni=input("Ingrese su DNI: ")
            print(f"Puede votar el DNI es: {dni}")
        else:
            print(f"No puede votar por mas alla que sos mayor {vi_edad}, pero tenes nacionalidad {vc_nacionalidad}")
    else:
        print(f"No puede votar por tema de edad ya que tenes {vi_edad} años")

print("Fin del Programa")