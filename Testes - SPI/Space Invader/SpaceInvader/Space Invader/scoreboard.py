import sys
from sprites import Comets_BG
import pygame as py
from save_scores import *
from menu_class import Text

class ScoreBoard:
    def __init__(self,color,screen,background,background_comet,clock):

        self.color = color
        self.screen = screen
        self.background = background
        self.background_comet = background_comet
        self.clock = clock
        self.data_dict = load_score()
        self.font = py.font.Font('Images/Font/slkscr.ttf',40)
        self.initial_pos = (300,100)
        self.ranking_numbers = []
        self.score_rects = []
        self.level_rects = []


        #Colors
        self.green = (102,211,48)
        self.blue = (0,76,200)

        self.create_page_icon('right')
        self.create_page_icon('left')


        #Create ranking positions
        for i in range(10):

            if i == 0:
                self.ranking_numbers.append(Text(f'{i + 1}st', self.font,self.green,
                                                 (self.initial_pos[0], self.initial_pos[1] + 60)))
                self.initial_pos = self.initial_pos[0],self.initial_pos[1] + 60

            elif i == 1:
                self.ranking_numbers.append(Text(f'{i + 1}nd', self.font, self.green,
                                                 (self.initial_pos[0], self.initial_pos[1] + 60)))
                self.initial_pos = self.initial_pos[0], self.initial_pos[1] + 60

            elif i == 2:
                self.ranking_numbers.append(Text(f'{i + 1}rd', self.font, self.green,
                                                 (self.initial_pos[0], self.initial_pos[1] + 60)))
                self.initial_pos = self.initial_pos[0], self.initial_pos[1] + 60

            else:
                self.ranking_numbers.append(Text(f'{i + 1}th', self.font, self.green,
                                                 (self.initial_pos[0], self.initial_pos[1] + 60)))
                self.initial_pos = self.initial_pos[0], self.initial_pos[1] + 60


        #Create score and level rects for display:
        for key, item in self.data_dict.items():

            if key == 'score_list':
                score_initial_pos = (350,100)

                for n, score in enumerate(item):
                    if n <= 9:
                        self.score_rects.append((Text(f'{item[n]}', self.font,self.green,
                                                       (score_initial_pos[0] + 300, score_initial_pos[1] + 60))))
                        score_initial_pos = score_initial_pos[0], score_initial_pos[1] + 60


            if key == 'level_list':
                level_initial_pos = (350, 100)

                for n, score in enumerate(item):
                    if n <= 9:
                        self.level_rects.append((Text(f'Level {item[n]}', self.font, self.green,
                                                      (level_initial_pos[0] + 300, level_initial_pos[1] + 60))))
                        level_initial_pos = level_initial_pos[0], level_initial_pos[1] + 60


        self.comet_event = py.USEREVENT + 1
        py.time.set_timer(self.comet_event, 5000)


    def blit_ranking(self
                     ,category:str
                     ,rects_group:list
                     ,pos:tuple):

        title = Text(category, self.font, self.green, pos)
        for number in self.ranking_numbers:
            for cat in rects_group:
                self.screen.blit(number.text_surf, number.text_rect)
                self.screen.blit(cat.text_surf, cat.text_rect)
        self.screen.blit(title.text_surf, title.text_rect)


    def create_page_icon(self,side):

        if side == 'right':
            self.right_icon = Text('=>',self.font,self.green,(800, 780))


        elif side == 'left':
            self.left_icon = Text('<=', self.font, self.green, (140, 780))


    def main_loop(self):

        score_page = True
        running = True

        while running:

            self.screen.blit(self.background, (0, 0))
            self.background_comet.draw(self.screen)
            self.background_comet.update()

            for event in py.event.get():

                if event.type == py.QUIT:
                    py.quit()
                    sys.exit()

                if event.type == py.KEYDOWN:

                    if event.key == py.K_ESCAPE:
                        running = False

                    if event.key == py.K_RIGHT and score_page:
                        score_page = False

                    if event.key == py.K_LEFT and not score_page:
                        score_page = True


                if event.type == self.comet_event:
                    self.background_comet.add(Comets_BG())

            if score_page:
                self.blit_ranking('Score Ranking',self.score_rects,(500, 50))
                self.right_icon.blinking_text(self.screen)

            else:
                self.blit_ranking('Level Ranking', self.level_rects, (500, 50))
                self.left_icon.blinking_text(self.screen)

            self.clock.tick(60)
            py.display.update()


        if not running:
            return False








