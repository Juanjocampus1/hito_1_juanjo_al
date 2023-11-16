import random

class Cliente:
    def __init__(self, nacionalidad, nombre, dni, correo, tlf, cupon_descuento=None):
        self.nacionalidad = nacionalidad
        self.nombre = nombre
        self.dni = dni
        self.correo = correo
        self.tlf = tlf
        self.cupon_descuento = cupon_descuento

class InicioSesion:

    comprobador = False

    @staticmethod
    def validar_nacionalidad(nacionalidad):
        nacionalidades_validas = {

            "español": 0.21,
            "española": 0.21,
            "francés": 0.18,
            "francesa": 0.18,
            "alemán": 0.19,
            "alemana": 0.19,
            "andorrano": 0.1,
            "andorrana": 0.1,
            "britanico": 0.20,
            "britanica": 0.20,
            "suizo": 0.17,
            "suiza": 0.17,
            "austriaco": 0.16,
            "austriaca": 0.16,
            "portugués": 0.23,
            "portuguesa": 0.23

        }

        return nacionalidades_validas.get(nacionalidad.lower(), None)

    @staticmethod
    def registrar():
        print("---------------------\n")
        while True:
            nombre = input("Dime tu nombre ('exit' para salir): ")
            if nombre.lower() == 'exit':
                return None
            elif nombre:
                break
            else:
                print("Debes ingresar tu nombre. Inténtalo de nuevo.")

        while True:
            nacionalidad = input("Dime tu nacionalidad: ").lower()
            impuesto = InicioSesion.validar_nacionalidad(nacionalidad)
            if impuesto is not None:
                break
            else:
                print("Nacionalidad no válida. Inténtalo de nuevo o verifica la escritura.")

        while True:
            dni = input("Dime tu DNI (debe tener 9 dígitos): ")
            if len(dni) == 9:
                break
            else:
                print("El DNI debe tener 9 dígitos. Inténtalo de nuevo.")

        print("---------------------\n")
        cliente = Cliente(nacionalidad, nombre, dni, "", "", cupon_descuento=None)
        cliente.cupon_descuento = None
        print("---------------------\n")
        print(f"Usuario registrado: {cliente.nombre} {cliente.nacionalidad} {cliente.dni}")
        return cliente

    @staticmethod
    def iniciar_sesion(cliente):
        global comprobador
        nombre_login = input("Nombre de usuario para iniciar sesión ('exit' para salir): ")

        if nombre_login.lower() == 'exit':
            return False

        dni_login = input("DNI para iniciar sesión: ")

        if cliente.nombre == nombre_login and cliente.dni == dni_login:
            InicioSesion.comprobador = True
            return True
        else:
            InicioSesion.comprobador = False
            return False


