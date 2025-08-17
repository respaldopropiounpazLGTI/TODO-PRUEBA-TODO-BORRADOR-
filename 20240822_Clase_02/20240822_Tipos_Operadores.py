#Opeadores Relacionales
# == igual
# != diferente
# < menor que
# > mayor que
# <= menor o igual que
# >= mayor o igual que

print("==:",1==1)
print(">=:",1>=1)
print('>:',1>1)
print('<:',1<1)
print('<=:',1<=1)

#Operadores Logicos
# and y
#Tabla de verdad AND
# v and v = v
# v and f = f
# f and v = f
# f and f = f
print('Primer uso del AND:',1==1 and 1>1)
print('Segundo uso del AND:',1==1 and 2>1)

# or o
#Tabla de verdad OR
# v or v = v
# v or f = v
# f or v = v
# f or f = f
print('Primer uso del OR:',1==1 or 1>1)
print('Segundo uso del OR:',1==1 or 2>1)
print('Tercer uso del OR:',1!=1 or 2<1)


#Tabla de verdad NOT
# not v = f
# not f = v


print('Niego 1 vez:',not(1==1 and 1>1))
print('Niego dos veces:',not(1==1 and 2>1))
print('Niego tres veces:',not(1==1) and not(2>1))

#Operadores de Aritmeticos
# + suma
# - resta
# * multiplicacion
# / division
# // division entera
# % modulo
resultado = 2+1
resultado2 = 2-1
resultado3 = 2*2
resultado4 = 9/2
resultado5 = 9//2
resultado6 = 8%4
print('Suma:',resultado)
print('Resta:',resultado2)
print('Multiplicacion:',resultado3)
print('Division:',resultado4)
print('Division Entera:',resultado5)
print('Modulo:',resultado6)
print('Es multiplo 9 de 3 ??:',9%3==0)
print('Es multiplo 9 de 5 ??:',9%5==0)

#Operadores de Asignacion
# = asignacion
# += incremento
# -= decremento
# *= multiplicacion
a=0
a=a+1
print('Incremento:',a)
a=a+1
print('Incremento:',a)
a+=1
print('Incremento:',a)
a=a-1
print('decreemento:',a)
a-=1
print('decreemento:',a)
a-=1
print('decreemento:',a)
