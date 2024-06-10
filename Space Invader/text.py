import pygame as py

py.init()

font = py.font.Font(None,40)

def display_points(screen,points):
    points_surf = font.render(f'Score: {points}',True,'red')
    points_rect = points_surf.get_rect(midleft = (50,30))
    screen.blit(points_surf,points_rect)


#def start_menu(screen):
