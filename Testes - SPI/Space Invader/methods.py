import pygame as py

py.init()

font = py.font.Font('Images/Font/slkscr.ttf',40)

def display_points(screen,points):
    points_surf = font.render(f'{points}',True,(0,76,200))
    points_rect = points_surf.get_rect(midleft = (760,50))
    screen.blit(points_surf,points_rect)

def display_life(screen,life):
    life_surf = font.render(f'Life: {life}',True,'red')
    life_rect = life_surf.get_rect(midleft = (250,30))
    screen.blit(life_surf,life_rect)

def life_bar(player_life,screen):
    life_bar1 = py.image.load('Images/life_bar/life bar-1.png.png').convert_alpha()
    life_bar2 = py.image.load('Images/life_bar/life bar-2.png.png').convert_alpha()
    life_bar3 = py.image.load('Images/life_bar/life bar-3.png.png').convert_alpha()
    life_bar4 = py.image.load('Images/life_bar/life bar-4.png').convert_alpha()
    life_bar5 = py.image.load('Images/life_bar/life bar-5.png').convert_alpha()
    life_bar6 = py.image.load('Images/life_bar/life bar-6.png').convert_alpha()


    show_life = {
        6:life_bar1,
        5:life_bar2,
        4:life_bar3,
        3:life_bar4,
        2:life_bar5,
        1:life_bar6
    }

    for num,image in show_life.items():
        if num == player_life:
            surf = show_life[num]
            rect = surf.get_rect(midright=(250,50))
            screen.blit(surf,rect)

def shield_duration(screen,shield_timer):

    shield_time = 5
    shield_cont = shield_time - shield_timer
    show_duration = font.render(f'Shield: {shield_cont}',False,(0,76,200))
    show_duration_rect = show_duration.get_rect(midleft=(760,90))

    if shield_cont >= 0:
        screen.blit(show_duration,show_duration_rect)

    return shield_cont,shield_timer


