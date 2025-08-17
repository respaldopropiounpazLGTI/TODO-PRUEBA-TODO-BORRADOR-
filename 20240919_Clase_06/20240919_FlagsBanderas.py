#Una carrera los autos dan hasta 15 vueltas.
#Es de interes saber si alguno de los autos es color naranja
#En caso lo sea al finalizar indicar si hubo o no hubo
#Si hay un naranja dejo de cargar
flagHubo206=False #hipotesis o estado inicial
ivuelta=0
while ivuelta < 5:
        #and not flagHubo206:
    ivuelta+=1
    vsTipo=input ("Ingrese Tipo Auto "+str(ivuelta)+': ')
    if vsTipo.upper() == '206':
        flagHubo206=True

#if flagHuboNaranja == True:
if flagHubo206:
    print("Hubo al menos un auto 206")
else:
    print("No Hubo ni uno")

