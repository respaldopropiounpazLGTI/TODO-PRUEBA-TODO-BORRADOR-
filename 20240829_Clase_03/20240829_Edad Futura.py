# -*- coding: utf-8 -*-
'''
Algoritmo EntradasYSalidas
	Escribir "Ingrese La edad:"
	Leer edad
	Escribir "Cuantos años a futuro:"
	Leer edadIntervalo
	Escribir "Ingrese el Peso:"
	Leer peso
	result=edad+edadIntervalo
	Escribir 'En ', edadIntervalo," años voy a a tener ",result, "El peso es: ",peso
FinAlgoritmo
'''
miEdad=int(input("Introduce tu edad: "))
miEdadFuturaAnios=int(input("Introduce los años a sumar a tu edad: "))
miPeso=float(input("Introduce tu peso: "))
resulEdad=miEdad+miEdadFuturaAnios
print("Tu edad es: ", resulEdad, "y tu peso es: ", miPeso)
#otras formas de hacer print mediante format
print(f'Tu edad es: {resulEdad} y tu peso es: {miPeso}')
#Otra mediante casteo
print("El Resultado es:" + str(resulEdad) + " y peso " + str(miPeso))
#Otra mediante format
print("El Resultado es: {} y peso {} ".format(resulEdad, miPeso))
#Otra mediante %
print("El Resultado es: %3d, y peso : %2.2f" % (resulEdad, miPeso))
print(1,2,3,4,sep='|',end='*')
#replicar *
print()
print("*"*10)
print("******************************************")

print("******************************************")
