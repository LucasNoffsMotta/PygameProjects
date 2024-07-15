import pygame as py
from sys import exit
from random import randint

width = 800
height = 600

screen = py.display.set_mode((width,height))

clock = py.time.Clock()


#Object 1
surface1 = py.surface.Surface((10,10))
surface1.fill('red')
vector1 = py.math.Vector2(400,400)


#Object 2
surface2 = py.surface.Surface((10,10))
py.draw.circle(surface2,'red',(5,5),5)


def main():

    target_pos = vector1
    target_vector = py.math.Vector2(0,0)
    
    while True:


        for event in py.event.get():


            if event.type == py.QUIT:
                py.quit()
                exit()
            

            if event.type == py.MOUSEBUTTONDOWN:
                target_pos = py.mouse.get_pos()
                screen.blit(surface2,target_pos)

        target_vector = py.math.Vector2(target_pos)
        vector1.move_towards_ip(target_vector,5)
        

        screen.fill('black')
        screen.blit(surface1,vector1)

    
        
        clock.tick(60)
        py.display.update()

        

if __name__ == '__main__':
    py.init()
    main()
