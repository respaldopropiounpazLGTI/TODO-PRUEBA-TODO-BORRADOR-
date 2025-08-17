import random # Necesitamos esto para generar cosas al azar, como contraseñas.
import string # Esto nos ayuda a trabajar con letras, números y símbolos para las contraseñas.
import time   # Esto nos permite hacer pausas en el programa, como para los bloqueos.

# --- Estructura de Datos para el Catálogo de Productos ---
# Aquí definimos cómo se verán nuestros productos. Usamos un "diccionario"
# para cada categoría, y dentro de ellos, más diccionarios para cada producto.
# Es como tener estantes (categorías) y en cada estante, cajas con información de cada producto.
catalogo_productos = {
    "Televisores": {
        "TV Smart 4K Samsung": {"precio": 500.00, "disponibilidad": 10, "descripcion": "Smart TV 4K de alta resolución.", "categoria": "Televisores"},
        "TV OLED LG Curvo": {"precio": 1200.00, "disponibilidad": 5, "descripcion": "Pantalla curva OLED para una inmersión total.", "categoria": "Televisores"}
    },
    "Celulares": {
        "Smartphone Galaxy A52": {"precio": 300.00, "disponibilidad": 20, "descripcion": "Teléfono de gama media con buena cámara.", "categoria": "Celulares"},
        "iPhone 15 Pro": {"precio": 1000.00, "disponibilidad": 15, "descripcion": "Lo último en tecnología móvil de Apple.", "categoria": "Celulares"}
    },
    "Computadoras": {
        "Notebook HP Pavilion": {"precio": 750.00, "disponibilidad": 8, "descripcion": "Laptop potente para trabajo y estudio.", "categoria": "Computadoras"},
        "PC Escritorio Gamer": {"precio": 1500.00, "disponibilidad": 3, "descripcion": "Computadora de alto rendimiento para juegos.", "categoria": "Computadoras"}
    },
    "Accesorios de informática": {
        "Teclado Mecánico RGB": {"precio": 70.00, "disponibilidad": 30, "descripcion": "Teclado con retroiluminación personalizable.", "categoria": "Accesorios de informática"},
        "Mouse Inalámbrico Logitech": {"precio": 25.00, "disponibilidad": 50, "descripcion": "Mouse ergonómico para uso diario.", "categoria": "Accesorios de informática"}
    },
    "Electrodomésticos pequeños": {
        "Microondas Atma 20L": {"precio": 90.00, "disponibilidad": 12, "descripcion": "Microondas compacto para calentar y cocinar.", "categoria": "Electrodomésticos pequeños"},
        "Licuadora Philips": {"precio": 50.00, "disponibilidad": 18, "descripcion": "Potente licuadora para preparar batidos.", "categoria": "Electrodomésticos pequeños"}
    },
    "Electrodomésticos grandes": {
        "Heladera No Frost": {"precio": 800.00, "disponibilidad": 7, "descripcion": "Refrigerador espacioso con tecnología No Frost.", "categoria": "Electrodomésticos grandes"},
        "Lavarropas Automático": {"precio": 600.00, "disponibilidad": 9, "descripcion": "Lavarropas de carga frontal con múltiples programas.", "categoria": "Electrodomésticos grandes"}
    },
    "Audio y sonido": {
        "Auriculares Bluetooth Sony": {"precio": 80.00, "disponibilidad": 25, "descripcion": "Auriculares inalámbricos con excelente sonido.", "categoria": "Audio y sonido"},
        "Parlante JBL Portátil": {"precio": 120.00, "disponibilidad": 15, "descripcion": "Parlante a prueba de agua con gran autonomía.", "categoria": "Audio y sonido"}
    },
    "Gaming": {
        "Consola PlayStation 5": {"precio": 700.00, "disponibilidad": 6, "descripcion": "La última consola de Sony para una experiencia inmersiva.", "categoria": "Gaming"},
        "Mando Xbox Series X": {"precio": 60.00, "disponibilidad": 20, "descripcion": "Control inalámbrico para consolas Xbox.", "categoria": "Gaming"}
    },
    "Cámaras y fotografía": {
        "Cámara Digital Canon": {"precio": 400.00, "disponibilidad": 10, "descripcion": "Cámara compacta ideal para principiantes.", "categoria": "Cámaras y fotografía"},
        "Drone DJI Mini": {"precio": 350.00, "disponibilidad": 5, "descripcion": "Drone ligero con cámara HD.", "categoria": "Cámaras y fotografía"}
    }
}

