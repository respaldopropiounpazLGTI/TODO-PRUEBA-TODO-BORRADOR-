#TRABAJO INTEGRADOR INTRODUCCION A LA PROGRAMACION 1 COMISION B1 PROFESOR :SERGIO EDUARDO TORRE
# INTEGRANTES:
#GONZALO TOMAS ARTAZA
#AARON LAUTARO BENJAMIN ROLON
#PEREZ CRISTIAN ALEJANDRO           
#inporta librerias para realizar el algoritmo 
import time  # Módulo para funciones relacionadas con el tiempo (ej. sleep)
import random  # Módulo para generar números aleatorios
import string  # Módulo para manejar caracteres (letras, dígitos, etc.)

# Catálogo de productos organizado por categorías
catalogo = {
    # Cada categoría tiene una lista de diccionarios, cada uno representando un producto
    "Televisores": [
        {"nombre": "Smart TV 55", "precio": 295, "disponible": 5, "descripcion": "Televisor inteligente con resolución 4K"},
        {"nombre": "LED 32", "precio": 126, "disponible": 4, "descripcion": "Televisor LED de 32 pulgadas"},
        {"nombre": "OLED 65", "precio": 421, "disponible": 0, "descripcion": "Pantalla OLED con calidad de cine"},
    ],
    "Celulares": [
        {"nombre": "iPhone 14 Pro", "precio": 1010, "disponible": 3, "descripcion": "iPhone con cámara mejorada y chip A16"},
        {"nombre": "Samsung Galaxy A23", "precio": 295, "disponible": 5, "descripcion": "Celular gama media con buena autonomía"},
        {"nombre": "Motorola G82", "precio": 253, "disponible": 0, "descripcion": "Pantalla OLED y sonido estéreo"},
    ],
    "Computadoras": [
        {"nombre": "Notebook", "precio": 379, "disponible": 1, "descripcion": "Notebook liviana y potente para uso diario"},
        {"nombre": "PC de escritorio", "precio": 463, "disponible": 2, "descripcion": "Computadora para oficina y gaming"},
        {"nombre": "iMac", "precio": 1010, "disponible": 0, "descripcion": "Todo en uno de Apple con gran rendimiento"},
    ],
    "Accesorios de informática": [
        {"nombre": "Teclado mecánico", "precio": 29, "disponible": 5 , "descripcion": "Teclado retroiluminado para gamers"},
        {"nombre": "Mouse inalámbrico", "precio": 17, "disponible": 10, "descripcion": "Mouse ergonómico sin cables"},
        {"nombre": "Parlantes", "precio": 38, "disponible": 0, "descripcion": "Parlantes estéreo con buen bajo"},
    ],
    "Electrodomésticos pequeños": [
        {"nombre": "Microondas", "precio": 67, "disponible": 8, "descripcion": "Microondas digital con grill"},
        {"nombre": "Licuadora", "precio": 25, "disponible": 9, "descripcion": "Licuadora de 1.5L con motor potente"},
        {"nombre": "Tostadora", "precio": 21, "disponible": 6, "descripcion": "Tostadora para 2 rebanadas"},
        {"nombre": "Pava eléctrica", "precio": 15, "disponible": 5, "descripcion": "Pava eléctrica con corte automático"},
        {"nombre": "Cafetera", "precio": 34, "disponible": 0, "descripcion": "Cafetera programable para 12 tazas"},
    ],
    "Electrodomésticos grandes": [
        {"nombre": "Heladera", "precio": 505, "disponible": 4, "descripcion": "Heladera no frost con freezer"},
        {"nombre": "Lavarropas", "precio": 421, "disponible": 8, "descripcion": "Lavarropas automático con múltiples programas"},
        {"nombre": "Cocina", "precio": 353, "disponible": 0, "descripcion": "Cocina a gas con horno autolimpiante"},
        {"nombre": "Horno eléctrico", "precio": 50, "disponible": 9, "descripcion": "Horno eléctrico de 50 litros"},
        {"nombre": "Lavavajillas", "precio": 589, "disponible": 0, "descripcion": "Lavavajillas con 6 programas"},
    ],
    "Audio y sonido": [
        {"nombre": "Auriculares inalámbricos", "precio": 29, "disponible": 12, "descripcion": "Auriculares con cancelación de ruido"},
        {"nombre": "Parlante Bluetooth", "precio": 38, "disponible": 5, "descripcion": "Parlante portátil resistente al agua"},
        {"nombre": "Equipo de sonido", "precio": 136, "disponible": 5, "descripcion": "Equipo con subwoofer y bluetooth"},
    ],
    "Gaming": [
        {"nombre": "PlayStation 5", "precio": 757, "disponible": 11, "descripcion": "Consola de nueva generación de Sony"},
        {"nombre": "Xbox Series X", "precio": 716, "disponible": 0, "descripcion": "Consola potente de Microsoft"},
        {"nombre": "Nintendo Switch", "precio": 505, "disponible": 9, "descripcion": "Consola híbrida para jugar en cualquier lado"},
    ],
    "Cámaras y fotografía": [
        {"nombre": "Cámara digital", "precio": 168, "disponible": 7, "descripcion": "Cámara compacta con zoom óptico"},
        {"nombre": "Cámara profesional", "precio": 716, "disponible": 0, "descripcion": "Reflex para fotógrafos avanzados"},
    ]
}

