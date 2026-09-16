productos = []
precios = []
vendidos = []

opcion = ""

while opcion != "9":
    print("\n========== KIOSCO EL RECREO ==========")
    print("1. Carga inicial de productos")
    print("2. Carga de ventas del día")
    print("3. Mostrar lista de precios")
    print("4. Consulta de un producto")
    print("5. Reporte de productos sin ventas")
    print("6. Alta de un producto nuevo")
    print("7. Registrar una venta puntual")
    print("8. Cierre de caja")
    print("9. Salir")
    print("======================================")

    opcion = input("Seleccione una opción: ").strip()

    match opcion:

        # ---------------------------------------------------------
        # 1. CARGA INICIAL DE PRODUCTOS
        # ---------------------------------------------------------
        case "1":
            if len(productos) > 0:
                print("Ya existen productos cargados.")
            else:
                cantidad_texto = input(
                    "¿Cuántos productos desea cargar?: "
                ).strip()

                while not cantidad_texto.isdigit() or int(cantidad_texto) <= 0:
                    print("Error: debe ingresar un número entero mayor que cero.")
                    cantidad_texto = input(
                        "¿Cuántos productos desea cargar?: "
                    ).strip()

                cantidad_productos = int(cantidad_texto)

                for i in range(cantidad_productos):
                    print(f"\nProducto {i + 1} de {cantidad_productos}")

                    nombre_valido = False

                    while not nombre_valido:
                        nombre = input("Nombre del producto: ").strip()

                        if nombre == "":
                            print("Error: el nombre no puede estar vacío.")

                        else:
                            duplicado = False

                            for producto in productos:
                                if producto.lower() == nombre.lower():
                                    duplicado = True

                            if duplicado:
                                print("Error: el producto ya existe.")
                            else:
                                nombre_valido = True

                    precio_texto = input("Precio del producto: $").strip()

                    while not precio_texto.isdigit() or int(precio_texto) <= 0:
                        print(
                            "Error: el precio debe ser un número entero "
                            "mayor que cero."
                        )
                        precio_texto = input(
                            "Precio del producto: $"
                        ).strip()

                    precio = int(precio_texto)

                    productos.append(nombre)
                    precios.append(precio)
                    vendidos.append(0)

                print("\nCarga inicial completada correctamente.")

        # ---------------------------------------------------------
        # 2. CARGA DE VENTAS DEL DÍA
        # ---------------------------------------------------------
        case "2":
            if len(productos) == 0:
                print("No hay productos cargados.")

            else:
                print("\n--- CARGA DE VENTAS DEL DÍA ---")

                for i in range(len(productos)):
                    cantidad_texto = input(
                        f"Unidades vendidas de {productos[i]}: "
                    ).strip()

                    while not cantidad_texto.isdigit():
                        print(
                            "Error: debe ingresar un número entero "
                            "positivo o cero."
                        )
                        cantidad_texto = input(
                            f"Unidades vendidas de {productos[i]}: "
                        ).strip()

                    vendidos[i] = int(cantidad_texto)

                print("Ventas cargadas correctamente.")

        # ---------------------------------------------------------
        # 3. MOSTRAR LISTA DE PRECIOS
        # ---------------------------------------------------------
        case "3":
            if len(productos) == 0:
                print("No hay productos cargados.")

            else:
                print("\n========== LISTA DE PRODUCTOS ==========")

                for i in range(len(productos)):
                    recaudacion = precios[i] * vendidos[i]

                    print(f"\nProducto: {productos[i]}")
                    print(f"Precio: ${precios[i]}")
                    print(f"Unidades vendidas: {vendidos[i]}")
                    print(f"Recaudación: ${recaudacion}")

        # ---------------------------------------------------------
        # 4. CONSULTA DE UN PRODUCTO
        # ---------------------------------------------------------
        case "4":
            if len(productos) == 0:
                print("No hay productos cargados.")

            else:
                nombre_buscado = input(
                    "Ingrese el nombre del producto: "
                ).strip()

                posicion = -1

                for i in range(len(productos)):
                    if productos[i].lower() == nombre_buscado.lower():
                        posicion = i

                if posicion == -1:
                    print("Error: el producto no existe.")

                else:
                    recaudacion = (
                        precios[posicion] * vendidos[posicion]
                    )

                    print("\n--- DATOS DEL PRODUCTO ---")
                    print(f"Producto: {productos[posicion]}")
                    print(f"Precio: ${precios[posicion]}")
                    print(
                        f"Unidades vendidas: {vendidos[posicion]}"
                    )
                    print(f"Recaudación: ${recaudacion}")

        # ---------------------------------------------------------
        # 5. PRODUCTOS SIN VENTAS
        # ---------------------------------------------------------
        case "5":
            if len(productos) == 0:
                print("No hay productos cargados.")

            else:
                print("\n--- PRODUCTOS SIN VENTAS ---")

                hay_sin_ventas = False

                for i in range(len(productos)):
                    if vendidos[i] == 0:
                        print(f"- {productos[i]}")
                        hay_sin_ventas = True

                if not hay_sin_ventas:
                    print("Todos los productos registraron ventas.")

        # ---------------------------------------------------------
        # 6. ALTA DE UN PRODUCTO NUEVO
        # ---------------------------------------------------------
        case "6":
            nombre = input(
                "Ingrese el nombre del nuevo producto: "
            ).strip()

            error = False

            if nombre == "":
                print("Error: el nombre no puede estar vacío.")
                error = True

            if not error:
                duplicado = False

                for producto in productos:
                    if producto.lower() == nombre.lower():
                        duplicado = True

                if duplicado:
                    print("Error: el producto ya existe.")
                    error = True

            if not error:
                precio_texto = input(
                    "Ingrese el precio del producto: $"
                ).strip()

                if (
                    not precio_texto.isdigit()
                    or int(precio_texto) <= 0
                ):
                    print(
                        "Error: el precio debe ser un número entero "
                        "mayor que cero."
                    )
                    error = True

            if not error:
                productos.append(nombre)
                precios.append(int(precio_texto))
                vendidos.append(0)

                print("Producto agregado correctamente.")

        # ---------------------------------------------------------
        # 7. REGISTRAR UNA VENTA PUNTUAL
        # ---------------------------------------------------------
        case "7":
            if len(productos) == 0:
                print("No hay productos cargados.")

            else:
                nombre_buscado = input(
                    "Ingrese el nombre del producto: "
                ).strip()

                posicion = -1

                for i in range(len(productos)):
                    if productos[i].lower() == nombre_buscado.lower():
                        posicion = i

                if posicion == -1:
                    print("Error: el producto no existe.")

                else:
                    cantidad_texto = input(
                        "Cantidad de unidades vendidas: "
                    ).strip()

                    while not cantidad_texto.isdigit():
                        print(
                            "Error: debe ingresar un número entero "
                            "positivo o cero."
                        )

                        cantidad_texto = input(
                            "Cantidad de unidades vendidas: "
                        ).strip()

                    cantidad = int(cantidad_texto)

                    vendidos[posicion] += cantidad

                    print("Venta registrada correctamente.")
                    print(
                        f"{productos[posicion]} ahora tiene "
                        f"{vendidos[posicion]} unidades vendidas."
                    )

        # ---------------------------------------------------------
        # 8. CIERRE DE CAJA
        # ---------------------------------------------------------
        case "8":
            if len(productos) == 0:
                print("No hay productos cargados.")

            else:
                recaudacion_total = 0

                for i in range(len(productos)):
                    recaudacion_total += (
                        precios[i] * vendidos[i]
                    )

                posicion_mas_vendido = 0

                for i in range(1, len(productos)):
                    if (
                        vendidos[i]
                        > vendidos[posicion_mas_vendido]
                    ):
                        posicion_mas_vendido = i

                print("\n========== CIERRE DE CAJA ==========")
                print(
                    f"Recaudación total: ${recaudacion_total}"
                )

                print(
                    f"Producto más vendido: "
                    f"{productos[posicion_mas_vendido]}"
                )

                print(
                    f"Unidades vendidas: "
                    f"{vendidos[posicion_mas_vendido]}"
                )

        # ---------------------------------------------------------
        # 9. SALIR
        # ---------------------------------------------------------
        case "9":
            print("\nPrograma finalizado.")
            print("Gracias por utilizar Kiosco El Recreo.")

        # ---------------------------------------------------------
        # OPCIÓN INVÁLIDA
        # ---------------------------------------------------------
        case _:
            print(
                "Opción inválida. Ingrese una opción del 1 al 9."
            )

            
