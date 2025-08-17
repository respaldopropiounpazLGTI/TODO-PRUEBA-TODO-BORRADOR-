#6. Escribir un programa que simule un juego de adivinanza. El programa deberá elegir un número aleatorio entre 1 y 100,
# y pedirle al usuario que adivine cuál es el número. El usuario deberá ingresar un número,
# y el programa deberá decirle si el número ingresado es mayor o menor que el número a adivinar.
# El juego termina cuando el usuario adivina el número correcto, y se le muestra al usuario cuántos
# intentos le llevó.
# Nota: Solo tiene 5 intentos.
import random
intento=0
numero_a_adivinar=random.randint(1,100)
print("pista==>",numero_a_adivinar)
while True:
	numero_usuario=int(input(f" adivine el numero usted tiene 5 intentos en total  !!! "))
	if numero_usuario==numero_a_adivinar:
		intento+=1
		print(" adivino muy bien!! numero de intento",intento)
		break
	elif numero_usuario>numero_a_adivinar:
		intento+=1
		print(" te pasaste ")
		if intento==5:
			print(" no quedan mas intentos  ")
			break
	elif numero_usuario<numero_a_adivinar:
		intento+=1
		print(" te falto !!! ")
		if intento==5:
			print(" sin mas intentos ")
			break
