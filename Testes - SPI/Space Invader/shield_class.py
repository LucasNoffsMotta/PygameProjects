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
        # show_timer = font.render(f'Shield: {self.initial_time}',True,(0,76,200))
        # show_timer_rect = show_timer.get_rect(midleft=(760,90))
        #
        # if self.initial_time > 0:
        #     self.screen.blit(show_timer,show_timer_rect)

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

    @staticmethod
    def shield_bar(time,screen):
        shield_bar1 = py.image.load('Images/Forcefield/energy_bar/shield_count0.png').convert_alpha()
        shield_bar2 = py.image.load('Images/Forcefield/energy_bar/shield_count1.png').convert_alpha()
        shield_bar3 = py.image.load('Images/Forcefield/energy_bar/shield_count2.png').convert_alpha()
        shield_bar4 = py.image.load('Images/Forcefield/energy_bar/shield_count3.png').convert_alpha()
        shield_bar5 = py.image.load('Images/Forcefield/energy_bar/shield_count4.png').convert_alpha()
        shield_bar6 = py.image.load('Images/Forcefield/energy_bar/shield_count5.png').convert_alpha()


        show_life = {
            6: shield_bar1,
            5: shield_bar2,
            4: shield_bar3,
            3: shield_bar4,
            2: shield_bar5,
            1: shield_bar6
        }

        for num, image in show_life.items():
            if num == time:
                surf = show_life[num]
                surf = py.transform.rotozoom(surf,0,0.9)
                rect = surf.get_rect(midleft=(30,890))

                screen.blit(surf, rect)


    def update(self,sprite_group,time,sprite_group2):
        self.get_time_engine()
        self.get_shield_pos()
        self.get_colision(sprite_group)
        self.get_sprite_group().draw(self.screen)
        self.shield_bar(time, self.screen)
        self.get_colision(sprite_group2)























