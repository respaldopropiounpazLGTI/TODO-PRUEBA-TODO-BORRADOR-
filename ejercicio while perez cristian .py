# El programa usará un nombre de usuario y contraseña predefinidos (puedes simular una cuenta con valores como "usuario" y "clave123").
usuario_ya_registrado="usuario"
clave_usuario_ya_registrado="clave123"
intentos=0
nueva_cuenta=""
#Escriba un programa que simule un sistema de registro e inicio de sesión para un usuario. El programa debe funcionar de la siguiente manera:
# Al iniciar, debe preguntar al usuario si ya está registrado (sí o no).
 # Luego, debe iniciar sesión con los datos recién ingresados.
 # Si el usuario ya está registrado:
 # Si el usuario no está registrado:
# Se le debe permitir crear un nombre de usuario y una contraseña.
#el usuario tiene 3 intentos para ingresar correctamente el nombre de usuario y la contraseña.
# Si los datos son correctos, debe mostrarse un mensaje de bienvenida.
# Si se agotan los 3 intentos sin éxito, debe mostrarse un mensaje de acceso denegado.
print("BIENVENIDO AL SISTEMA ")
print("")
pregunta=input("USTED ESTA REGISTRADO?").lower()
print("")
if pregunta=="no":nueva_cuenta=input("DESEA USTED REGISTRARSE ? ").lower()
if nueva_cuenta=="si":
    cuenta_nuevo_usuario=input("POR FAVOR INGRESE UN NOMBRE DE USUARIO PARA SU NUEVA CUENTA ").lower()
    clave_nuevo_usuario=input("POR FAVOR  INGRESE UNA CLAVE PARA SU NUEVO  USUARIO  ").lower()
    print("")
    print("*** BIENVENDIO NUEVO USUARIO !!! SE LE PEDIRA QUE INGRESE SU USUARIO Y CLAVE PARA INICIAR SECCION *** ")
    print("*** USTED TIENE 3 INTENTOS *** ")
    intentos=0
    while intentos<3:
        validacion_nuevo_usuario=input("por favor ingrese su nombre de usuario recien creado :").lower()
        validacion_nueva_clave=input("por favor ingrese su contraseña recien creado :").lower()
        if validacion_nuevo_usuario==clave_nuevo_usuario and validacion_nueva_clave==clave_nuevo_usuario:
            print("BIENVENIDO NUEVO USUARIO ",cuenta_nuevo_usuario,"!!!")
            break
        else:
         intentos+=1
         resta_de_intentos=3-intentos 
         print(" CLAVE O CONTRASEÑAS ENCORRECTOS POR FAVOR VUELVA A INTENTARLO SOLO TIENE ",resta_de_intentos," INTENTOS ")
         if intentos==3:
            print(" acceso denegado ") 
            break
elif pregunta=="si":
   print("BIENVENIDO USUARIO REGISTRADO ")
   intentos_usuario_ya_registrado=0
   print("a continuacion se le pedira su usuario y contraseña usted tiene 3 intentos en total !!! ")
   while intentos_usuario_ya_registrado<3:
    cuenta_ya_registrada=input("por favor ingrese su usuario resgitrado : ").lower()
    clave_para_usuario_ya_registrado=input("por favor ingrese su clave de usuario registrado : ").lower()
    if cuenta_ya_registrada==usuario_ya_registrado and clave_para_usuario_ya_registrado==clave_usuario_ya_registrado:
       print("BIENVENIDO AL SISTEMA USUARIO ",usuario_ya_registrado)
       print(" QUE TENGA UN BUEN DIA !!! ")
       break
    else:
       intentos_usuario_ya_registrado+=1
       resta_para_intentos=3-intentos_usuario_ya_registrado
       print("usuario o contraseña equivocadas ")
       print(" le quedan ",resta_para_intentos,"intentos ")
       if   intentos_usuario_ya_registrado==3:
          print("acceso denegado  ")
else:print(" gracias por utilzar el programa  adios !!! ")          
 
 






 
 
 
 
        
    



    



