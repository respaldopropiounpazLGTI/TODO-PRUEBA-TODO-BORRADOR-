import array as arr
#Quiero registrar los tiempos de vuelta de una carrera de colapinto y que me des el tiempo promedio
#y la vuelta mas rapida y lenta
#Realizar un menu que permita:
# 1)los registos de las vueltas (Carga)
# 2) la visualizacion de los tiempos (Informar Vuielta)
# 3) La mejor vuelta
# 4) La peor vuelta
# 5) El promedio de las vueltas
# 6) Salir
#Definicion y dimensionamiento


def mi_menu():
    print("(1) Carga los registos de las vueltas")
    print("(2) Informar Tiempos de Vuelta")
    print("(3) Informar la mejor vuelta")
    print("(4) Informar la peor vuelta")
    print("(5) Informar el promedio de las vueltas")
    print("(6) Salir")
    opcion=int(input("Ingrese Opcion:"))
    return opcion


def udf_registra_vueltas(pmiVuelta, pCantVueltas):
    for i in range (0,pCantVueltas,1):
        pmiVuelta[i]=int(input(f'Tiempo Vuelta [{i}] en seg.:'))


def udf_informar_vuelta(pmiVuelta,pCantVueltas):
    for i in range (0,pCantVueltas,1):
        if i%2!=0:
            print(f'Tiempo Vuelta[{i}]:{pmiVuelta[i]+10}')
        else:
            print(f'Tiempo Vuelta[{i}]:{pmiVuelta[i]}')


def udf_mejor_vuelta(pmiVuelta,pCantVueltas):
    for i in range (0,pCantVueltas,1):
        if i==0:
            lvmejorvuelta=pmiVuelta[i]
            lvmejornumerovuelta=i
        else:
            if pmiVuelta[i]<lvmejorvuelta:
                lvmejorvuelta=pmiVuelta[i]
                lvmejornumerovuelta = i

    return  lvmejorvuelta, lvmejornumerovuelta


def udf_peor_vuelta(pmiVuelta,pCantVueltas):
    for i in range (0,pCantVueltas,1):
        if i==0:
            lvpeorvuelta=pmiVuelta[i]
            lvpeornumerovuelta=i
        else:
            if pmiVuelta[i]>lvpeorvuelta:
                lvpeorvuelta=pmiVuelta[i]
                lvpeornumerovuelta = i

    return  lvpeorvuelta, lvpeornumerovuelta


def udf_promedio_vueltas(pmiVuelta,pCantVueltas):
    lvsumavueltas=0
    for i in range (0,pCantVueltas,1):
        lvsumavueltas=lvsumavueltas+pmiVuelta[i]
    lvpromedio=lvsumavueltas/pCantVueltas
    return lvpromedio

def miMain():
    cant_vueltas=int(input("Ingrese la cantidad de vueltas:"))
    mivuelta = arr.array('i', [0] * cant_vueltas)
    while True:
        opcionrecibida=mi_menu()
        if opcionrecibida==1:
            udf_registra_vueltas(mivuelta, cant_vueltas)
        elif opcionrecibida==2:
            udf_informar_vuelta(mivuelta, cant_vueltas)
        elif opcionrecibida==3:
            mejorvuelta,mejornumerovuelta=udf_mejor_vuelta(mivuelta, cant_vueltas)
            print(f"La mejor vuelta es {mejorvuelta} en la vuelta {mejornumerovuelta}")
        elif opcionrecibida==4:
            peorvuelta,peornumerovuelta=udf_peor_vuelta(mivuelta, cant_vueltas)
            print(f"La peor vuelta es {peorvuelta} en la vuelta {peornumerovuelta}")
        elif opcionrecibida==5:
            promedio=udf_promedio_vueltas(mivuelta, cant_vueltas)
            print(f"El promedio de las vueltas es {promedio}")
        elif opcionrecibida==6:
            print("Adios")
            break
        else:
            print("Opcion Incorrecta 1-6 es lo que vale")


#Area global
miMain()

