import csv


def guardar_puntaje_csv(nombre, puntaje):
    '''
    Guarda el nombre y puntaje de un jugador en un archivo CSV.

    Args:
    - nombre (str): Nombre del jugador.
    - puntaje (int): Puntaje obtenido por el jugador.

    Returns:
    - None'''

    with open('C:/Users/mtnar/OneDrive/Área de Trabalho/Programacion/Programacion/Programacion I/preguntados.py/datos.csv','a') as archivo:
        datos = csv.writer(archivo)
        datos.writerow([nombre, puntaje])
        
import csv

def obtener_mejores_puntajes_csv():
    """
    Lee los puntajes guardados en un archivo CSV y devuelve los 3 mejores puntajes ordenados de mayor a menor.

    Returns:
    - list: Lista de diccionarios con los 3 mejores puntajes, cada diccionario tiene 'nombre' y 'puntaje'.

    """
    with open('C:/Users/mtnar/OneDrive/Área de Trabalho/Programacion/Programacion/Programacion I/preguntados.py/datos.csv', 'r') as archivo:
        datos = csv.reader(archivo)
        puntajes = list(datos)

    nuevos_puntajes = []
    for fila in puntajes:
        if len(fila) >= 2:  # Validar antes de procesar
            nombre = fila[0]
            puntaje = int(fila[1])
            nuevos_puntajes.append({'nombre': nombre, 'puntaje': puntaje})

    # Ordenamiento burbuja para ordenar por puntaje descendente
    for i in range(len(nuevos_puntajes) - 1):
        for j in range(i + 1, len(nuevos_puntajes)):
            if nuevos_puntajes[i]['puntaje'] < nuevos_puntajes[j]['puntaje']:
                aux = nuevos_puntajes[i]
                nuevos_puntajes[i] = nuevos_puntajes[j]
                nuevos_puntajes[j] = aux

    mejores_puntajes = nuevos_puntajes[:3]  # Obtener los 3 mejores puntajes
    return mejores_puntajes

def cargar_y_mostrar_puntajes():
    '''"""
    Lee los puntajes guardados en un archivo CSV y guarda el último puntaje mostrado.

    Returns:
    - None
    '''
    with open('datos.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            nombre = fila[0]
            puntaje = fila[1]

        guardar_puntaje_csv(nombre, puntaje)






