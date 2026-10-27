from utils.terminal import limpiar
import Backend.productos as Productos
from tabulate import tabulate

headers=["ID", "Nombre", "Precio", "Cantidad"]

def listaProductos():
    productos = Productos.listarProductos()

    print(tabulate(productos, headers=headers, tablefmt="rounded_grid"))
  

def mostrarProductos():
    idProducto = input("Ingrese el ID del producto: ")

    try:
        idProducto = int(idProducto)
    except ValueError:
        print("El ID debe ser un número.")
        return

    producto = Productos.consultarProducto(idProducto)

    if producto is None:
        print(f"No existe un producto con el ID {idProducto}")
        return

    print(tabulate(
        [producto[1:]],
        headers=headers,
        tablefmt="rounded_grid"
    ))


def mostrarMenuProductos():
    separador = "------------------------------------------------"
    bienvenidos = "Productos"
    opciones = {
        "1": listaProductos,
        "2": mostrarProductos,
    }
    solicitud = "Ingrese una opción: "
    salida = False
   
   
    while True:
        menu = f"{bienvenidos if salida == False else separador}\n1. Lista productos\n2. Buscar productos\n3. Salir "
        print(menu)
        opcion = input(solicitud)
        salida = False

        if opcion == "3":
            limpiar()
            break

        if opcion in opciones:
            salida = True
            solicitud = "Ingrese una opción: "
            limpiar ()
            opciones.get(opcion)()


            
        else:
            solicitud = "Opción inválida, ingrese una nueva opción: "
            limpiar() 