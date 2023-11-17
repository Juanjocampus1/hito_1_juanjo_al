import random
from colorama import Fore, Style
from tabulate import tabulate
import pyfiglet

"""
print(f"{Fore.BLUE}Texto en azul{Style.RESET_ALL}")
print(f"{Fore.RED}Texto en rojo{Style.RESET_ALL}")
print(f"{Fore.GREEN}Texto en verde{Style.RESET_ALL}")
print(f"{Fore.YELLOW}Texto en amarillo{Style.RESET_ALL}")
"""

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
        print(f"{Fore.BLUE}---------------------\n{Style.RESET_ALL}")
        while True:
            nombre = input(f"{Fore.GREEN}Dime tu nombre ('exit' para salir): {Style.RESET_ALL}")
            if nombre.lower() == 'exit':
                return None
            elif nombre:
                break
            else:
                print(f"{Fore.YELLOW}Debes ingresar tu nombre. Inténtalo de nuevo.{Style.RESET_ALL}")

        while True:
            nacionalidad = input(f"{Fore.GREEN}Dime tu nacionalidad: {Style.RESET_ALL}").lower()
            impuesto = InicioSesion.validar_nacionalidad(nacionalidad)
            if impuesto is not None:
                break
            else:
                print(f"{Fore.RED}Nacionalidad no válida. Inténtalo de nuevo o verifica la escritura.{Style.RESET_ALL}")

        while True:
            dni = input(f"{Fore.GREEN}Dime tu DNI (debe tener 9 dígitos): {Style.RESET_ALL}")
            if len(dni) == 9:
                break
            else:
                print(f"{Fore.RED}El DNI debe tener 9 dígitos. Inténtalo de nuevo.{Style.RESET_ALL}")

        print(f"{Fore.BLUE}---------------------\n{Style.RESET_ALL}")
        cliente = Cliente(nacionalidad, nombre, dni, "", "", cupon_descuento=None)
        cliente.cupon_descuento = None
        print(f"{Fore.BLUE}---------------------\n{Style.RESET_ALL}")
        return cliente

    @staticmethod
    def iniciar_sesion(cliente):
        global comprobador
        nombre_login = input(f"{Fore.GREEN}Nombre de usuario para iniciar sesión ('exit' para salir): {Style.RESET_ALL}")

        if nombre_login.lower() == 'exit':
            return False

        dni_login = input(f"{Fore.GREEN}DNI para iniciar sesión: {Style.RESET_ALL}")

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
                print(f"{Fore.RED}Nacionalidad no válida. Las opciones válidas son:{Style.RESET_ALL}")
                print(", ".join(impuestos.keys()))
                nacionalidad = input(f"{Fore.YELLOW}Por favor, ingresa una nacionalidad válida: {Style.RESET_ALL}")

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

        print(f"{Fore.RED}PAISES{Style.RESET_ALL}")
        for pais in paises.keys():
            print(f"{Fore.BLUE}-------------------{Style.RESET_ALL}")
            print(f"{Fore.GREEN}{pais}{Style.RESET_ALL}")

    @staticmethod
    def mostrar_productos(productos):
        headers = ["Producto", "Precio", "Unidades"]

        data = []
        for producto, info in productos.items():
            data.append([producto, f"{info['precio']} €", info['unidades']])

        table = tabulate(data, headers, tablefmt="grid")

        print(f"{Fore.BLUE}-------------------")
        print("Este es nuestro catálogo de productos:")
        print(f"{Fore.BLUE}-------------------")
        print(table)
        print(f"{Fore.BLUE}-------------------")

    @staticmethod
    def jugar_minijuego_descuento():
        numero_aleatorio = random.randint(1, 10)
        print(f"{Fore.GREEN}Para ganar un cupón de descuento, adivina el número del 1 al 10{Style.RESET_ALL}")
        for intento in range(3):
            try:
                cupon_usuario = int(input(f"{Fore.BLUE}Intento {intento + 1}: {Style.RESET_ALL}"))
                if cupon_usuario == numero_aleatorio:
                    cupon_descuento = random.randint(1000, 9999)
                    print(f"{Fore.CYAN}¡Felicidades! Has adivinado el número. Tu nuevo cupón es: {cupon_descuento}{Style.RESET_ALL}")
                    return cupon_descuento
                else:
                    print(f"{Fore.RED}Número incorrecto. Inténtalo de nuevo.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.YELLOW}Por favor, ingresa un número del 1 al 10.{Style.RESET_ALL}")

        print(f"{Fore.MAGENTA}Lo siento, el número correcto era {numero_aleatorio}. No ganaste el cupón.{Style.RESET_ALL}")
        return None

    @staticmethod
    def comprar(productos, cliente):
        global numero_de_pedido, total_con_descuento
        carrito = {}

        while True:
            Operaciones.mostrar_productos(productos)
            producto_elegido = input(f"{Fore.GREEN}Escribe el nombre del producto que quieres comprar: {Style.RESET_ALL}")

            if producto_elegido not in productos:
                print(F"{Fore.YELLOW}El producto seleccionado no está en la lista.{Style.RESET_ALL}")
                break

            cantidad = int(input(f"{Fore.GREEN}Ingresa la cantidad que deseas comprar: {Style.RESET_ALL}"))

            if cantidad > productos[producto_elegido]["unidades"]:
                print(f"{Fore.RED}No hay suficientes unidades de este producto.{Style.RESET_ALL}")
                break

            if producto_elegido in carrito:
                carrito[producto_elegido]["cantidad"] += cantidad
            else:
                carrito[producto_elegido] = {"precio": productos[producto_elegido]["precio"], "cantidad": cantidad}

            while True:
                seguir_comprando = input(f"{Fore.MAGENTA}¿Quieres añadir algo más al carrito? (s/n): {Style.RESET_ALL}").lower()

                if seguir_comprando == 'n':
                    total_carrito = sum(item["precio"] * item["cantidad"] for item in carrito.values())
                    total_sin_descuento_con_impuesto = Operaciones.aplicar_impuesto(total_carrito, Operaciones.obtener_impuesto(cliente.nacionalidad))

                    if cliente.cupon_descuento is not None:
                        cupon_ingresado = input(f"{Fore.GREEN}Ingresa el número del cupón para conseguir un descuento del 10% (o 'no' si no tienes): {Style.RESET_ALL}")

                        if cupon_ingresado.lower() == 'no':
                            cupon_descuento = None
                        elif cupon_ingresado.isdigit() and len(cupon_ingresado) == 4:
                            cupon_descuento = int(cupon_ingresado)
                            if cupon_descuento != cliente.cupon_descuento:
                                print(f"{Fore.GREEN}Cupón incorrecto. No se aplicará el descuento.{Style.RESET_ALL}")
                                cupon_descuento = None
                        else:
                            print(f"{Fore.RED}Formato de cupón incorrecto. No se aplicará el descuento.{Style.RESET_ALL}")
                            cupon_descuento = None
                    else:
                        print(f"{Fore.YELLOW}No tienes un cupón de descuento.{Style.RESET_ALL}")
                        cupon_descuento = None

                    impuesto = Operaciones.obtener_impuesto(cliente.nacionalidad)
                    total_sin_descuento_ni_impuestos = total_carrito

                    if cupon_descuento is not None:
                        total_con_descuento = Operaciones.aplicar_descuento_con_impuesto(total_sin_descuento_ni_impuestos, 0.1, impuesto)
                        total_con_descuento_con_impuesto = Operaciones.aplicar_impuesto(total_con_descuento, impuesto)
                        print(f"{Fore.GREEN}El precio total con impuestos y descuento es: {total_con_descuento}€{Style.RESET_ALL}")
                    else:
                        total_con_descuento_con_impuesto = Operaciones.aplicar_impuesto(total_sin_descuento_ni_impuestos, impuesto)
                        print(f"{Fore.GREEN}El precio total con impuestos y sin descuento es: {total_sin_descuento_con_impuesto}€{Style.RESET_ALL}")

                    while True:
                        try:
                            total_con_descuento = total_con_descuento if cupon_descuento is not None else total_con_descuento_con_impuesto
                            pago = float(input(f"{Fore.GREEN}Ingrese el importe: {Style.RESET_ALL}"))
                            if pago < 0:
                                print(f"{Fore.RED}El importe no puede ser negativo. Inténtalo de nuevo.{Style.RESET_ALL}")
                                continue
                            elif pago >= total_con_descuento:
                                cambio = pago - total_con_descuento
                                cambio_redondeado = round(cambio, 2)
                                print(f"{Fore.GREEN}¡Gracias por tu pago! Tu cambio es: {cambio_redondeado}€{Style.RESET_ALL}")
                                print(f"{Fore.BLUE}-------------------{Style.RESET_ALL}")

                                def numero_de_pedido():
                                    return random.randint(10000, 99999)

                                quiere_factura = input(f"{Fore.GREEN}¿Desea recibir la factura por correo electrónico? (s/n): {Style.RESET_ALL}").lower()

                                if quiere_factura == 's':
                                    correo = input(f"{Fore.GREEN}Ingrese su correo electrónico para recibir la factura en PDF: {Style.RESET_ALL}")
                                    cliente = Cliente("nacionalidad", "nombre", "dni", correo, "")
                                    print(f"{Fore.GREEN}La factura de la compra ha sido enviada a su correo en PDF{Style.RESET_ALL}")
                                else:
                                    print(F"{Fore.GREEN}Gracias por su compra. La factura no será enviada por correo.{Style.RESET_ALL}")
                                print(f"{Fore.BLUE}-------------------{Style.RESET_ALL}")

                                quiere_numero_seguimiento = input(
                                    F"{Fore.GREEN}¿Desea recibir el número de seguimiento del pedido? (s/n): {Style.RESET_ALL}").lower()

                                if quiere_numero_seguimiento == 's':
                                    tlf = input(
                                        F"{Fore.GREEN}Ingrese su numero de telefono para recibir el numero por SMS: {Style.RESET_ALL}")
                                    cliente = Cliente("nacionalidad", "nombre", "dni", "correo", tlf)
                                    print(
                                        f"{Fore.GREEN}Su número de seguimiento de pedido es: {numero_de_pedido()} y se le ha enviado una copia de este mediante un SMS{Style.RESET_ALL}")
                                else:
                                    print(F"{Fore.GREEN}Gracias por su compra. El número de seguimiento no será enviado.{Style.RESET_ALL}")
                                print(f"{Fore.BLUE}-------------------{Style.RESET_ALL}")

                                for producto, info in carrito.items():
                                    productos[producto]["unidades"] -= info["cantidad"]
                                carrito = {}

                                seguir_comprando = input(f"{Fore.GREEN}¿Quieres seguir comprando? (s/n): {Style.RESET_ALL}").lower()

                                if seguir_comprando != 's':
                                    print(f"{Fore.GREEN}Gracias por comprar en nuestra tienda. ¡Hasta luego!{Style.RESET_ALL}")
                                    return
                                else:
                                    break
                            else:
                                print(f"{Fore.RED}El importe ingresado no es suficiente. Inténtalo de nuevo.{Style.RESET_ALL}")
                        except ValueError:
                           print(f"{Fore.RED}Por favor, ingresa un valor numérico válido{Style.RESET_ALL}")
                    break
                elif seguir_comprando == 's':
                    break
                else:
                    print(f"{Fore.RED}Respuesta no válida. Por favor, responde con 's' o 'n'.{Style.RESET_ALL}")
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

    def titulo_tienda(titulo):
        ascii_art = pyfiglet.figlet_format(titulo, font="big", width=150)
        print(f"{Fore.BLUE}{ascii_art.rstrip()}{Style.RESET_ALL}\n \n \n \n \n \n \n", end='')

    while True:
        titulo = "LLUANLLAXHOP"
        titulo_tienda(titulo)
        print(f"{Fore.BLUE} ======{Style.RESET_ALL}")
        print(f"{Fore.BLUE}[ MENU ]{Style.RESET_ALL}")
        print(f"{Fore.BLUE} ======{Style.RESET_ALL}")
        print(f"{Fore.GREEN}1. Registro{Style.RESET_ALL}")
        print(f"{Fore.GREEN}2. Inicio de sesión{Style.RESET_ALL}")
        print(f"{Fore.GREEN}3. Paises a los que exportamos{Style.RESET_ALL}")
        print(f"{Fore.GREEN}4. Salir{Style.RESET_ALL}")

        print(f"{Fore.BLUE}---------------------{Style.RESET_ALL}")
        opcion = input(f"{Fore.GREEN}Elige una opción: {Style.RESET_ALL}")

        if opcion == "1":
            cliente = InicioSesion.registrar()
        elif opcion == "2":
            if cliente is not None and InicioSesion.iniciar_sesion(cliente):
                print(f"{Fore.BLUE}---------------------\n")
                print("Inicio de sesión exitoso")
                print(f"{Fore.BLUE}---------------------\n")
                print("¡Bienvenido!")
                sesion_iniciada = True
            elif cliente is None:
                print(f"{Fore.YELLOW}Debes registrarte primero{Style.RESET_ALL}")
            else:
                print(f"{Fore.BLUE}---------------------\n{Style.RESET_ALL}")
                print(f"{Fore.RED}Credenciales incorrectas. Inicio de sesión fallido{Style.RESET_ALL}")
                sesion_iniciada = False
        elif opcion == "3":
            Operaciones.mostrar_paises()
        elif opcion == "4":
            break
        else:
            print(f"{Fore.RED}Opción no válida. Por favor, elige una opción correcta.{Style.RESET_ALL}")

        if sesion_iniciada:
            while True:
                print(f"{Fore.BLUE}-------{Style.RESET_ALL}")
                print(f"{Fore.GREEN} MENU PRINCIPAL{Style.RESET_ALL}")
                print(f"{Fore.BLUE}-------{Style.RESET_ALL}")
                print(f"{Fore.GREEN}1. Minijuego de Descuento{Style.RESET_ALL}")
                print(f"{Fore.GREEN}2. Comprar producto{Style.RESET_ALL}")
                print(f"{Fore.GREEN}3. Volver{Style.RESET_ALL}")

                print(f"{Fore.BLUE}---------------------")
                opcion_principal = input(f"{Fore.GREEN}Elige una opción: {Style.RESET_ALL}")
                if opcion_principal == "1":
                    cliente.cupon_descuento = Operaciones.jugar_minijuego_descuento()
                elif opcion_principal == "2":
                    Operaciones.comprar(productos, cliente)
                elif opcion_principal == "3":
                    break
                else:
                    print(f"{Fore.RED}Opción no válida. Por favor, elige una opción correcta.")