# -*- coding: utf-8 -*-
# Inicializacion de variables
vi_suma_valores = 0
vs_palabra_mas_valiosa = ""
max_valor = 0

# Ingresar 5 palabras y valorarlas en el momento
for i in range(5):
    palabra = input(f"Ingrese la palabra {i+1}: ")
    valor_total = 0

    # Calcular el valor de la palabra
    for letra in palabra.lower():
        if letra == 'a':
            valor_total += 1
        elif letra == 'e':
            valor_total += 2
        elif letra == 'i':
            valor_total += 3
        elif letra == 'o':
            valor_total += 4
        elif letra == 'u':
            valor_total += 5
        else:
            valor_total += 2  # Las consonantes y demás caracteres valen 2 puntos

    # Mostrar el valor de la palabra
    print(f"El valor de la palabra '{palabra}' es: {valor_total}")

    # Acumular el valor para calcular el promedio después
    vi_suma_valores += valor_total

    # Comparar si es la palabra más valiosa hasta ahora
    if valor_total > max_valor:
        max_valor = valor_total
        vs_palabra_mas_valiosa = palabra

# Calcular el promedio
promedio_valores = vi_suma_valores / 5
print(f"\nEl valor promedio de las palabras es: {promedio_valores:.2f}")

# Mostrar la palabra más valiosa
print(f"La palabra con mayor valor es: '{vs_palabra_mas_valiosa}' con un valor de {max_valor}")
