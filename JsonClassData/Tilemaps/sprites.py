import pygame as py
from constants import *

class WhiteTile(py.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = 1
        self.group = game.all_groups
        py.sprite.Sprite.__init__(self,self.group)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.image = py.Surface((TILESIZE,TILESIZE))
        self.image.fill('white')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y


        

