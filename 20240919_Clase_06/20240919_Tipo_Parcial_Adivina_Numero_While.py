import random

# Generar un n�mero secreto entre 1 y 10
numero_secreto = random.randint(1, 10)

# Inicializar las variables
vi_intentos_maximos = 3
intentos_realizados = 0
adivinado = False

print("�Bienvenido al juego del N�mero Secreto!")
print("Debes adivinar un n�mero entre 1 y 10.")
print(f"Tienes {vi_intentos_maximos} intentos para adivinar el n�mero correcto.\n")

# Ciclo while que se ejecuta mientras no haya adivinado y la cantidad de errores sea menor a 3
while intentos_realizados < vi_intentos_maximos and not adivinado:
    # Pedir al usuario que ingrese un n�mero
    adivinanza = int(input(f"Intento {intentos_realizados + 1}: �Cu�l es tu n�mero? "))

    # Comprobar si la adivinanza es correcta
    if adivinanza == numero_secreto:
        print(f"�Felicidades! Has adivinado el n�mero secreto ({numero_secreto}) en {intentos_realizados + 1} intento(s).")
        adivinado = True
    elif adivinanza < numero_secreto:
        print("El n�mero es mayor. Intenta de nuevo.")
    else:
        print("El n�mero es menor. Intenta de nuevo.")

    # Incrementar el contador de intentos
    intentos_realizados += 1

# Si el bucle se termina y no ha adivinado, mostrar el n�mero secreto
if not adivinado:
    print(f"\nLo siento, no has adivinado el n�mero. El n�mero secreto era {numero_secreto}.")