# Carrito de compras: diccionario global que almacena los productos seleccionados por el usuario
carrito_de_compras = {}

# Simula limpiar la pantalla imprimiendo líneas en blanco
def limpiar_pantalla():
    print("\n" * 1)

# Valida que la cantidad ingresada sea un entero positivo
def validar_cantidad_positiva_entera(mensaje, intentos_maximos=5):
    intentos = 0
    while intentos < intentos_maximos:
        cantidad_str = input(mensaje)
        if cantidad_str.isdigit() and int(cantidad_str) > 0:
            return int(cantidad_str)
        else:
            intentos += 1
            print(f"La cantidad debe ser un número entero positivo. Intento ({intentos}) de ({intentos_maximos}).")
    print("Demasiados intentos. Esperando 60 segundos...")
    time.sleep(60)
    return None

# Valida que el usuario ingrese una cadena no vacía
def validar_entrada_alfanumerica(mensaje, intentos_maximos=5):
    intentos = 0
    while intentos < intentos_maximos:
        entrada = input(mensaje).strip()
        if entrada:
            return entrada
        else:
            intentos += 1
            print(f"La entrada no puede estar vacía. Intento ({intentos}) de ({intentos_maximos}).")
    print("Demasiados intentos. Esperando 60 segundos...")
    time.sleep(60)
    return None

# Genera una contraseña aleatoria segura
def generar_contraseña(longitud=8):
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()_+-=<>?"
    return ''.join(random.choice(caracteres) for _ in range(longitud))

# Proceso de login con generación de contraseña temporal
def login():
    contraseña_sistema = generar_contraseña()
    print("Bienvenido al sistema de ElectroSmart")
    print("Su contraseña temporal es:", contraseña_sistema)
    intentos = 0
    while intentos < 5:
        ingreso = input("Ingrese la contraseña: ")
        if ingreso == contraseña_sistema:
            print("Acceso concedido.")
            return True
        else:
            intentos += 1
            print(f"Incorrecta. Intento {intentos}/5")
    print("Bloqueado por 60 segundos.")
    time.sleep(60)
    return login()

# Muestra el catálogo completo con nombre, precio, stock y descripción
def visualizar_catalogo():
    print("\n--- Catálogo ---")
    for categoria, productos in catalogo.items():
        print(f"\nCategoría: {categoria}")
        for producto in productos:
            print(f"- {producto['nombre']} | Precio: ${producto['precio']} | Stock: {producto['disponible']} | {producto['descripcion']}")

# Agrega productos al carrito si están disponibles
def agregar_al_carrito():
    print("\n--- Agregar al Carrito ---")
    nombre = validar_entrada_alfanumerica("¿Qué producto desea agregar?: ")
    if nombre is None:
        return
    for categoria, productos in catalogo.items():
        for producto in productos:
            if producto["nombre"].lower() == nombre.lower():
                if producto["disponible"] == 0:
                    print("Sin stock.")
                    return
                cantidad = validar_cantidad_positiva_entera("Cantidad: ")
                if cantidad is None:
                    return
                if cantidad > producto["disponible"]:
                    print(f"Solo hay {producto['disponible']} disponibles.")
                    return
                if nombre in carrito_de_compras:
                    carrito_de_compras[nombre]['cantidad'] += cantidad
                else:
                    carrito_de_compras[nombre] = {
                        "precio": producto["precio"],
                        "cantidad": cantidad,
                        "categoria": categoria,
                        "descripcion": producto["descripcion"]
                    }
                producto["disponible"] -= cantidad
                print(f"{cantidad} x {nombre} agregado al carrito.")
                return
    print("Producto no encontrado.")