# --- Variable global para el carrito de compras ---
# Aquí guardaremos los productos que el usuario elija. Es como la canasta de compras.
carrito_de_compras = {}

# --- Funciones Auxiliares (pequeñas herramientas que nos ayudan) ---

def limpiar_pantalla():
    """Simula una limpieza de pantalla para mejorar la visualización en la consola."""
    # Esto es una forma simple de "limpiar" la consola. En programas más complejos,
    # se usarían librerías específicas para una limpieza real.
    print("\n" * 50) # Imprime 50 líneas en blanco para "borrar" lo anterior.

def validar_entrada_alfanumerica(mensaje, intentos_maximos=5):
    """
    Valida que la entrada del usuario solo contenga caracteres alfanuméricos y permitidos.
    Tiene un límite de intentos y un bloqueo temporal si se excede.
    """
    intentos = 0
    while intentos < intentos_maximos:
        entrada = input(mensaje)
        # Aquí definimos los caracteres que SÍ están permitidos.
        # Es como decir: "solo acepto letras, números y estos símbolos".
        caracteres_permitidos = string.ascii_letters + string.digits + " " + "!@#$%^&*()_+-=[]{};:,./<>?\|`~"
        
        # Comprobamos si todos los caracteres de la entrada están en nuestra lista de permitidos.
        if all(c in caracteres_permitidos for c in entrada):
            return entrada # Si es válida, la devolvemos.
        else:
            intentos += 1
            print(f"ERROR: Entrada inválida. Solo se permiten caracteres alfanuméricos y símbolos específicos. Intento ({intentos}) de ({intentos_maximos}).")
    
    print(f"\n¡Se ha superado el límite de {intentos_maximos} intentos. Bloqueo temporal por 1 minuto!")
    time.sleep(60)
    return None # Si se bloquea, no devuelve nada.

def validar_cantidad_positiva_entera(mensaje, intentos_maximos=5):
    """
    Valida que la cantidad ingresada sea un número entero positivo.
    Tiene un límite de intentos y un bloqueo temporal.
    """
    intentos = 0
    while intentos < intentos_maximos:
        try:
            cantidad_str = input(mensaje)
            cantidad = int(cantidad_str) # Intentamos convertir lo que el usuario escribió a un número entero.
            if cantidad > 0: # Verificamos que sea mayor que cero (positivo).
                return cantidad # Si es válido, lo devolvemos.
            else:
                intentos += 1
                print(f"ERROR: La cantidad debe ser un número entero positivo. Intento ({intentos}) de ({intentos_maximos}).")
        except ValueError: # Si el usuario no escribió un número, ocurre un error (ValueError).
            intentos += 1
            print(f"ERROR: Por favor, ingrese un número entero válido. Intento ({intentos}) de ({intentos_maximos}).")
    
    print(f"\n¡Se ha superado el límite de {intentos_maximos} intentos. Bloqueo temporal por 1 minuto!")
    time.sleep(60)
    return None # Si se bloquea, no devuelve nada.

# --- Parte 1: Ingreso Seguro al Sistema (Login) ---

def generar_contraseña(longitud=10):
    """
    Genera una contraseña aleatoria y segura usando letras, números y símbolos.
    """
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()_+-=<>?"
    return "".join(random.choice(caracteres) for _ in range(longitud))

