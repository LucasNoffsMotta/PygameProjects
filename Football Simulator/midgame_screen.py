import sys

import pygame
from lines_draw import *
from functions import *

pygame.init()

def midgame_screen():
    width = 1200
    height = 900

    screen = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()

    font = pygame.font.Font(None,30)
    intervalo_text = font.render('Pause',True,'red')
    intervalo_text_rect = intervalo_text.get_rect(center = (400,50))
    run =True

    while run:



        screen.blit(intervalo_text,intervalo_text_rect)

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False


            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()
        clock.tick(60)
