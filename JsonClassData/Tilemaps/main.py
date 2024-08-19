import pygame as py
from constants import *
from sprites import *
from map import map
from build_map import *


class Game:
    def __init__(self):
        self.screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.all_groups = py.sprite.LayeredUpdates()
        self.clock = py.time.Clock()
        self.runnning = True


 
    def new(self, map):
        get_tilemap(self, map)



    def draw(self):
        self.screen.fill('black')
        self.all_groups.draw(self.screen)
        self.clock.tick(FPS)
        py.display.update()



    def events(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                self.runnning = False



    def update(self):
        self.screen.fill('black')
        self.draw()
        self.events()
    


    def main_loop(self):
        while self.runnning:
            self.update()


game = Game()
game.new(map)
game.main_loop()
py.quit()