def login():
    """
    Gestiona el proceso de inicio de sesión con contraseña generada aleatoriamente
    y control de intentos fallidos.
    """
    contraseña_sistema = generar_contraseña()
    print("\n--- Bienvenido al sistema de gestión de ElectroSmart ---")
    print(f"Su contraseña temporal es: {contraseña_sistema}") # Le mostramos al usuario la contraseña generada.
    print("\nPor favor, ingrese la contraseña para continuar (máximo 5 intentos):")

    intentos = 0
    max_intentos = 5

    while intentos < max_intentos:
        ingreso_usuario = input("Ingrese la contraseña: ")
        if ingreso_usuario == contraseña_sistema:
            print("Acceso concedido. ¡Bienvenido al sistema!")
            return True # El inicio de sesión fue exitoso.
        else:
            intentos += 1
            print(f"X Contraseña incorrecta. Intento ({intentos}) de ({max_intentos}).")
    
    # Si se llega aquí, el usuario superó los intentos.
    print("\n¡Se han superado los intentos permitidos. Usuario bloqueado por 60 segundos!")
    time.sleep(60)
    print("\nIntente iniciar sesión nuevamente.")
    return login() # Vuelve a llamar a la función login para que intente de nuevo.

# --- Parte 2: Visualización del Catálogo ---

def visualizar_catalogo():
    """
    Muestra todos los productos organizados por categoría.
    Incluye nombre, categoría, precio, disponibilidad y descripción.
    """
    print("\n--- Catálogo de Productos ElectroSmart ---")
    for categoria, productos in catalogo_productos.items():
        print(f"\n--- Categoría: {categoria} ---") # Muestra el nombre de la categoría.
        if not productos:
            print("    No hay productos en esta categoría.")
            continue
        for nombre_producto, info_producto in productos.items():
            # Muestra los detalles de cada producto.
            print(f"  - Nombre: {nombre_producto}")
            print(f"    Categoría: {info_producto['categoria']}")
            print(f"    Precio: ${info_producto['precio']:.2f}") # Formatea el precio con 2 decimales.
            print(f"    Disponibilidad: {info_producto['disponibilidad']} unidades")
            print(f"    Descripción: {info_producto['descripcion']}")
            print("-" * 30) # Una línea para separar los productos.

# --- Parte 3: Agregar Productos al Carrito ---

def agregar_al_carrito():
    """
    Permite al usuario seleccionar productos del catálogo y agregarlos al carrito.
    Valida la existencia del producto y la cantidad.
    """
    print("\n--- Agregar Productos al Carrito ---")
    visualizar_catalogo() # Primero, mostramos el catálogo para que el usuario sepa qué elegir.

    # Pedimos al usuario el nombre del producto que quiere.
    nombre_producto_elegido = validar_entrada_alfanumerica("Ingrese el nombre exacto del producto que desea agregar: ")
    if nombre_producto_elegido is None:
        print("Volviendo al menú principal debido a demasiados intentos fallidos.")
        return # Si hay bloqueo, volvemos al menú.

    # Buscamos el producto en todo el catálogo.
    producto_encontrado = None
    info_producto_encontrado = None
    for categoria, productos in catalogo_productos.items():
        if nombre_producto_elegido in productos:
            producto_encontrado = nombre_producto_elegido
            info_producto_encontrado = productos[nombre_producto_elegido]
            break # Una vez que lo encontramos, salimos del bucle.

    if producto_encontrado is None:
        print("X El producto ingresado no se encuentra en el catálogo. Por favor, intente con el nombre exacto.")
        # Aquí podríamos implementar el bloqueo por 5 intentos como se indica en el documento.
        # Para simplificar este ejemplo, solo avisamos y volvemos.
        return

    print(f"Producto seleccionado: {producto_encontrado} (Disponibles: {info_producto_encontrado['disponibilidad']})")
    
    # Pedimos la cantidad deseada.
    cantidad_deseada = validar_cantidad_positiva_entera("Ingrese la cantidad que desea agregar: ")
    if cantidad_deseada is None:
        print("Volviendo al menú principal debido a demasiados intentos fallidos.")
        return # Si hay bloqueo, volvemos al menú.

    # Validamos que haya suficiente stock.
    if cantidad_deseada > info_producto_encontrado['disponibilidad']:
        print(f"X Lo sentimos, solo quedan {info_producto_encontrado['disponibilidad']} unidades disponibles de {producto_encontrado}.")
        return

    # Si todo es válido, agregamos o actualizamos el producto en el carrito.
    if producto_encontrado in carrito_de_compras:
        carrito_de_compras[producto_encontrado]['cantidad'] += cantidad_deseada
    else:
        # Copiamos la información del producto y agregamos la cantidad.
        carrito_de_compras[producto_encontrado] = info_producto_encontrado.copy()
        carrito_de_compras[producto_encontrado]['cantidad'] = cantidad_deseada
    
    # Reducimos la disponibilidad del producto en el catálogo.
    info_producto_encontrado['disponibilidad'] -= cantidad_deseada

    print(f"'{cantidad_deseada}' unidades de '{producto_encontrado}' agregadas al carrito exitosamente.")

