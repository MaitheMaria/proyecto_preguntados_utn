'''Desafío:
A. Analizar detenidamente el set de datos (puede agregarle más preguntas si así
lo desea).

OK B. Crear una pantalla de inicio, con 3 (tres) botones, “Jugar”, “Ver Puntajes”,
“Salir”, la misma deberá tener alguna imagen cubriendo completamente el
fondo y tener un sonido de fondo. Al apretar el botón jugar se iniciará el juego.
Opcional: Agregar un botón para activar/desactivar el sonido de fondo.

OK C. Crear 2 botones uno con la etiqueta “Pregunta”, otro con la etiqueta “Reiniciar”

OK D. Imprimir el Puntaje: 000 donde se va a ir acumulando el puntaje de las
respuestas correctas. Cada respuesta correcta suma 10 puntos.

OK E. Al hacer clic en el botón “Pregunta” debe mostrar las preguntas comenzando
por la primera y las tres opciones, cada clic en este botón pasa a la siguiente
pregunta.

OK F. Al hacer clic en una de las tres palabras que representa una de las tres
opciones, si es correcta, debe sumar el puntaje, reproducir un sonido de
respuesta correcta y dejar de mostrar las otras opciones.

OK G. Solo tiene 2 intentos para acertar la respuesta correcta y sumar puntos, si
agotó ambos intentos, deja de mostrar las opciones y no suma puntos. Al
elegir una respuesta incorrecta se reproducirá un sonido indicando el error y
se ocultará esa opción, obligando al usuario a elegir una de las dos restantes.

OK H. Al hacer clic en el botón “Reiniciar” debe mostrar las preguntas comenzando
por la primera y las tres opciones, cada clic pasa a la siguiente pregunta.
También debe reiniciar el puntaje.

ok I. Una vez terminado el juego se deberá pedirle el nombre al usuario, guardar
ese nombre con su puntaje en un archivo, y volver a la pantalla de inicio.

J. Al ingresar a la pantalla “Ver Puntajes”, se deberá mostrar los 3 (tres) mejores
puntajes ordenados de mayor a menor, junto con sus nombres de usuario
correspondientes. Debe haber un botón para volver al menú principal.
NOTAS:
- Tienen total libertad para utilizar los sonidos, imágenes, y animaciones
(opcional) alusivas, donde corresponda.
- El formato del archivo que se debe crear para guardar los puntajes
debe ser TXT, CSV o JSON.
- Se deben definir y utilizar funciones, y las mismas deben esta'''

import pygame
from datos import lista
from funciones import *

pygame.init()

config_pantalla = [500, 400]
pygame.display.set_caption("Mi primer juego")

screen = pygame.display.set_mode(config_pantalla)

imagen_fondo = pygame.image.load("C:/Users/mtnar/OneDrive/Área de Trabalho/Programacion/Programacion/Programacion I/preguntados.py/img/img.fondo.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo, config_pantalla)

ubicacion_rect_jugar = [190, 120]
ubicacion_rect_ver_puntaje = [190, 190]
ubicacion_rect_salir = [190, 260]
ubicacion_rec_pregunta = [80, 280]
ubicacion_rec_reiniciar = [280, 280]
ubicacion_rec_nombre_puntaje = [110, 310]
ubicacion_volver_menu = [180, 280]

color_rectangulos = (49, 225, 247)

ubicacion_rec_opcion1 = [150, 120]
ubicacion_rec_opcion2 = [150, 160]
ubicacion_rec_opcion3 = [150, 200]
tam_rect_opcion = [180, 30]
color_rectangulos_opciones = (255, 0, 128)

ubicacion_mute = [400, 10]
tam_mute = [70, 25]
color_rect_mute = (255, 119, 119)

tam_rect_reiniciar = [150, 50]
tam_rect_jugar = [150, 50]
tam_rect__ver_puntaje = [150, 50]
tam_rect_salir = [150, 50]
tam_rect_pregunta = [150, 50]
tam_rect_nombre_puntaje = [280, 50]
tam_rec_volver_menu = [150, 50]

rectangulo_jugar = pygame.Rect(ubicacion_rect_jugar, tam_rect_jugar)
rectangulo_ver_puntaje = pygame.Rect(ubicacion_rect_ver_puntaje, tam_rect__ver_puntaje)
rectangulo_salir = pygame.Rect(ubicacion_rect_salir, tam_rect_salir)
rectangulo_pregunta = pygame.Rect(ubicacion_rec_pregunta, tam_rect_pregunta)
rectangulo_reiniciar = pygame.Rect(ubicacion_rec_reiniciar, tam_rect_reiniciar)
rectangulo_opcion1 = pygame.Rect(ubicacion_rec_opcion1, tam_rect_opcion)
rectangulo_opcion2 = pygame.Rect(ubicacion_rec_opcion2, tam_rect_opcion)
rectangulo_opcion3 = pygame.Rect(ubicacion_rec_opcion3, tam_rect_opcion)
rectangulo_nombre_puntaje = pygame.Rect(ubicacion_rec_nombre_puntaje, tam_rect_nombre_puntaje)
rectangulo_volver_menu = pygame.Rect(ubicacion_volver_menu, tam_rec_volver_menu)

font = pygame.font.SysFont("Arial Narrow", 20)
text_jugar = font.render("Jugar", True, (175, 71, 210))
text_ver_puntaje = font.render("Ver Puntaje", True, (175, 71, 210))
text_salir = font.render("Salir", True, (175, 71, 210))
text_pregunta = font.render("Pregunta", True, (175, 71, 210))
text_reiniciar = font.render("Reiniciar", True, (175, 71, 210))
mensaje_error = ""
text_error = font.render(mensaje_error, True, (216, 0, 166))
puntaje = 0
nombre_usuario = ''
text_nombre_jugador_puntaje = font.render(f"Nombre: {nombre_usuario} / Puntaje: {puntaje} ", True, (255, 255, 255))
text_volver_menu = font.render("Menu", True, (175, 71, 210) )
mensaje_correcto = ''
font = pygame.font.SysFont("Arial Narrow", 20)
font_ingresar_nombre = pygame.font.SysFont("Arial", 18)  

rectangulo_mute = pygame.Rect(ubicacion_mute, tam_mute)
text_mute = font.render("Mute", True, ((216, 0, 166)))
text_unmute = font.render("Unmute", True, ((216, 0, 166)))

pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)

