from Backend.hoja_producto import obtenerHojaDeProductos

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

def consultarProducto(idProducto):
    refFilas = hoja.iter_rows(
        min_row=2,
        max_row=hoja.max_row,
        min_col=1,
        max_col=4
    )

    refFilasEnum = enumerate(refFilas)

    for idx, refFila in refFilasEnum:
        if refFila[0].value == idProducto:
            valores = []

            valores.append(idx)

            for celda in refFila:
                valores.append(celda.value)

            return valores

    return None

