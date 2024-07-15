import pygame as py
from sys import exit
from engine import *

py.init()

width = 800
height = 600

clock = py.time.Clock()

screen = py.display.set_mode((width,height))
blue_pos = (400,400)
blue = Being(screen,(10,10),'blue',(blue_pos),5)
target_rect = blue.get_rect()


while True:
    screen.fill('black')
    mouse_pos = py.mouse.get_pos()
    mouse_surf = py.surface.Surface((2,2))
    mouse_rect = mouse_surf.get_rect(center=mouse_pos)
    blue.update()



    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
        
        if event.type == py.MOUSEBUTTONDOWN:
            target_rect = mouse_rect
    
    blue.get_move(target_rect)

    
    py.display.update()
    clock.tick(60)