sonido_fondo = pygame.mixer.Sound("C:/Users/mtnar/OneDrive/Área de Trabalho/Programacion/Programacion/Programacion I/preguntados.py/sonidos/soundjuego.mp3")
pygame.mixer.Sound.play(sonido_fondo, -1)

sonido_correcto = pygame.mixer.Sound("C:/Users/mtnar/OneDrive/Área de Trabalho/Programacion/Programacion/Programacion I/preguntados.py/sonidos/correcto.mp3")
sonido_incorrecto = pygame.mixer.Sound("C:/Users/mtnar/OneDrive/Área de Trabalho/Programacion/Programacion/Programacion I/preguntados.py/sonidos/errado.mp3")

estado = 'inicio'
indice_pregunta_actual = 0
intentos_por_pregunta = 0
puntaje = 0
opcion_seleccionada = None
opciones_ocultas = []
mensaje_error = ""
mostrando_error = False
sonido_muteado = False
nombre_usuario = ''
ingresando_nombre = False
puntajes = []
mensaje_correcto = ""
mostrando_correcto = False
diccionario_datos = {}  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if rectangulo_mute.collidepoint(event.pos):
                sonido_muteado = not sonido_muteado
                if sonido_muteado:
                    sonido_fondo.set_volume(0)
                    sonido_correcto.set_volume(0)
                    sonido_incorrecto.set_volume(0)
                else:
                    sonido_fondo.set_volume(1.0)

            if estado == 'inicio':
                if rectangulo_jugar.collidepoint(event.pos):
                    estado = 'jugando'
                elif rectangulo_ver_puntaje.collidepoint(event.pos):
                    estado = 'ver_puntajes'
                elif rectangulo_salir.collidepoint(event.pos):
                    running = False

            elif estado == 'jugando' or estado == 'mostrar_pregunta':
                if rectangulo_pregunta.collidepoint(event.pos):
                    if mostrando_correcto or intentos_por_pregunta >= 2:
                        indice_pregunta_actual += 1
                        intentos_por_pregunta = 0
                        opciones_ocultas = []
                        mensaje_error = ""
                        mostrando_error = False
                        mostrando_correcto = False  
                        mensaje_correcto = ""
                        if indice_pregunta_actual < len(lista):
                            estado = 'mostrar_pregunta'
                        else:
                            estado = 'fin'
                    else:
                        estado = 'mostrar_pregunta'
                        intentos_por_pregunta = 0
                        opciones_ocultas = []
                        mensaje_error = ""
                        mostrando_error = False
                        mostrando_correcto = False  
                        mensaje_correcto = ""

                elif rectangulo_reiniciar.collidepoint(event.pos):
                    estado = 'inicio'
                    indice_pregunta_actual = 0
                    puntaje = 0
                    intentos_por_pregunta = 0
                    opciones_ocultas = []
                    mensaje_error = ""
                    mostrando_error = False
                    mostrando_correcto = False
                                    
                elif estado == 'mostrar_pregunta':
                    mostrando_correcto = False  
                    mensaje_correcto = ""
                    if rectangulo_opcion1.collidepoint(event.pos) or rectangulo_opcion2.collidepoint(event.pos) or rectangulo_opcion3.collidepoint(event.pos):
                        if intentos_por_pregunta < 2:
                            opcion_seleccionada = None

                            if rectangulo_opcion1.collidepoint(event.pos) and 'a' not in opciones_ocultas:
                                opcion_seleccionada = 'a'
                            elif rectangulo_opcion2.collidepoint(event.pos) and 'b' not in opciones_ocultas:
                                opcion_seleccionada = 'b'
                            elif rectangulo_opcion3.collidepoint(event.pos) and 'c' not in opciones_ocultas:
                                opcion_seleccionada = 'c'

                            if opcion_seleccionada is not None:
                                pregunta_actual = lista[indice_pregunta_actual]

                                if pregunta_actual["correcta"] == opcion_seleccionada:
                                    puntaje += 10
                                    pygame.mixer.Sound.play(sonido_correcto)
                                    mensaje_correcto = "¡CORRECTO!"
                                    mostrando_correcto = True
                                    mostrando_error = False

                                    opciones_ocultas = []
                                    for opcion in ['a', 'b', 'c']:  
                                        if opcion != opcion_seleccionada:
                                            opciones_ocultas.append(opcion)

                                    if indice_pregunta_actual >= len(lista):
                                        estado = 'fin'

                                else:
                                    pygame.mixer.Sound.play(sonido_incorrecto)
                                    intentos_por_pregunta += 1

                                    if intentos_por_pregunta == 1:
                                        opciones_ocultas = [opcion_seleccionada]
                                        mensaje_error = "Respuesta incorrecta, tenés una chance más."
                                        mostrando_error = True
                                        mostrando_correcto = False
                                    elif intentos_por_pregunta == 2:
                                        opciones_ocultas = []
                                        for opcion in ['a', 'b', 'c']:  
                                            if opcion == opcion_seleccionada or opcion != pregunta_actual['correcta']:
                                                opciones_ocultas.append(opcion)
                                        mensaje_error = "Se agotaron los intentos. Pasá a la próxima pregunta"
                                        mostrando_error = True
                                        mostrando_correcto = False
            
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if rectangulo_volver_menu.collidepoint(event.pos):
                            estado = 'inicio'
                            indice_pregunta_actual = 0
                            puntaje = 0
                            intentos_por_pregunta = 0
                            opciones_ocultas = []
                            mensaje_error = ""
                            mostrando_error = False
                            mostrando_correcto = False
                            mensaje_correcto = ""

        if event.type == pygame.MOUSEBUTTONDOWN:
                if rectangulo_volver_menu.collidepoint(event.pos):
                    if estado == 'ver_puntajes':
                        estado = 'inicio'

        if estado == 'fin':
            if event.type == pygame.KEYDOWN:
                if ingresando_nombre and event.key == pygame.K_RETURN:
                    nombre_usuario = nombre_usuario.strip()
                    if nombre_usuario != '':
                        nuevo_puntaje = {"nombre": nombre_usuario, "puntaje": puntaje}
                        guardar_puntaje_csv(nombre_usuario, puntaje)
                        nombre_usuario = ''
                        
                        puntaje = 0
                        estado = 'inicio'  
                elif event.key == pygame.K_BACKSPACE:
                    nombre_usuario = nombre_usuario[:-1]
                else:
                    nombre_usuario += event.unicode  

            


    screen.blit(imagen_fondo, (0, 0))

    if estado == 'inicio':
        pygame.draw.rect(screen, color_rectangulos, rectangulo_jugar, border_radius=10)
        pygame.draw.rect(screen, color_rectangulos, rectangulo_ver_puntaje, border_radius=10)
        pygame.draw.rect(screen, color_rectangulos, rectangulo_salir, border_radius=10)
        screen.blit(text_jugar, (rectangulo_jugar.x + 55, rectangulo_jugar.y + 18))
        screen.blit(text_ver_puntaje, (rectangulo_ver_puntaje.x + 40, rectangulo_ver_puntaje.y + 18))
        screen.blit(text_salir, (rectangulo_salir.x + 55, rectangulo_salir.y + 18))

    elif estado == 'jugando' or estado == 'mostrar_pregunta':
        pygame.draw.rect(screen, color_rectangulos, rectangulo_pregunta, border_radius=10)
        pygame.draw.rect(screen, color_rectangulos, rectangulo_reiniciar, border_radius=10)
        screen.blit(text_pregunta, (rectangulo_pregunta.x + 45, rectangulo_pregunta.y + 18))
        screen.blit(text_reiniciar, (rectangulo_reiniciar.x + 45, rectangulo_reiniciar.y + 18))
        text_puntos = font.render(f"Puntaje: {str(puntaje):03}", True, (216, 0, 166))
        screen.blit(text_puntos, (400, 40))

    if estado == 'mostrar_pregunta':
        if indice_pregunta_actual < len(lista):
            pregunta_actual = lista[indice_pregunta_actual]
            text_pregunta_actual = font.render(pregunta_actual["pregunta"], True, (255, 0, 128))
            text_opcion1 = font.render(f"a) {pregunta_actual['a']}", True, (55, 62, 165))
            text_opcion2 = font.render(f"b) {pregunta_actual['b']}", True, (55, 62, 165))
            text_opcion3 = font.render(f"c) {pregunta_actual['c']}", True, (55, 62, 165))
            screen.blit(text_pregunta_actual, (140, 90))

            if 'a' not in opciones_ocultas:
                pygame.draw.rect(screen, color_rectangulos_opciones, rectangulo_opcion1, border_radius=10)
                screen.blit(text_opcion1, (rectangulo_opcion1.x + 10, rectangulo_opcion1.y + 5))
            if 'b' not in opciones_ocultas:
                pygame.draw.rect(screen, color_rectangulos_opciones, rectangulo_opcion2, border_radius=10)
                screen.blit(text_opcion2, (rectangulo_opcion2.x + 10, rectangulo_opcion2.y + 5))
            if 'c' not in opciones_ocultas:
                pygame.draw.rect(screen, color_rectangulos_opciones, rectangulo_opcion3, border_radius=10)
                screen.blit(text_opcion3, (rectangulo_opcion3.x + 10, rectangulo_opcion3.y + 5))

            if mensaje_correcto:
                text_correcto = font.render(mensaje_correcto, True, (250, 239, 93))
                screen.blit(text_correcto, (200, 250))

            if mostrando_error:
                text_error = font.render(mensaje_error, True, (250, 239, 93))
                screen.blit(text_error, (100, 250))

    elif estado == 'fin':
        
        text_ingresar_nombre = font.render("Ingresa tu nombre y presiona ENTER", True, (250, 239, 93))
        screen.blit(text_ingresar_nombre, (150, 150))

        nombre_text = font_ingresar_nombre.render(nombre_usuario, True, (250, 239, 93))
        screen.blit(nombre_text, (150, 200))

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    nombre_usuario = nombre_usuario.strip()
                    if nombre_usuario != '':
                        guardar_puntaje_csv(nombre_usuario, puntaje)
                        estado = 'inicio'  
                        
    elif estado == 'ver_puntajes':
        mejores_puntajes = obtener_mejores_puntajes_csv()
        texto_base_y = 100
        altura_texto = 50
        for idx, puntaje in enumerate(mejores_puntajes):
            texto_puntaje = font.render(f"{idx + 1}. {puntaje['nombre']}: {puntaje['puntaje']}", True, (250, 239, 93))
            posicion_texto = (200, texto_base_y + idx * altura_texto)
            screen.blit(texto_puntaje, posicion_texto)
        pygame.draw.rect(screen, color_rectangulos, rectangulo_volver_menu, border_radius=10)
        screen.blit(text_volver_menu, (rectangulo_volver_menu.x + 55, rectangulo_volver_menu.y + 15))
        

    pygame.draw.rect(screen, (49, 225, 247), rectangulo_mute, border_radius=10)
    if sonido_muteado:
        screen.blit(text_unmute, (rectangulo_mute.x + 10, rectangulo_mute.y + 5))
    else:
        screen.blit(text_mute, (rectangulo_mute.x + 20, rectangulo_mute.y + 5))

    if estado == 'ingresar_nombre':
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    nombre_usuario = nombre_usuario.strip()
                    if nombre_usuario != '':
                        diccionario_datos = {
                            "nombre_usuario": nombre_usuario,
                            "puntaje": puntaje
                        }
                        guardar_puntaje_csv(nombre_usuario, puntaje)
                        nombre_usuario = ''
                        puntaje = 0
                        estado = 'inicio'  
                elif event.key == pygame.K_BACKSPACE:
                    nombre_usuario = nombre_usuario[:-1]
                else:
                    nombre_usuario += event.unicode

    pygame.display.flip()

pygame.quit()