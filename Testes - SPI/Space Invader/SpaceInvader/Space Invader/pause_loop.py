import pygame as py
from menu_class import *
from sprites import Comets_BG
import sys
from instructions import *

class PauseLoop:
    def __init__(self
                 , screen: py.display
                 , background: py.image
                 , background_comet : py.sprite.Group
                 ):

        self.screen = screen
        self.background = background
        self.clock = py.time.Clock()
        self.background_comet = background_comet
        self.pause_menu = MainMenu(screen, 'Paused', 'Resume', 'Options','Help','Quit')
        self.instructions = InstructionsLoop(self.screen,self.background,self.background_comet)

    def main_loop(self):
        paused = True

        while paused:

            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    sys.exit()

                if event.type == py.KEYDOWN:
                    if event.key == py.K_ESCAPE:
                        return True


            self.screen.blit(self.background, (0, 0))
            choice = self.pause_menu.update()


            if choice == 1:
                return True

            if choice == 3:
                if not self.instructions.main_loop():
                    continue

            if choice == 4:
                return False


            self.clock.tick(60)
            py.display.update()








