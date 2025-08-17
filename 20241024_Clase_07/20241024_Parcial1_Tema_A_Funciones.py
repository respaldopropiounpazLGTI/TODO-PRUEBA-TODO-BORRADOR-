#unicode utf-8

def conteo_vocales(palabra):
    cantidad_vocales=0
    for letra in palabra:
        if letra in "aeiou":
            cantidad_vocales+=1
    return cantidad_vocales

def mi_len(ppalabra):
    cantidad=0
    for letra in ppalabra:
        cantidad+=1
    return cantidad

def mimain():
    cuento=0
    palabra_mas_vocales=""
    cantidad_palabras= int(input("Ingrese la cantidad de palabras que desea procesar: "))
    for i in range(cantidad_palabras):
        mi_palabra=input(f"Ingrese la palabra {i+1}: ")
        cant_vocales=conteo_vocales(mi_palabra)
        cant_letras_total=mi_len(mi_palabra)
        porc_vocales=(cant_vocales/cant_letras_total)*100
        if porc_vocales <=50:
            cuento=cuento+1
        if i == 0:
            palabra_mas_vocales = mi_palabra
            porc_vocales_max = porc_vocales
        else:
            if porc_vocales > porc_vocales_max:
                palabra_mas_vocales = mi_palabra
                porc_vocales_max = porc_vocales
        print(f"La palabra '{mi_palabra}' tiene {cant_vocales} vocales, y {cant_letras_total} letras en total, lo que representa un {porc_vocales:.2f}% de vocales")


    print("La palabra con mayor porcentaje de vocales es:",palabra_mas_vocales, "Con un porcentaje de:",porc_vocales_max)
    print("La cantidad de palabras con menos del 50% de vocales es:",cuento)


#area de gobal principal
mimain()