# --- Parte 4: Ver Productos en el Carrito ---

def ver_carrito():
    """
    Muestra la lista de productos que el usuario ha agregado al carrito.
    Incluye detalles como nombre, categoría, precio unitario, cantidad y subtotal.
    """
    print("\n--- Su Carrito de Compras ---")
    if not carrito_de_compras:
        print("Su carrito está vacío. ¡Explore nuestro catálogo y agregue productos!")
        return

    total_general = 0.0 # Variable para calcular el costo total del carrito.
    for nombre_producto, info_en_carrito in carrito_de_compras.items():
        precio_unitario = info_en_carrito['precio']
        cantidad = info_en_carrito['cantidad']
        subtotal = precio_unitario * cantidad # Calculamos el subtotal de cada producto.
        total_general += subtotal # Sumamos al total general.

        print(f"  - Producto: {nombre_producto}")
        print(f"    Categoría: {info_en_carrito['categoria']}")
        print(f"    Precio Unitario: ${precio_unitario:.2f}")
        print(f"    Cantidad: {cantidad}")
        print(f"    Subtotal: ${subtotal:.2f}")
        print("-" * 30)
    
    print(f"\n--- Total a Pagar en Carrito: ${total_general:.2f} ---")

# --- Parte 5: Eliminar Productos del Carrito ---

def eliminar_del_carrito():
    """
    Permite al usuario eliminar productos del carrito.
    Solicita confirmación antes de eliminar.
    """
    print("\n--- Eliminar Productos del Carrito ---")
    if not carrito_de_compras:
        print("Su carrito está vacío, no hay productos para eliminar.")
        return

    ver_carrito() # Mostramos el carrito para que el usuario vea qué puede eliminar.

    # Pedimos el nombre del producto a eliminar.
    nombre_producto_a_eliminar = validar_entrada_alfanumerica("Ingrese el nombre exacto del producto a eliminar del carrito: ")
    if nombre_producto_a_eliminar is None:
        print("Volviendo al menú principal debido a demasiados intentos fallidos.")
        return

    if nombre_producto_a_eliminar not in carrito_de_compras:
        print("X El producto ingresado no se encuentra en su carrito.")
        return

    # Solicitamos confirmación.
    confirmacion = input(f"¿Está seguro de que desea eliminar '{nombre_producto_a_eliminar}' del carrito? (sí/no): ").lower()
    if confirmacion == 'si' or confirmacion == 'sí':
        # Devolvemos la cantidad al stock del catálogo.
        cantidad_a_devolver = carrito_de_compras[nombre_producto_a_eliminar]['cantidad']
        categoria_producto = carrito_de_compras[nombre_producto_a_eliminar]['categoria']
        
        # Incrementamos la disponibilidad en el catalogo_productos.
        catalogo_productos[categoria_producto][nombre_producto_a_eliminar]['disponibilidad'] += cantidad_a_devolver

        del carrito_de_compras[nombre_producto_a_eliminar] # Eliminamos el producto del carrito.
        print(f"'{nombre_producto_a_eliminar}' ha sido eliminado de su carrito.")
    else:
        print("Operación cancelada. El producto no fue eliminado.")

# --- Parte 6: Finalizar la Compra ---

