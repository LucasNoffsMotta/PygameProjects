import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from particles import Particle
from random import choice, uniform,randint


display = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

particle_group = pygame.sprite.Group()


def main_loop():
    while True:
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('clicked')
                for n in range (1000):
                    pos = pygame.mouse.get_pos()
                    color = choice(('red','orange','yellow'))
                    direction = pygame.math.Vector2(uniform(1,0),uniform(1,0))
                    direction = direction.normalize()
                    speed = randint(50,400)
                    particle_group.add(Particle(particle_group,pos,color,direction,speed))
                
        

        

        dt = clock.tick() / 1000

    
        
        display.fill('black')
        particle_group.draw(display)
        particle_group.update(dt)
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    main_loop()

