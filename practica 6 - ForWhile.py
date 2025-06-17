
# 1)Dada la lista numeros = [10, 20, 30, 40], calcular la suma de todos los elementos.

lista = []
numeros = [10, 20, 30, 40]
suma = 0

for i in range(4):
    suma = suma + numeros[i] 
    print(f"{suma}")

# 2)Pedir al usuario ingresar una palabra y cuenta cuántas vocales (a, e, i, o, u) contiene (sin diferenciar mayúsculas/minúsculas).

contador = 0
palabra = str(input("Ingrese una palabra: "))
vocales = ("a","e","i","o","u")

for i in palabra:
    if i.lower() in vocales:
        contador = contador + 1
print(f"Hay {contador} vocales en tu palabra.")

# 3)Genera un número secreto entre 1 y 10 . Luego, pedile al usuario que intente adivinarlo hasta que lo logre. El programa debe indicar si el 
# intento es mayor o menor al número secreto.

num_secret = 8
adivina = int(input("Hola usuario, adivene el numero secreto entre 1 y 10: "))

while num_secret != adivina:
    if adivina > num_secret:
        print("Tu numero es mayor al secreto")
        adivina = int(input("Ingrese de nuevo: "))
    elif adivina < num_secret:
        print("Tu numero es menor al secreto")
        adivina = int(input("Ingrese de nuevo: "))
    
print("Felicitaciones!, adivinaste :)")

# 4)Crea un programa que pida al usuario ingresar usuario y contraseña (guardados previamente como por ejemplo usuario = “taller_4b” y 
# contraseña = "Python123"). El usuario debe tener la posibilidad de ingresar hasta 3 intentos. Si ingresa correctamente, 
# muestra "Iniciaste sesión correctamente"; si falla, "Usuario y/o contraseña incorrectos".

usuario_vd = "vicu y cande 4B"
contra_vd = "programacion 2025"
contador = 0

usuario = input(str("Hola, ingrese su usuario: "))
contra = input(str(f"Hola, {usuario}, ingrese su contraseña: "))

while usuario != usuario_vd and contra != contra_vd or contador == 3:
    contador = contador + 1

    if contador == 3:
        print("Usuario y/o contraseña incorrectos, intentos terminados")
        break
    usuario = input(str("Ingrese el usuario otra vez: "))
    contra = input("Ingrese la contra otra vez: ")

if usuario == usuario_vd and contra == contra_vd:
    print("Iniciaste sesion correctamente!")


# 5)Pedir al usuario un número y mostrar su tabla de multiplicar correspondiente del 1 al 10. Primero validar que el número ingresado sea positivo,
# sino debe intentar de nuevo. Una vez ingrese un número correcto, imprimir la tabla completa.

num = int(input("Hola usuario, ingrese un numero: "))

while num < 0:
    print("El numero es negativo")
    num = int(input("Ingrese el numero de nuevo: ")) 

if num > 0:
    for i in range(11): 
        print(num * i)
        

# 6)Dado el siguiente código, leer y entender lo que hace y luego hacer las modificaciones necesarias para que pueda ejecutarse varias veces hasta
#  que el usuario decida finalmente Salir. Sistema de Kiosco 

# Desarrollar un programa que simule la compra de un producto en un kiosco, cumpliendo estos requisitos:

# El usuario debe poder consultar si un producto está disponible. Si el producto no está disponible (no existe o no hay stock) debe informar: 
# "Disculpa, no tengo [nombre_producto_ingresado]." agua
# *Los productos (nombre, precio) deben estar almacenados en una tupla de tuplas. Al menos 5 productos.
# 		*El stock de un producto debe estar almacenado en una lista de listas
# [nombre, cantidad].

# Si el producto está disponible el usuario debe poder elegir la cantidad que desea comprar.
# Validar la cantidad que el usuario quiere comprar y si hay stock disponible.
# Si no hay suficiente stock, ofrecer comprar lo disponible y consultar si el usuario desea comprar igualmente o no.
# "Solo quedan [X] unidades. ¿Desea comprar esta cantidad? (S/N)"  

# Una vez confirmada la compra debe ofrecerse 2 opciones como método de pago:

#- Efectivo (sin recargo).
#- Mercado Pago (10% de recargo). Calcular el recargo si elige esta opción.

# Una vez que el usuario elige el método de pago se debe actualizar el stock del producto.

# Al finalizar la compra debe mostrar un ticket como:
# "TICKET - Producto: [nombre] | Total: $[monto]"  


# Definición de productos (tupla de tuplas)
productos = (
    ("Galletitas", 1200.0),
    ("Gaseosa", 2000.0),
    ("Chocolate", 800.0),
    ("Caramelos", 30.0),
    ("Agua", 700.0)
)

# Stock de productos (lista de listas)
stock = [
    ["Galletitas", 10],
    ["Gaseosa", 5],
    ["Chocolate", 8],
    ["Caramelos", 15],
    ["Agua", 3]
]


# 1. Consulta de producto disponible

# Búsqueda del producto
continuar = True
while continuar == True: 
    producto_buscado = input("¿Qué producto deseas comprar? ").capitalize()
    indice_producto = -1

    if producto_buscado == productos[0][0]:
        indice_producto = 0
    elif producto_buscado == productos[1][0]:
        indice_producto = 1
    elif producto_buscado == productos[2][0]:
        indice_producto = 2
    elif producto_buscado == productos[3][0]:
        indice_producto = 3
    elif producto_buscado == productos[4][0]:
        indice_producto = 4

    if indice_producto == -1:
        print(f"Disculpa, no tengo {producto_buscado}.")
    else:
        # Verificar stock
        stock_actual = stock[indice_producto][1]
    
    if stock_actual == 0:
        print(f"Disculpa, no tengo {producto_buscado}.")
    else:
        # Mostrar precio y stock
        precio = productos[indice_producto][1]
        print(f"{producto_buscado} - Precio: $ {str(precio)} - Stock: {str(stock_actual)}")
        
        # Pedir cantidad
        cantidad = int(input("¿Cuántas unidades deseas comprar? "))
        
        # Validar cantidad
        if cantidad > stock_actual:
            opcion = input(f"Solo quedan {str(stock_actual)} unidades. ¿Desea comprar esta cantidad? (S/N) ").upper()
            if opcion == "S":
                cantidad = stock_actual
            else:
                cantidad = 0
    
    respuesta = input("¿Desea comprar algo màs? (SI/NO) ")
    if respuesta.upper()=="NO": 
        continuar = False
        
        if cantidad > 0:
            # Calcular total
            total = cantidad * precio
                
            # Método de pago
            print("Métodos de pago:")
            print("1. Efectivo (sin recargo)")
            print("2. Mercado Pago (10% de recargo)")
            metodo = input("Elija método de pago (1/2): ")
             

        if metodo == "2":
            recargo = total * 0.1
            # Redondeo manual multiplicando y dividiendo
            recargo = int(recargo * 100 + 0.5) / 100
            total = total + recargo
            # Mostrar recargo
            print(f"Recargo por Mercado Pago: $ {str(recargo)}.")
                
            # Actualizar stock
            stock[indice_producto][1] = stock[indice_producto][1] - cantidad
                
            # Mostrar ticket
            print(f"TICKET - Producto: {producto_buscado} | Total: $ {str(total)}")
        else:
            print("Compra cancelada.")
    