from utils.terminal import limpiar


def listaProductos():
    print("Seleccionaste la opción lista de productos")   

def mostrarProductos():
    print("Seleccionaste la opción mostrar productos")

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