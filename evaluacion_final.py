# *******************************************************
# Nombre del Estudiante: Freddy Samir Bustos Bohórquez
# Grupo: 213022A_2201
# Problema Seleccionado: Problema 3 - Auditoría de Inventario
# Código Fuente: Python
# *******************************************************

# Módulo (Función) para determinar la cantidad exacta a pedir 
def calcular_cantidad_pedido(stock_actual, stock_minimo):
    """
    Lógica de Negocio:
    - Si el Stock Actual es menor al Stock Mínimo, se pide la diferencia[cite: 217].
    - Si el Stock Actual es suficiente, se pide cero[cite: 218].
    """
    if stock_actual < stock_minimo:
        cantidad_a_pedir = stock_minimo - stock_actual
    else:
        cantidad_a_pedir = 0
    return cantidad_a_pedir

def ejecutar_auditoria():
    # Matriz con datos de artículos: [Código, Nombre, Stock Actual, Stock Mínimo] [cite: 212, 214]
    inventario = [
        [101, "Mouse Óptico", 5, 12],
        [102, "Teclado RGB", 20, 10],
        [103, "Monitor 24p", 3, 8],
        [104, "Cámara Web", 15, 15],
        [105, "Disco SSD", 2, 25]
    ]

    print("--- INFORME DE AUDITORÍA DE INVENTARIO ---")
    print(f"{'Artículo':<20} | {'Cantidad a Pedir'}")
    print("-" * 40)

    # Recorrido de la matriz para generar el informe [cite: 219]
    for articulo in inventario:
        nombre = articulo[1]
        actual = articulo[2]
        minimo = articulo[3]
        
        # Llamado al módulo de cálculo
        pedido = calcular_cantidad_pedido(actual, minimo)
        
        # Salida de resultados
        print(f"{nombre:<20} | {pedido} unidades")

# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_auditoria() 
