import pygame as py

py.init()

font = py.font.Font('Images/Font/slkscr.ttf',40)

def display_points(screen,points):
    points_surf = font.render(f'{points}',True,(0,76,200))
    points_rect = points_surf.get_rect(midleft = (900,900))
    screen.blit(points_surf,points_rect)

def life_bar(player_life,screen,pos=None):
    life_bar1 = py.image.load('Images/life_bar/life bar-1.png.png').convert_alpha()
    life_bar2 = py.image.load('Images/life_bar/life bar-2.png.png').convert_alpha()
    life_bar3 = py.image.load('Images/life_bar/life bar-3.png.png').convert_alpha()
    life_bar4 = py.image.load('Images/life_bar/life bar-4.png').convert_alpha()
    life_bar5 = py.image.load('Images/life_bar/life bar-5.png').convert_alpha()
    life_bar6 = py.image.load('Images/life_bar/life bar-6.png').convert_alpha()

    if pos == 'left':
        pos = (250,50)
    elif pos == 'right':
        pos = (900,150)

    elif pos == 'bottomleft':
        pos = (200,750)

    elif pos == 'center':
        pos = (500,900)

    else:
        pos = (-100,-100)


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
            rect = surf.get_rect(center=(pos))
            screen.blit(surf,rect)



