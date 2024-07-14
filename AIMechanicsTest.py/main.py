import pygame as py
from sys import exit
from engine import *

py.init()

width = 800
height = 600

clock = py.time.Clock()

screen = py.display.set_mode((width,height))
vector1 = py.math.Vector2(200,200)
vector2 = py.math.Vector2(400,400)
red = Being(screen,(10,10),'red',vector1,6)
blue = Being(screen,(10,10),'blue',vector2,5)





while True:
    screen.fill('black')
    blue.update()
    red.update(blue.get_vector())
    # blue.get_move(red.get_rect())
    # red.get_escape(blue.get_rect())


    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
    

    py.display.update()
    clock.tick(60)




