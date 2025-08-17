import random

# Generar un número secreto entre 1 y 10
numero_secreto = random.randint(1, 10)

# Inicializar las variables
vi_intentos_maximos = 3
intentos_realizados = 0
adivinado = False

print("¡Bienvenido al juego del Número Secreto!")
print("Debes adivinar un número entre 1 y 10.")
print(f"Tienes {vi_intentos_maximos} intentos para adivinar el número correcto.\n")

# Ciclo while que se ejecuta mientras no haya adivinado y la cantidad de errores sea menor a 3
while intentos_realizados < vi_intentos_maximos and not adivinado:
    # Pedir al usuario que ingrese un número
    adivinanza = int(input(f"Intento {intentos_realizados + 1}: ¿Cuál es tu número? "))

    # Comprobar si la adivinanza es correcta
    if adivinanza == numero_secreto:
        print(f"¡Felicidades! Has adivinado el número secreto ({numero_secreto}) en {intentos_realizados + 1} intento(s).")
        adivinado = True
    elif adivinanza < numero_secreto:
        print("El número es mayor. Intenta de nuevo.")
    else:
        print("El número es menor. Intenta de nuevo.")

    # Incrementar el contador de intentos
    intentos_realizados += 1

# Si el bucle se termina y no ha adivinado, mostrar el número secreto
if not adivinado:
    print(f"\nLo siento, no has adivinado el número. El número secreto era {numero_secreto}.")
