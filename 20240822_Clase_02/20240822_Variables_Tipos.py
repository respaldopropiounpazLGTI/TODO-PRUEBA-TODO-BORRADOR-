'''
aca les menti
entrada
proceso
salida
'''
#declaras y tipas, asignacion de un valor a la variable
vix=4  #int
print('Valor parcial de mi primer valor int x fue:',vix)
vix=6  #int
print('Ultimo valor de mi Int X',vix)
viyconcoma=6.5 #float
print('Aca tengo mi primer dato float', viyconcoma)
vix=6.5 #float (era int peroi asigno un float y se castea automaticamente a float)
print('Ultimo valor de X que era int pero lo autocastie a float', vix)
caracter='a' #char
print ('Aca tengo mi primer caracter',caracter)
caracter='1' #char
print ('Aca tengo mi primer sobreescrtio',caracter)
#Esta es una situacion donde quiero sumar un caracter que era un eventual numero pero estaba entre comillas
#y era un char. COmo lo quiero pasar a numero lo casteo a int
print ('Aca tengo mi primer sobreescrtio',int(caracter)+2)
#---------------------------------------
#Asignacion multiple
x,y,z=1,2,3
print('Asignacion multiple:',x,y,z)
#Mi primer string
miString='Hola Mundo'
print('Mi primer string:',miString)
#mi primer booleano
miBooleano=False
print('Mi primer booleano:',miBooleano)
print('Mi primer booleano:',miBooleano==0)
otroentero=5
print('Otro entero:',type(otroentero))
resultado=otroentero+5
print('Resultado:',resultado, type(resultado))
#Casteo de un entero a float implicito
resultado=otroentero*1.5
print('Resultado (Habra cambiado el tipo???:',resultado, type(resultado))
#Casteo de un entero a float explicito
resultado=float(otroentero)*1
print('Resultado (Habra cambiado el tipo???:',resultado, type(resultado))
#Hblamos de casteo y ahora vamos a hablar de concatenacion
#Concatenacion de dos strings
minum_char='1'
miotronum_char='2'
resultado=miotronum_char+minum_char
print("Concatenacion de dos strings:",resultado)

minum_char='1'
miotronum_char='2'
resultado=int(miotronum_char)+float(minum_char)
print("Suma Aritmetica con casteo explicito:",resultado,type(resultado))

mifloat=1.5
print('Mi primer float casteado y truncado:',int(mifloat))