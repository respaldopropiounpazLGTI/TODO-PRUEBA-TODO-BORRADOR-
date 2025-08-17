# -*- coding: utf-8 -*-
import random

# Generar un número secreto entre 1 y 10
vi_numero_secreto = random.randint(1, 10)

# Número de intentos permitidos
vi_intentos_programados = 3
print(vi_numero_secreto)
print("¡Bienvenido al juego del Número Secreto!")
print("Debes adivinar un número entre 1 y 10.")
print(f"Tienes {vi_intentos_programados} intentos para adivinar el número correcto.\n")

# Ciclo para permitir hasta 3 intentos
for intento_hechos in range(1, vi_intentos_programados + 1):
    # Pedir al usuario que ingrese un número
    adivinanza = int(input(f"Intento {intento_hechos}: ¿Cuál es tu número? "))

    # Comprobar si la adivinanza es correcta
    if adivinanza == vi_numero_secreto:
        print(f"¡Felicidades! Has adivinado el número secreto ({vi_numero_secreto}) en {intento_hechos} intento(s).")
        break
    elif adivinanza < vi_numero_secreto:
        print("El número es mayor. Intenta de nuevo.")
    else:
        print("El número es menor. Intenta de nuevo.")

    # Informar si se ha llegado al tercer intento sin éxito
    if intento_hechos == vi_intentos_programados:
        print(f"\nLo siento, no has adivinado el número. El número secreto era {vi_numero_secreto}.")
