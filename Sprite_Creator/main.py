import pygame as py
import sys
from engine import *

py.init()

#Test game

width,length = (800,400)
screen = py.display.set_mode((width,length))
clock = py.time.Clock()


#The objects from the engine classes
list1 = FramesGenerator(60,'green',(5,5))
anima1 = FramesAnimation(list1.get_frames(),(400,200),1,screen)



while True:
    screen.fill('black')

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        
    anima1.animation()
    anima1.screen_blit()

    py.display.update()
    clock.tick(60)


