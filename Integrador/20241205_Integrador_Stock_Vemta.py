#ecoding: utf-8
import array as arr

def udf_dibujar_menu():
    print("\nMenú de Opciones")
    print("1. Registrar Ventas")
    print("2. Reportes de Ventas y Stock")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion

def udf_registrar_venta(arrstock, arrprecios, arrventas):
    indice = int(input("Ingrese el índice del producto (0 a 4): "))
    if indice >= 0 and indice <= 4:
        if arrstock[indice] == 0:
            print("No se pueden realizar más ventas para este producto. Stock agotado.")
            return
        else:
            cantidad = int(input("Ingrese la cantidad a vender: "))
            if cantidad > arrstock[indice]:
                print("Cantidad insuficiente en stock.")
            else:
                print(f"El producto {indice} tiene stock {arrstock[indice]} y va a quedar con {arrstock[indice]-cantidad}")
                arrstock[indice] = arrstock[indice] -cantidad # Restar la cantidad vendida al stock
                total_venta = cantidad * arrprecios[indice] # Calcular el total de la venta
                arrventas[indice] += total_venta
                print(f"Venta registrada. Total: ${total_venta:.2f}. Stock restante: {arrstock[indice]} unidades.")
    else:
        print("Producto inexistente.")

def udf_reportar_stock_ventas(arrstock, arrprecios, arrventas):
    print("\nReporte de Stock y Ventas:")
    print("{:<10} {:<10} {:<15} {:<15}".format("Producto", "Stock", "Ventas", "Precio Unitario"))
    for i in range(len(arrstock)):
        print("{:<10} {:<10} ${:<14.2f} ${:<14.2f}".format(i, arrstock[i], arrventas[i], arrprecios[i]))

def udf_main():
    # Inicialización de vectores
    arrstock = arr.array('i', [10, 20, 30, 40, 50])  # Stock inicial
    arrprecios = arr.array('f', [5.0, 10.0, 15.0, 20.0, 25.0])  # Precios por producto
    arrventas = arr.array('f', [0.0, 0.0, 0.0, 0.0, 0.0])  # Ventas iniciales

    while True:
        opcion = udf_dibujar_menu()
        if opcion == 1:
            udf_registrar_venta(arrstock, arrprecios, arrventas)
        elif opcion == 2:
            udf_reportar_stock_ventas(arrstock, arrprecios, arrventas)
        elif opcion == 3:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
udf_main()