class Operaciones:
    @staticmethod
    def obtener_impuesto(nacionalidad):
        impuestos = {
            "español": 0.21,
            "española": 0.21,
            "francés": 0.18,
            "francesa": 0.18,
            "alemán": 0.19,
            "alemana": 0.19,
            "andorrano": 0.1,
            "andorrana": 0.1,
            "britanico": 0.20,
            "britanica": 0.20,
            "suizo": 0.17,
            "suiza": 0.17,
            "austriaco": 0.16,
            "austriaca": 0.16,
            "portugués": 0.23,
            "portuguesa": 0.23
        }

        while True:
            nacionalidad_normalizada = nacionalidad.lower()

            if nacionalidad_normalizada in impuestos:
                return impuestos[nacionalidad_normalizada]
            else:
                print("Nacionalidad no válida. Las opciones válidas son:")
                print(", ".join(impuestos.keys()))
                nacionalidad = input("Por favor, ingresa una nacionalidad válida: ")

    @staticmethod
    def aplicar_impuesto(precio, impuesto):
        return precio + (precio * impuesto)

    @staticmethod
    def aplicar_descuento_con_impuesto(precio, descuento, impuesto):

        precio_con_descuento = precio - (precio * descuento)
        return Operaciones.aplicar_impuesto(precio_con_descuento, impuesto)

    @staticmethod
    def mostrar_paises():

        paises = {

            "España": 0.21,
            "Francia": 0.18,
            "Alemania": 0.19,
            "Andorra": 0.1,
            "Reino Unido": 0.20,
            "Suiza": 0.17,
            "Austria": 0.16,
            "Portugal": 0.23

        }

        print("PAISES")
        for pais in paises.keys():
            print("-------------------")
            print(pais)

    @staticmethod
    def mostrar_productos(productos):

        print("-------------------")
        print("Este es nuestro catálogo de productos:")
        print("-------------------")
        for producto, info in productos.items():
            print(f"{producto}: Precio - {info['precio']} unidades - {info['unidades']}")
        print("-------------------")

    @staticmethod
    def jugar_minijuego_descuento():
        numero_aleatorio = random.randint(1, 10)
        print(f"Para ganar un cupón de descuento, adivina el número del 1 al 10")
        for intento in range(3):
            try:
                cupon_usuario = int(input(f"Intento {intento + 1}: "))
                if cupon_usuario == numero_aleatorio:
                    cupon_descuento = random.randint(1000, 9999)
                    print(f"¡Felicidades! Has adivinado el número. Tu nuevo cupón es: {cupon_descuento}")
                    return cupon_descuento
                else:
                    print("Número incorrecto. Inténtalo de nuevo.")
            except ValueError:
                print("Por favor, ingresa un número del 1 al 10.")

        print(f"Lo siento, el número correcto era {numero_aleatorio}. No ganaste el cupón.")
        return None

    @staticmethod
    def comprar(productos, cliente):
        global numero_de_pedido, total_con_descuento
        carrito = {}

        while True:
            Operaciones.mostrar_productos(productos)
            producto_elegido = input("Escribe el nombre del producto que quieres comprar: ")

            if producto_elegido not in productos:
                print("El producto seleccionado no está en la lista.")
                break

            cantidad = int(input("Ingresa la cantidad que deseas comprar: "))

            if cantidad > productos[producto_elegido]["unidades"]:
                print("No hay suficientes unidades de este producto.")
                break

            if producto_elegido in carrito:
                carrito[producto_elegido]["cantidad"] += cantidad
            else:
                carrito[producto_elegido] = {"precio": productos[producto_elegido]["precio"], "cantidad": cantidad}

            while True:
                seguir_comprando = input("¿Quieres añadir algo más al carrito? (s/n): ").lower()

                if seguir_comprando == 'n':
                    total_carrito = sum(item["precio"] * item["cantidad"] for item in carrito.values())
                    total_sin_descuento_con_impuesto = Operaciones.aplicar_impuesto(total_carrito, Operaciones.obtener_impuesto(cliente.nacionalidad))

                    if cliente.cupon_descuento is not None:
                        cupon_ingresado = input("Ingresa el número del cupón para conseguir un descuento del 10% (o 'no' si no tienes): ")

                        if cupon_ingresado.lower() == 'no':
                            cupon_descuento = None
                        elif cupon_ingresado.isdigit() and len(cupon_ingresado) == 4:
                            cupon_descuento = int(cupon_ingresado)
                            if cupon_descuento != cliente.cupon_descuento:
                                print("Cupón incorrecto. No se aplicará el descuento.")
                                cupon_descuento = None
                        else:
                            print("Formato de cupón incorrecto. No se aplicará el descuento.")
                            cupon_descuento = None
                    else:
                        print("No tienes un cupón de descuento.")
                        cupon_descuento = None

                    impuesto = Operaciones.obtener_impuesto(cliente.nacionalidad)
                    total_sin_descuento_ni_impuestos = total_carrito

                    if cupon_descuento is not None:
                        total_con_descuento = Operaciones.aplicar_descuento_con_impuesto(total_sin_descuento_ni_impuestos, 0.1, impuesto)
                        total_con_descuento_con_impuesto = Operaciones.aplicar_impuesto(total_con_descuento, impuesto)
                    else:
                        total_con_descuento_con_impuesto = Operaciones.aplicar_impuesto(total_sin_descuento_ni_impuestos, impuesto)

                    if cupon_descuento is True:
                        print(f"El precio total con impuestos y descuento es: {total_con_descuento_con_impuesto}€")
                    else:
                        print(f"El precio total con impuestos y sin descuento es: {total_sin_descuento_con_impuesto}€")

                    while True:
                        try:
                            total_con_descuento = total_con_descuento if cupon_descuento is not None else total_con_descuento_con_impuesto
                            pago = float(input("Ingrese el importe: "))
                            if pago < 0:
                                print("El importe no puede ser negativo. Inténtalo de nuevo.")
                                continue
                            elif pago >= total_con_descuento:
                                cambio = pago - total_con_descuento
                                cambio_redondeado = round(cambio, 2)
                                print(f"¡Gracias por tu pago! Tu cambio es: {cambio_redondeado}€")
                                print("-------------------")

                                def numero_de_pedido():
                                    return random.randint(10000, 99999)

                                quiere_factura = input(
                                    "¿Desea recibir la factura por correo electrónico? (s/n): ").lower()

                                if quiere_factura == 's':
                                    correo = input("Ingrese su correo electrónico para recibir la factura en PDF: ")
                                    cliente = Cliente("nacionalidad", "nombre", "dni", correo, "")
                                    print("La factura de la compra ha sido enviada a su correo en PDF")
                                else:
                                    print("Gracias por su compra. La factura no será enviada por correo.")
                                print("-------------------")

                                quiere_numero_seguimiento = input(
                                    "¿Desea recibir el número de seguimiento del pedido? (s/n): ").lower()

                                if quiere_numero_seguimiento == 's':
                                    tlf = input(
                                        "Ingrese su numero de telefono para recibir el numero por SMS: ")
                                    cliente = Cliente("nacionalidad", "nombre", "dni", "correo", tlf)
                                    print(
                                        f"Su número de seguimiento de pedido es: {numero_de_pedido()} y se le ha enviado una copia de este mediante un SMS")
                                else:
                                    print("Gracias por su compra. El número de seguimiento no será enviado.")
                                print("-------------------")

                                for producto, info in carrito.items():
                                    productos[producto]["unidades"] -= info["cantidad"]
                                carrito = {}

                                seguir_comprando = input("¿Quieres seguir comprando? (s/n): ").lower()

                                if seguir_comprando != 's':
                                    print("Gracias por comprar en nuestra tienda. ¡Hasta luego!")
                                    return
                                else:
                                    break
                            else:
                                print("El importe ingresado no es suficiente. Inténtalo de nuevo.")
                        except ValueError:
                           print("Por favor, ingresa un valor numérico válido")
                    break
                elif seguir_comprando == 's':
                    break
                else:
                    print("Respuesta no válida. Por favor, responde con 's' o 'n'.")
