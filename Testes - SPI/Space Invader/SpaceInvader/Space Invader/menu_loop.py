import pygame as py
from menu_class import *
import sys
from sprites import Comets_BG
from scoreboard import *
from instructions import *

class MenuLoop:

    def __init__(self
                 ,screen: py.display
                 ,background: py.image
                 ,background_comet: py.sprite.Group
                 ):


        self.screen = screen
        self.clock = py.time.Clock()
        self.background = background
        self.background_comet = background_comet

        self.scoreboard = ScoreBoard((64, 152, 94),self.screen,self.background,self.background_comet,self.clock)

        self.initial_screen = InitialScreen(self.screen,'Space Invaders','Press Enter to continue')
        self.main_menu = MainMenu(self.screen,'Space Invaders','New Game','Scoreboard','Help','Quit')
        self.instructions = InstructionsLoop(self.screen,self.background,self.background_comet)

        self.menu_loop = True
        self.running = True

        self.comet_event = py.USEREVENT + 1
        py.time.set_timer(self.comet_event,5000)



    def main_loop(self):

        while self.menu_loop:
            mouse_pos = py.mouse.get_pos()
            print(mouse_pos)


            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    sys.exit()


                if event.type == self.comet_event:
                    self.background_comet.add(Comets_BG())

                if self.running:

                    if event.type == py.KEYDOWN:
                        if event.key == py.K_RETURN:
                            self.main_menu = MainMenu(self.screen, 'Space Invaders', 'New Game',
                                                      'Scoreboard', 'Help','Quit')
                            self.running = False

                else:
                    if event.type == py.KEYDOWN:
                        if event.key == py.K_ESCAPE:

                            self.initial_screen = InitialScreen(self.screen, 'Space Invaders',
                                                                'Press Enter to continue')
                            self.running = True


            if self.running:
                self.screen.blit(self.background, (0, 0))
                self.initial_screen.update()
                self.background_comet.draw(self.screen)
                self.background_comet.update()


            if not self.running:
                self.screen.blit(self.background, (0, 0))
                choice = self.main_menu.update()
                self.background_comet.draw(self.screen)
                self.background_comet.update()

                if choice == 1:
                    self.menu_loop = False

                elif choice == 2:
                    if not self.scoreboard.main_loop():
                        continue

                elif choice == 3:
                    if not self.instructions.main_loop():
                        continue

                elif choice == 4:
                    py.quit()
                    sys.exit()


            self.clock.tick(60)
            py.display.update()