def finalizar_compra():
    """
    Permite al usuario finalizar la compra y proceder al pago.
    Gestiona los diferentes métodos de pago y sus recargos.
    No permite finalizar la compra si el carrito está vacío.
    """
    print("\n--- Finalizar Compra ---")
    if not carrito_de_compras:
        print("Su carrito está vacío. No puede finalizar la compra sin productos.")
        return

    ver_carrito() # Mostramos el resumen del carrito antes de finalizar.
    
    total_a_pagar = sum(item['precio'] * item['cantidad'] for item in carrito_de_compras.values())

    print(f"\nEl total de su compra es: ${total_a_pagar:.2f}")

    print("\nSeleccione un medio de pago:")
    print("1. Efectivo")
    print("2. Tarjeta de crédito")
    print("3. Bitcoin")

    opcion_pago = validar_cantidad_positiva_entera("Ingrese el número de la opción de pago: ")
    if opcion_pago is None:
        print("Volviendo al menú principal debido a demasiados intentos fallidos.")
        return

    monto_final = total_a_pagar

    if opcion_pago == 1:
        print(f"\nHa elegido pagar en Efectivo. El monto final es: ${monto_final:.2f}")
    elif opcion_pago == 2:
        print("\nHa elegido pagar con Tarjeta de crédito.")
        print("Seleccione un plan de cuotas:")
        print("1. 3 cuotas (12% de recargo)")
        print("2. 6 cuotas (18% de recargo)")
        print("3. 12 cuotas (36% de recargo)")

        opcion_cuotas = validar_cantidad_positiva_entera("Ingrese el número de la opción de cuotas: ")
        if opcion_cuotas is None:
            print("Volviendo al menú principal debido a demasiados intentos fallidos.")
            return

        recargo = 0
        if opcion_cuotas == 1:
            recargo = 0.12 # 12%
        elif opcion_cuotas == 2:
            recargo = 0.18 # 18%
        elif opcion_cuotas == 3:
            recargo = 0.36 # 36%
        else:
            print("Opción de cuotas inválida. Se aplicará el precio sin recargo.")
        
        monto_final *= (1 + recargo) # Calculamos el monto con el recargo.
        print(f"\nMonto final con recargo por cuotas: ${monto_final:.2f}")

    elif opcion_pago == 3:
        print(f"\nHa elegido pagar con Bitcoin. El monto final es: ${monto_final:.2f}")
    else:
        print("Opción de pago inválida. Por favor, seleccione una opción válida.")
        return

    print("\n--- ¡Compra finalizada con éxito! ---")
    print(f"El monto total cobrado es: ${monto_final:.2f}")
    
    # Vaciamos el carrito después de la compra.
    carrito_de_compras.clear()
    print("Su carrito ha sido vaciado.")

# --- Menú Principal del Sistema ---

def menu_principal():
    """
    Muestra el menú principal de opciones del software de gestión y
    dirige al usuario a las diferentes funcionalidades.
    """
    while True: # Este bucle hace que el menú se muestre una y otra vez hasta que el usuario elija salir.
        limpiar_pantalla() # Para que el menú se vea siempre limpio.
        print("\n--- Menú Principal de ElectroSmart ---")
        print("1. Ver Catálogo de Productos")
        print("2. Agregar Productos al Carrito")
        print("3. Ver Carrito de Compras")
        print("4. Eliminar Productos del Carrito")
        print("5. Finalizar Compra")
        print("6. Salir del Sistema")

        opcion = validar_cantidad_positiva_entera("Ingrese el número de la opción deseada: ")
        if opcion is None:
            continue # Si hay un bloqueo en la entrada, volvemos a mostrar el menú.

        if opcion == 1:
            visualizar_catalogo()
            input("\nPresione Enter para continuar...") # Pausa para que el usuario pueda leer.
        elif opcion == 2:
            agregar_al_carrito()
            input("\nPresione Enter para continuar...")
        elif opcion == 3:
            ver_carrito()
            input("\nPresione Enter para continuar...")
        elif opcion == 4:
            eliminar_del_carrito()
            input("\nPresione Enter para continuar...")
        elif opcion == 5:
            finalizar_compra()
            input("\nPresione Enter para continuar...")
        elif opcion == 6:
            print("\nGracias por usar el sistema de ElectroSmart. ¡Hasta pronto!")
            break # Sale del bucle, terminando el programa.
        else:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 6.")
            input("\nPresione Enter para continuar...")

# --- Inicio del Programa ---
# Esta es la parte que "enciende" todo el software.
if __name__ == "__main__":
    # Primero, intentamos iniciar sesión. Si el login es exitoso, procedemos al menú principal.
    if login():
        menu_principal()