def main():

    cliente = None

    productos = {

        "pantalones vaqueros": {"precio": 30, "unidades": 15},
        "camiseta de algodon": {"precio": 15, "unidades": 20},
        "zapatos deportivos": {"precio": 50, "unidades": 10},
        "gorra de moda": {"precio": 12, "unidades": 25},
        "bufanda de invierno": {"precio": 8, "unidades": 18},
        "abrigo elegante": {"precio": 80, "unidades": 5},
        "vestido de noche": {"precio": 60, "unidades": 8},
        "calcetines estampados": {"precio": 5, "unidades": 30},
        "bolso de cuero": {"precio": 40, "unidades": 12},
        "gafas de sol": {"precio": 25, "unidades": 15},
        "sombrero de lana": {"precio": 18, "unidades": 20},
        "chaqueta deportiva": {"precio": 45, "unidades": 10},
        "falda plisada": {"precio": 22, "unidades": 15},
        "polo clasico": {"precio": 20, "unidades": 25},
        "chaleco acolchado": {"precio": 35, "unidades": 8},
        "botines de moda": {"precio": 55, "unidades": 12},
        "blusa elegante": {"precio": 28, "unidades": 18},
        "mochila casual": {"precio": 30, "unidades": 10},
        "reloj de pulsera": {"precio": 38, "unidades": 15},
        "pijama comodo": {"precio": 15, "unidades": 20},

    }

    sesion_iniciada = False

    while True:
        print("-------")
        print(" MENU")
        print("-------")
        print("1. Registro")
        print("2. Inicio de sesión")
        print("3. Paises a los que exportamos")
        print("4. Salir")

        print("---------------------")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            cliente = InicioSesion.registrar()
        elif opcion == "2":
            if cliente is not None and InicioSesion.iniciar_sesion(cliente):
                print("---------------------\n")
                print("Inicio de sesión exitoso")
                print("---------------------\n")
                print("¡Bienvenido!")
                sesion_iniciada = True
            elif cliente is None:
                print("Debes registrarte primero")
            else:
                print("---------------------\n")
                print("Credenciales incorrectas. Inicio de sesión fallido")
                sesion_iniciada = False
        elif opcion == "3":
            Operaciones.mostrar_paises()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, elige una opción correcta.")

        if sesion_iniciada:
            while True:
                print("-------")
                print(" MENU PRINCIPAL")
                print("-------")
                print("1. Minijuego de Descuento")
                print("2. Comprar producto")
                print("3. Volver")

                print("---------------------")
                opcion_principal = input("Elige una opción: ")
                if opcion_principal == "1":
                    cliente.cupon_descuento = Operaciones.jugar_minijuego_descuento()
                elif opcion_principal == "2":
                    Operaciones.comprar(productos, cliente)
                elif opcion_principal == "3":
                    break
                else:
                    print("Opción no válida. Por favor, elige una opción correcta.")