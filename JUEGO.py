import pygame
pygame.init()

screen = pygame.display.set_mode((800, 500))

pygame.display.set_caption("Mi primer juego")

blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)
PI = 3.141592653

# Itera hasta que el usuario pincha sobre el botón de cierre.
hecho = False

# Se usa para gestionar cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()

# -------- Bucle Principal del Programa -----------
while not hecho:
    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR DEBAJO DE ESTE COMENTARIO
    for evento in pygame.event.get():  # El usuario hizo algo
        if evento.type == pygame.QUIT:  # Si el usuario pincha sobre cerrar
            hecho = True  # Esto que indica que hemos acabado y sale de este bucle
    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR ENCIMA DE ESTE COMENTARIO

    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR DEBAJO DE ESTE COMENTARIO

    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR ENCIMA DE ESTE COMENTARIO

    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
    screen.fill(blanco)
    pygame.draw.rect(screen, rojo, [50, 200, 40, 35])
    pygame.display.flip()

    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR ENCIMA DE ESTE COMENTARIO

    # Limita a 20 fotogramas por segundo (frames per second)
    reloj.tick(20)