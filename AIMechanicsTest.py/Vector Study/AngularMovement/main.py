import pygame as py
from sys import exit
import math


py.init()


def main():

    width = 800
    height = 600

    clock = py.time.Clock()

    screen = py.display.set_mode((width,height))
    end_point = py.math.Vector2(170, 0)
    angle = 0
    start_rotation =  2
    rotation = start_rotation

    while True:
        screen.fill('black')
        mouse_pos = py.mouse.get_pos()
        start_point = py.math.Vector2(400,100)
        angle = (angle + rotation) % 360
        current_endpoint = start_point + end_point.rotate(angle)
        py.draw.line(screen,'red',(start_point),(current_endpoint))
        
        if angle >= 180:
            rotation = -rotation
            
    
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                exit()

            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    rotation = 0
                if event.key == py.K_RETURN:
                    rotation = -2
                
            
        
        py.display.update()
        clock.tick(60)


if __name__ == '__main__':
    py.init()
    main()

