#56. Contador de caracteres: Escribe un programa que pida al usuario que ingrese una
#cadena de texto y luego cuente cuántos caracteres tiene esa cadena (sin incluir
#espacios en blanco).
palabra=input("ingrese cadena de texto ")
junto=palabra.replace(" ","")
cadena=len(junto)
print("la cadena de texto tiene una extencion de:",cadena,"   palabras en total ")
print(junto)