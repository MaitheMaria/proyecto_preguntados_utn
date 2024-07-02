import csv


def guardar_puntaje_csv(nombre, puntaje):
    with open('C:/Users/mtnar/OneDrive/Área de Trabalho/Programacion/Programacion/Programacion I/preguntados.py/datos.csv','a') as archivo:
        datos = csv.writer(archivo)
        datos.writerow([nombre, puntaje])
        
import csv

def obtener_mejores_puntajes_csv():
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
    with open('datos.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            nombre = fila[0]
            puntaje = fila[1]

        guardar_puntaje_csv(nombre, puntaje)














# import json
# import pygame

# ruta_puntajes = "C:/Users/mtnar/OneDrive/Área de Trabalho/Programacion/Programacion/Programacion I/preguntados.py/puntajes.json"

# def guardar_json(nombre_usuario, puntaje):
#     diccionario_datos = {
#         "nombre_usuario": nombre_usuario,
#         "puntaje": puntaje
#     }
#     with open(ruta_puntajes, 'a') as archivo:
#         json.dump(diccionario_datos, archivo, indent=2)
#         archivo.write('\n')


# def obtener_mejores_puntajes():

#     with open(ruta_puntajes, 'r') as archivo:
#         puntajes = json.load(archivo)

#         if len(puntajes) < 3:
#                 return puntajes
            
#         for i in range(len(puntajes)):
#             for j in range(i + 1, len(puntajes)):
#                 if puntajes[i]['puntaje'] < puntajes[j]['puntaje']:
#                     puntajes[i], puntajes[j] = puntajes[j], puntajes[i]

#         return puntajes[:3]

# def mostrar_puntajes(screen):
#     mejores_puntajes = obtener_mejores_puntajes()
#     font = pygame.font.SysFont("Arial", 20)

#     y = 100  # Ajusta la posición vertical inicial de los puntajes en la pantalla
#     posicion = 1  # Variable para llevar la cuenta de la posición de los puntajes

#     for puntaje in mejores_puntajes:
#         text = f"{posicion}. {puntaje['nombre']}: {puntaje['puntaje']}"
#         rendered_text = font.render(text, True, (255, 255, 255))
#         screen.blit(rendered_text, (100, y))  # Ajusta la posición horizontal de los puntajes
#         y += 30  # Ajusta el espacio vertical entre los puntajes
#         posicion += 1  # Incrementa la posición para el siguiente puntaje   

# def manejar_entrada_texto(event, nombre_usuario, ingresando_nombre):
#     if event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_RETURN:
#             ingresando_nombre = False
#         elif event.key == pygame.K_BACKSPACE:
#             nombre_usuario = nombre_usuario[:-1]
#         else:
#             nombre_usuario += event.unicode

#     return {'nombre_usuario': nombre_usuario, 'ingresando_nombre': ingresando_nombre}

