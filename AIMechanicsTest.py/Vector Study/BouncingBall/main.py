import pygame as py
from sys import exit
from random import randint


width = 800
height = 600


screen = py.display.set_mode((width,height))

clock = py.time.Clock()

#Vectors
gravity1 = py.math.Vector2(0,1)
gravity2 = py.math.Vector2(0,1)


#Floor pos
start_pos, end_pos = (0,500),(800,500)
floor = 500

#Object 1
surface1 = py.surface.Surface((10,10))
surface1.fill('red')
rect1 = surface1.get_rect(center=(400,0))
weitht1 = 0.5



#Object 2
surface2 = py.surface.Surface((10,10))
surface2.fill('green')
rect2 = surface2.get_rect(center=(100,200))
weight2 = 0.5


def move():
    rect1.center += gravity1 
    rect2.center += gravity2 

def gravity_aceleration():
        gravity1[1] += 1
        gravity2[1] += 1


def main():
    
    while True:

        screen.fill('black')
        py.draw.line(screen,'blue',start_pos, end_pos)
        screen.blit(surface1,rect1)
        screen.blit(surface2,rect2)

        for event in py.event.get():

            if event.type == py.QUIT:
                py.quit()
                exit()

            if event.type == py.MOUSEBUTTONDOWN:
                rect1.center = (400,0)
                rect2.center = (100,200)


        move()
        gravity_aceleration()


        if rect1.bottom >= floor:
            gravity1[1] *= 0.5
            gravity1[1] *= -1
        
        if rect2.bottom >= floor:
            gravity2[1] *= 0.5
            gravity2[1] *= -1
    
        
        clock.tick(60)
        py.display.update()

        


if __name__ == '__main__':
    py.init()
    main()
