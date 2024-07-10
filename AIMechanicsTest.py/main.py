import pygame as py
from sys import exit
from engine import *

py.init()

width = 800
height = 600

clock = py.time.Clock()

screen = py.display.set_mode((width,height))
red = Being(screen,(10,10),'red',(200,200),6)
blue = Being(screen,(10,10),'blue',(400,400),5)


while True:
    screen.fill('black')
    red.update()
    blue.update()
    blue.get_move(red.get_rect())
    red.get_escape(blue.get_rect())

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
    

    py.display.update()
    clock.tick(60)




