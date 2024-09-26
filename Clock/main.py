import pygame as py
from constants import screen_widith,screen_height,screen_center
from sys import exit
from clock_draw import NiceClock

import os
print(os.getcwd())


screen = py.display.set_mode((screen_widith,screen_height))
clock = py.time.Clock()
nice_clock = NiceClock('red','blue','red',screen,(screen_center))



def main():

    while True:

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                exit
        
        screen.fill('black')
        nice_clock.update()
        py.display.update()

        clock.tick(20)
        


if __name__ == '__main__':
    py.init()
    main()