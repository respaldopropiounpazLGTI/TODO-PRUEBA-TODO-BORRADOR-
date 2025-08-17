#encoding: utf-8
import array as arr

def udf_caragaAlumnos(plistaAlumnos,plistMaterias,parrNotas):
    for i in range(0,5,1):
        plistaAlumnos[i]=(input("Ingrese el nombre del alumno: "))
        plistMaterias[i]=(input("Ingrese la materia: "))
        parrNotas[i]=int(input("Ingrese la nota: "))

def udf_mostrarTodo(plistaAlumnos,plistMaterias,parrNotas):
    for i in range(0,5,1):
        print(f"Alumno: {plistaAlumnos[i]} Materia{plistMaterias[i]}, Notas{parrNotas[i]}")
        print("-------------------")

def udf_peor_nota(parrNotas):
    minimaNota=parrNotas[0]
    indice_peor=0
    for i in range(0,5,1):
        if parrNotas[i]<minimaNota:
            minimaNota=parrNotas[i]
            indice_peor=i
    return indice_peor

def udf_mejor_nota(parrNotas):
    maximaNota=parrNotas[0]
    indice_mejor=0
    for i in range(0,5,1):
        if parrNotas[i]>maximaNota:
            maximaNota=parrNotas[i]
            indice_mejor=i
    return indice_mejor
def udf_promedio_notas(parrNotas):
    sumatoria=0
    for i in range(0,5,1):
        sumatoria+=parrNotas[i]
    return sumatoria/5

def miMenu():
    print("1-Ingresar Alumnos")
    print("2-Mostrar Estadisticas")
    print("3-Listar todo")
    print("4-Salir")
    opcion=int(input("Ingrese una opcion: "))
    return opcion

def mimain():
    listaAlumnos=[""]*5
    listMaterias=[""]*5
    arrNotas=arr.array("i",[0]*5)
    cargado=False
    while True:
        opcion_recibida=miMenu()
        if opcion_recibida==1:
            udf_caragaAlumnos(listaAlumnos,listMaterias,arrNotas)
            cargado=True
        elif opcion_recibida==2:
            if not cargado:
                print("Primero debes cargar los datos")
            else:
                indice_peor_recibido=udf_peor_nota(arrNotas)
                print(f"El peor alumno es {listaAlumnos[indice_peor_recibido]} con la nota {arrNotas[indice_peor_recibido]}")
                indice_mejor_recibido=udf_mejor_nota(arrNotas)
                print(f"El mejor alumno es {listaAlumnos[indice_mejor_recibido]} con la nota {arrNotas[indice_mejor_recibido]}")
                print(f"El promedio de notas es {udf_promedio_notas(arrNotas)}")
        elif opcion_recibida==3:
            if not cargado:
                print("Primero debes cargar los datos")
            else:
                udf_mostrarTodo(listaAlumnos,listMaterias,arrNotas)

        else:
            print("Adios")
            break

#Programa Principal
mimain()