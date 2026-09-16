# Ejercicio 2  — “Acceso al Campus y Menú Seguro” 
# Objetivo: Login con intentos + menú de acciones con validación estricta. 
# Requisitos 
# 1. Definir credenciales fijas en el código: 
#   -usuario correcto: "alumno" 
#   -clave correcta: "python123" 

# 2. Permitir máximo 3 intentos para ingresar usuario y clave. 

# 3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar. 

# 4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir: 
#     1. Ver estado de inscripción (mostrar “Inscripto”) 
#     2. Cambiar clave (pedir nueva clave y confirmación; deben 
#     coincidir) 
#     3. Mostrar mensaje motivacional (1 frase) 
#     4. Salir 
# 5. Validación del menú: 
#   -Debe ser número (.isdigit()) 
#   -Debe estar entre 1 y 4 
# Cambio de clave 
# • La nueva clave debe tener mínimo 7 caracteres (validar con len()), si no, 
# rechazar.

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

# hacemos un contador para limitar la cantidad de intentos

while intentos < 3:
    print(f"\nintento {intentos + 1}/3")
    login_user = input("usuario: ").strip()
    login_clave = input("clave: ").strip()

    # verifica que el usuario y la clave sean correctos
    if login_user == usuario_correcto and login_clave == clave_correcta:
        acceso = True
        print("acceso concedido.")
        break

    else:
        intentos += 1
        print("error: credenciales invalidas.")

# si no pudo acceder despues de los 3 intentos, bloquea la cuenta
if not acceso:
    print("cuenta bloqueada.")

else:
    salir = False

    # mantiene el menu activo hasta que se elija la opcion salir
    while not salir:
        print("\n1) estado  2) cambiar clave  3) mensaje  4) salir")
        accion = input("opcion: ").strip()

        # valida que la opcion ingresada sea un numero
        if not accion.isdigit():
            print("error: ingrese un numero valido.")
            continue

        accion = int(accion)

        # valida que el numero este dentro de las opciones disponibles
        if accion < 1 or accion > 4:
            print("error: opcion fuera de rango.")
            continue

        match accion:
            case 1:
                # muestra el estado de inscripcion
                print("inscripto")

            case 2:
                # solicita una nueva clave
                nueva_clave = input("nueva clave: ").strip()

                # valida que la clave tenga al menos 7 caracteres
                while len(nueva_clave) < 7:
                    print("error: minimo 7 caracteres.")
                    nueva_clave = input("nueva clave: ").strip()

                # pide confirmar la nueva clave
                confirmacion = input("confirmar nueva clave: ").strip()

                # repite la confirmacion hasta que ambas claves coincidan
                while confirmacion != nueva_clave:
                    print("error: las claves no coinciden.")
                    confirmacion = input("confirmar nueva clave: ").strip()

                # actualiza la clave correcta
                clave_correcta = nueva_clave
                print("clave cambiada correctamente.")

            case 3:
                # muestra un mensaje para motivar al alumno
                print("segui asi, cada practica te acerca a recibirte.")

            case 4:
                # finaliza el menu
                print("hasta luego.")
                salir = True