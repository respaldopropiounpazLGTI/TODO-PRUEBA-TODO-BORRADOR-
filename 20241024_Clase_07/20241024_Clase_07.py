#encoding: utf-8
'''Este ejercicio tenia como pròposito mostrar la estructura de un programa en Python,
el ambito de las variables y la definicion de funciones. Probamos jugando con las funciones locales
y globales, y con el paso de parametros por valor a las funciones.
explicamos los concepros de parametros actuales y formales, y como se comportan las variables
explicamos el tema del retorno de valores en las funciones y como se pueden utilizar.
Usamos una funcion main para controlar todas las variables, funciones y el flujo del programa.'''
def udf_funcion1(pmivar2):
    print("Hola mundo",pmivar2)

def udf_funcion2(pmiVar):
    print(f"Hola mundo 2 {pmiVar}")

def mi_len(ppalabra):
    cantidad=0
    for letra in ppalabra:
        #print(letra)
        cantidad+=1
    return cantidad

def mimain():
    cantidad=99
    mivar2 = '2'  # Ambito Global
    mivar='1' #Ambito Local
    mitexto="Hola Mundo"
    mitexto2="Mundo"
    mivarint=int(mivar)
    print(mivarint)
    udf_funcion1(mivar)
    udf_funcion2(mivar2)
    resul=mi_len(mitexto)
    result2=mi_len(mitexto2)
    print(len(mitexto),cantidad,'Aca aparece milen:',resul,'Aca aparece milen:',result2)


#Programa Principal
mimain()
