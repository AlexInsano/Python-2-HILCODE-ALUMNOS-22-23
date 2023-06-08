# Escribe tu código aquí :-)
import pygame
import colores

ANCHO = 1080
ALTO = 720
CENTRO = (ANCHO/2, ALTO/2)
NOMBRE = "Alejandro"

VENTANA = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption(NOMBRE)

print(colores.getColor("AMARILLO"))

#FUENTE = pygame.font,SysFont("comicsans",16)

VENTANA.fill(colores.getColor("NEGRO"))
SOL = pygame.draw.circle(VENTANA,colores.getColor("AMARILLO"),CENTRO,60)
PLANETA = pygame.draw.circle(VENTANA,colores.getColor("AZUL"),(160,360),30)

pygame.PLANETA.rotate.CENTRO(360)

pygame.display.update()

