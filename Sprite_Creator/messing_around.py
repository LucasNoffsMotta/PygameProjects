from engine import *
from random import randint
import sys


#Test game

width,length = (800,400)
screen = py.display.set_mode((width,length))
clock = py.time.Clock()


#The objects from the engine classes
random_color = (randint(0,255),randint(0,255),randint(0,255))
list1 = FramesGenerator(5,(random_color),(randint(10,20),randint(10,50)))
anima1 = FramesAnimation(list1.get_frames(),(400,200),0.5,screen)
  



while True:
    screen.fill('black')

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        
    
    
    anima1.animation()
    anima1.screen_blit()

    py.display.update()
    clock.tick(10)
