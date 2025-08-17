# -*- coding: utf-8 -*-
'''
Algoritmo sin_titulo
	Leer numeroA
	Leer numeroB
	Escribir "1-Sumarlos"
	Escribir "2-Restarlos"
	Escribir "3-Multiplicarlos"
	Escribir "4-Dividirlos"
	Leer OpcionDecision


	Si OpcionDecision = 1 Entonces
		Escribir numeroA+numeroB
	SiNo
		Si OpcionDecision=2 Entonces
			Escribir numeroA-numeroB
		SiNo
			Si OpcionDecision= 3 Entonces
				Escribir numeroA*numeroB
			SiNo
				Si OpcionDecision = 4 Entonces
					Escribir 	numeroA/numeroB
				SiNo
					Escribir "Opcion no Valida"
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
'''

numeroA = int(input("Ingrese el numero A: "))
numeroB = int(input("Ingrese el numero B: "))
while True:
    print("1-Sumarlos")
    print("2-Restarlos")
    print("3-Multiplicarlos")
    print("4-Dividirlos")
    print("5-Salir")
    OpcionDecision=int(input("Ingrese la opcion: "))
    match OpcionDecision:
        case 1:
            print ('Selecciono suma: ',numeroA+numeroB)
        case 2:
           print ('Selecciono resta', numeroA-numeroB)
        case 3:
           print ('Selecciono multiplicacion', numeroA*numeroB)
        case 4:
           print('Selecciono division', numeroA/numeroB)
        case 5:
            break
        case _:
           print('Errors')



'''
if OpcionDecision == 1:
    print(numeroA+numeroB)
else:
    if OpcionDecision == 2:
        print(numeroA-numeroB)
    else:
        if OpcionDecision == 3:
            print(numeroA*numeroB)
        else:
            if OpcionDecision == 4:
                print(numeroA/numeroB)
            else:
                print("Opcion no Valida")
'''
#Otra forma de hacerlo
'''
if OpcionDecision == 1:
    print(numeroA+numeroB)
elif OpcionDecision == 2:
    print(numeroA-numeroB)
elif OpcionDecision == 3:
    print(numeroA*numeroB)
elif OpcionDecision == 4:
    print(numeroA/numeroB)
else:
    print("Opcion no Valida")
'''



