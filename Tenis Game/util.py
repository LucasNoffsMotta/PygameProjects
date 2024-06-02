import pygame

pygame.init()

def font_render(text):
    font2 = pygame.font.Font('Font/Pixeltype.ttf', 30)
    surf = font2.render(text, False, (2, 212, 9))
    return surf


