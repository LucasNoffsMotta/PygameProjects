import pygame

pygame.init()

def font_render(text):
    font2 = pygame.font.Font('Font/Pixeltype.ttf', 30)
    surf = font2.render(text, False, (2, 212, 9))
    return surf


def move_mode(dificulty):
    if dificulty == 1:
        vel = 10
        return vel
    if dificulty == 2:
        vel = 15
        return vel
    if dificulty == 3:
        vel = 25
        return vel
    if dificulty == 4:
        vel = 40
        return vel

#def life_icons(life):


#    life_surf = pygame.image.load('Images/heart_icon.png').convert_alpha()
#    life_surf = pygame.transform.rotozoom(life_surf, 0, 0.25)
#    dark_surf = pygame.Surface((30,30))
#    dark_surf.fill('black')
#    life_rect_1 = life_surf.get_rect(midleft=(30, 25))
#   life_rect_2 = life_surf.get_rect(midleft=(55, 25))
#   life_rect_3 = life_surf.get_rect(midleft=(80, 25))


#   if life == 3:
#        screen.blit(life_surf,life_rect_1)
#        screen.blit(life_surf,life_rect_2)
#        screen.blit(life_surf,life_rect_3)
#    if life == 2:
#        screen.blit(life_surf, life_rect_1)
#        screen.blit(life_surf, life_rect_2)

#    if life == 1:
#        screen.blit(life_surf,life_rect_1)
