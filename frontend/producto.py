from utils.terminal import limpiar
import Backend.productos as Productos
from tabulate import tabulate

headers=["ID", "Nombre", "Precio", "Cantidad"]

def solicitarProducto():
    nombre = input("Ingrese el nombre del producto: ")
    idProducto = input(f"Ingrese el id de {nombre}: ")
    precio = input(f"Ingrese el precio de {nombre}: ")
    cantidad = input(f"Ingrese la cantidad de {nombre}: ")

    return (idProducto, nombre, precio, cantidad)

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

def agregarProducto():
    nuevoProducto = solicitarProducto()
    productoCrado = Productos.crearProducto(*nuevoProducto)

    if productoCrado:
        print("Producto agregado correctamente...")
    else:
        print("Error al agregar producto")

def actualizarProducto():
    nuevoProducto = solicitarProducto()
    productoActualizado = Productos.actualizarProducto(*nuevoProducto)

    if productoActualizado:
        print("Producto actualizado correctamente...")
    else:
        print("Error: verifique que el producto con ese id si exista")

def eliminarProducto():
    idProducto = input("Ingrese el id del producto: ")

    productoEliminado = Productos.eliminarProducto(idProducto)

    if productoEliminado:
        print("Producto eliminado correctamente...")
    else:
        print("Error: verifique que el producto con ese id si exista")

def mostrarMenuProductos():
    separador = "------------------------------------------------"
    bienvenidos = "Productos"
    opciones = {
        "1": listaProductos,
        "2": mostrarProductos,
        "3": agregarProducto,
        "4": eliminarProducto,
        "5": actualizarProducto,
    }
    solicitud = "Ingrese una opción: "
    salida = False
   
   
    while True:
        menu = f"{bienvenidos if salida == False else separador}\n1. Lista productos\n2. Buscar productos\n3. Agregar producto\n4. Eliminar producto\n5. Actualizar producto\n6. Salir"
        print(menu)
        opcion = input(solicitud)
        salida = False

        if opcion == "6":
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