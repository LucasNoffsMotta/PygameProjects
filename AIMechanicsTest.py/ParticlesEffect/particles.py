from typing import Any
import pygame


class Particle(pygame.sprite.Sprite):

    def __init__(self,
                 groups:pygame.sprite.Group,
                 pos: list[int],
                 color:str,
                 direction: pygame.math.Vector2,
                 speed: int):
        
        super().__init__()
        self.groups = groups
        self.pos = pos
        self.color = color
        self.direction = direction
        self.speed = speed
        self.get_surface()

    
    def get_surface(self):

        self.image = pygame.Surface((4,4)).convert_alpha()
        #Make all the black pixels transparent:
        self.image.set_colorkey('black')
        pygame.draw.circle(surface=self.image,color = self.color,center=(2,2),radius=2)
        self.rect = self.image.get_rect(center = self.pos)

    
    def move(self,dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos
    
    def fall(self,dt):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_g]:
            self.direction[1] =  1
        
        if pressed[pygame.K_f]:
            self.direction[1] = -1


    def update(self,dt):
        self.move(dt)
        self.fall(dt)


    


    