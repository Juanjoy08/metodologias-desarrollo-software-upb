from Backend.hoja_producto import obtenerHojaDeProductos
from Backend.excel import guardarHoja

hoja = obtenerHojaDeProductos()

def listarProductos():
    filas = []

    refFilas = hoja.iter_rows(
        min_row=2,
        max_row=hoja.max_row,
        min_col=1,
        max_col=4
    )
    

    for refFila in refFilas:
        valores = []

        for celda in refFila:
            valores.append(celda.value)

        filas.append(valores)

    return filas

def consultarProducto(idProducto, soloValores=True):
    refFilas = hoja.iter_rows(
        min_row=2,
        max_row=hoja.max_row,
        min_col=1,
        max_col=4
    )

    refFilasEnum = enumerate(refFilas)

    for idx, refFila in refFilasEnum:
        if str(refFila[0].value) == str(idProducto):

            if soloValores:
                valores = []
                valores.append(idx)

                for celda in refFila:
                    valores.append(celda.value)

                return valores

            else:
                return refFila

    return None

def crearProducto(idProducto, nombre, precio, cantidad):
    if consultarProducto(idProducto) != None:
        return False

    producto = (idProducto, nombre, precio, cantidad)

    hoja.append(producto)

    guardarHoja(hoja)

    return True

def eliminarProducto(idProducto):
    producto = consultarProducto(idProducto)

    if producto == None:
        return False

    hoja.delete_rows(producto[0] + 2)

    guardarHoja(hoja)

    return True

def actualizarProducto(idProducto, nombre, precio, cantidad):
    nuevos_valores = (idProducto, nombre, precio, cantidad)

    refFila = consultarProducto(idProducto, False)

    if refFila == None:
        return False

    for celda, nuevo_valor in zip(refFila, nuevos_valores):
        celda.value = nuevo_valor

    guardarHoja(hoja)

    return True