# Muestra el contenido actual del carrito con el total acumulado
def ver_carrito():
    print("\n--- Carrito ---")
    if not carrito_de_compras:
        print("Carrito vacío.")
        return
    total = 0
    for nombre, info in carrito_de_compras.items():
        subtotal = info["precio"] * info["cantidad"]
        total += subtotal
        print(f"{nombre} ({info['cantidad']} x ${info['precio']}) = ${subtotal}")
    print(f"Total: ${total:.2f}")

# Elimina un producto específico del carrito y actualiza el stock
def eliminar_del_carrito():
    print("\n--- Eliminar Producto ---")
    if not carrito_de_compras:
        print("Carrito vacío.")
        return
    ver_carrito()
    nombre = validar_entrada_alfanumerica("Nombre exacto del producto a eliminar: ")
    if nombre is None or nombre not in carrito_de_compras:
        print("Producto no está en el carrito.")
        return
    confirmacion = input(f"¿Eliminar '{nombre}'? (si/no): ").lower()
    if confirmacion in ['si', 'sí']:
        cantidad = carrito_de_compras[nombre]["cantidad"]
        categoria = carrito_de_compras[nombre]["categoria"]
        for producto in catalogo[categoria]:
            if producto["nombre"] == nombre:
                producto["disponible"] += cantidad
                break
        carrito_de_compras.pop(nombre)
        print(f"{nombre} eliminado del carrito.")
    else:
        print("Eliminación cancelada.")

# Finaliza la compra y ofrece métodos de pago con cálculo de recargos
def finalizar_compra():
    print("\n--- Finalizar Compra ---")
    if not carrito_de_compras:
        print("Su carrito está vacío. No puede finalizar la compra.")
        return
    
    ver_carrito()
    total = sum(item["precio"] * item["cantidad"] for item in carrito_de_compras.values())
    print(f"\nTotal a pagar: ${total:.2f}")
    
    print("\nSeleccione un medio de pago:")
    print("1. Efectivo")
    print("2. Tarjeta de crédito")
    print("3. Bitcoin")

    metodo = validar_cantidad_positiva_entera("Ingrese opción (1-3): ")
    if metodo is None:
        print("Volviendo al menú principal.")
        return

    monto_final = total

    if metodo == 1:
        print(f"\nElegiste Efectivo. Total a pagar: ${monto_final:.2f}")
    elif metodo == 2:
        print("\nElegiste Tarjeta. Elija plan de cuotas:")
        print("1. 1 o 3 cuotas (12% recargo)")
        print("2. 6 cuotas (18% recargo)")
        print("3. 12 cuotas (36% recargo)")

        cuotas = validar_cantidad_positiva_entera("Opción de cuotas (1-3): ")
        if cuotas is None:
            print("Volviendo al menú principal.")
            return

        recargo = 0
        if cuotas == 1:
            recargo = 0.12
        elif cuotas == 2:
            recargo = 0.18
        elif cuotas == 3:
            recargo = 0.36
        else:
            print("Opción no válida. Se asume sin recargo.")

        monto_final *= (1 + recargo)
        print(f"Monto final con recargo: ${monto_final:.2f}")
    elif metodo == 3:
        print(f"\nElegiste Bitcoin. Total a pagar: ${monto_final:.2f}")
    else:
        print("Opción inválida.")
        return

    print("\nCompra realizada con éxito.")
    print(f"Total cobrado: ${monto_final:.2f}")
    carrito_de_compras.clear()
    print("El carrito ha sido vaciado.")

# Muestra el menú principal del sistema y llama a las funciones según la elección
def menu_principal():
    while True:
        limpiar_pantalla()
        print("=== Menú ElectroSmart ===")
        print("1. Ver Catálogo")
        print("2. Agregar al Carrito")
        print("3. Ver Carrito")
        print("4. Eliminar del Carrito")
        print("5. Finalizar Compra")
        print("6. Salir")

        opcion = validar_cantidad_positiva_entera("Opción: ")

        if opcion is None:
            print("Reintentando login...")
            if not login():
                break
        elif opcion == 1:
            visualizar_catalogo()
        elif opcion == 2:
            agregar_al_carrito()
        elif opcion == 3:
            ver_carrito()
        elif opcion == 4:
            eliminar_del_carrito()
        elif opcion == 5:
            finalizar_compra()
        elif opcion == 6:
            print("Gracias por usar ElectroSmart.")
            break
        else:
            print("Opción inválida.")
# Punto de inicio del programa
if __name__ == "__main__":
    if login():
        menu_principal()
