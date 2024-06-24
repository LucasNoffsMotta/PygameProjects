import pygame
from random import randint
from sprites import *

class ShieldGroup():

    frame_counter = 0

    def __init__(self, screen, font, object_shielded):
        self.shield_group = pygame.sprite.GroupSingle()
        self.shield_group.add(Shield())
        self.screen = screen
        self.font = font
        self.timer_added = 0
        self.initial_time = 6
        self.sprite = self.get_shield_sprite()
        self.object_shielded = object_shielded


    def get_time_engine(self):
        self.frame_counter += 1


    def get_show_timer(self):
        if self.frame_counter % 60 == 0:
            self.frame_counter = 1
            self.initial_time -= self.frame_counter
        show_timer = font.render(f'Shield: {self.initial_time}',True,(0,76,200))
        show_timer_rect = show_timer.get_rect(midleft=(760,90))

        if self.initial_time > 0:
            self.screen.blit(show_timer,show_timer_rect)

        return self.initial_time

    def get_sprite_group(self):
        return self.shield_group

    def get_shield_sprite(self):
        return self.shield_group.sprite

    def get_shield_pos(self):
        self.sprite.rect.x = self.object_shielded.rect.centerx - 80
        self.sprite.rect.y = self.object_shielded.rect.centery - 30
        self.shield_group.update()

    def get_colision(self,colide_group):
        return pygame.sprite.spritecollide(self.shield_group.sprite,colide_group,True)

























