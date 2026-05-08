from subprocess import STARTF_USESHOWWINDOW
import pygame
import os

pygame.init()
pygame.font.init()

#COSTANTI
WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ripasso elementi")

FPS = 120
BORDO = pygame.Rect(WIDTH//2-5, 0, 6, HEIGHT)

BIANCO = (255,255,255)
CREMA = (255, 253, 208)
NERO = (0,0,0)
ROSSO = (255,0,0)
GIALLO = (255,255,0)
VERDE = (1,157,49)
ARANCIONE = (194,90,2)

SFONDO = pygame.Rect(0, 0, WIDTH, HEIGHT)


def draw_window():
    pygame.draw.rect(WIN, CREMA, SFONDO)
    

    pygame.display.update()
