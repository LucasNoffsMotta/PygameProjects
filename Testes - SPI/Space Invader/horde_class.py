import pydoc

import pygame
import pygame.examples.testsprite
import pygame.image
from sprites import *
from random import randint



class EnemyHorde:
    def __init__(self,screen,colide_group):
        self.sprites_group = pygame.sprite.Group()
        self.initial_pos = (50, 100)
        self.pos_distribute = 5
        self.screen = screen
        self.y_speed = 25
        self.x_speed = 5  #IF doubles, need to cut the Times Added condition by 2 times
        self.times_added = 0
        self.screen_width = 600
        self.screen_height = 920
        self.line_adjustment = 500
        self.distance_between = 25
        self.colidegroup = colide_group
        self.shoots_group = py.sprite.Group()

        for i in range(0, 80):
            self.sprites_group.add(Enemy_Horde())

        for count,sprite in enumerate(self.sprites_group):
            sprite.rect.x = self.initial_pos[0] + self.pos_distribute
            self.pos_distribute += self.distance_between
            if count >= 20:
                sprite.rect.y = self.initial_pos[1] + self.distance_between
                sprite.rect.x -= self.line_adjustment
            if count >= 40:
                sprite.rect.y = self.initial_pos[1] + self.distance_between*2
                sprite.rect.x -= self.line_adjustment
            if count >= 60:
                sprite.rect.y = self.initial_pos[1] + self.distance_between*3
                sprite.rect.x -= self.line_adjustment
            if count >= 80:
                sprite.rect.y = self.initial_pos[1] + self.distance_between*4
                sprite.rect.x -= self.line_adjustment

    def enemy_move(self):
        for sprite in self.sprites_group:
            sprite.rect.centerx += self.x_speed
        self.times_added += 1
        if self.times_added == 80:
            self.x_speed = -self.x_speed
            for sprite in self.sprites_group:
                sprite.rect.y += self.y_speed
            self.times_added = 0

    def shoots(self):
        for sprite in self.sprites_group:
            if randint(0,3500) == 5:
                self.shoots_group.add(Boss_Shoots((sprite.rect.x,sprite.rect.y)))

        self.shoots_group.draw(self.screen)
        self.shoots_group.update()

    def get_colision(self):
        for sprite in self.sprites_group:
            for shoot in self.colidegroup:
                py.sprite.spritecollide(shoot,self.sprites_group,True)
                py.sprite.spritecollide(sprite,self.colidegroup,True)


    #Get if the horde is still alive, return False if it isnt, so the boss can enter the screen
    def horde_end(self):
        if len(self.sprites_group.sprites()) <= 0:
            return False
        return True


    def update(self):
        self.sprites_group.draw(self.screen)
        self.enemy_move()
        self.get_colision()
        self.shoots()



