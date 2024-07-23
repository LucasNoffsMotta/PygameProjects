import pygame as py
from horde_class import *
from EnemyClass import *
from player_class import *
from LuckyCoinClass import *

class Level():

    def __init__(self,screen,level,previous_score):
        self.screen = screen
        self.text_color = (0,76,200)
        self.font = py.font.Font('Images/Font/slkscr.ttf',30)
        self.level = level
        self.text_surf = self.font.render(f'LEVEL {self.level}',False,self.text_color)
        self.text_rect_initial_pos = (510,450)
        self.text_rect = self.text_surf.get_rect(center=self.text_rect_initial_pos)
        self.score_font = py.font.Font('Images/Font/slkscr.ttf',30)
        self.text_timer = 0
        self.timer_on_screen = False
        self.level_passed = False

        self.horde_moving_time = 20 - level

        self.player = Player(self.screen)
        self.player_rect = self.player.get_rect()
        self.player_bomb = self.player.get_bomb_rect()
        self.player_bomb_particles = self.player.get_particles_rect()

        self.horde = HordeClass(self.screen,self.player.get_shoot(),self.player_rect,
                                self.horde_moving_time,self.player_bomb,self.player_bomb_particles,
                                self.level)

        self.boss = BossClass(self.screen, self.player_rect, self.player.get_shoot())
        self.lucky_coin = LuckyCoin(self.screen,self.player.get_shoot(),self.level,self.player_bomb_particles)
        self.previous_score = previous_score
        self.coin_points = 0
        self.score = self.horde.get_score() + self.previous_score + self.coin_points

        #Killing Streak:
        self.ac_font = py.font.Font('Images/Font/slkscr.ttf', 25)
        self.killing_streak_text = py.surface.Surface((10,20))
        self.killing_steak_rect = self.killing_streak_text.get_rect(midleft=(880,780))
        self.killing_streak = 0
        self.killing_timer = 0  #Comes from the Horde method Update
        self.killing_streak_time_count = 180 - self.killing_timer
        self.killing_streak_total_time = 3
        self.killing_timer_text = py.surface.Surface((10,20))
        self.killing_timer_rect = self.killing_timer_text.get_rect(midleft=(880,800))
        self.multiplicator = 1





        #Stage1 = Horde // Stage2 = Boss
        self.stage = 1
        self.playing = True




    def display_killing_streak(self):

            #Show the timer and the number of killing spread on the screen
            if self.killing_streak > 0 and self.killing_streak_total_time > 0:
                self.killing_streak_text = self.ac_font.render(f'{int(self.killing_streak)} X ', True, self.text_color)
                self.screen.blit(self.killing_streak_text,self.killing_steak_rect)

                self.killing_timer_text = self.ac_font.render(f'{self.killing_streak_total_time}s ', True, self.text_color)
                self.screen.blit(self.killing_timer_text,self.killing_timer_rect)


    def level_text_display(self):

        if self.text_timer <= 100:
            self.text_timer += 1
            if self.text_timer >= 20:
                self.text_rect.centerx += 5
                self.text_rect.centery -= 5
        else:
            self.text_timer = 101
        self.screen.blit(self.text_surf, self.text_rect)


    def display_score(self):
        points_surf = self.score_font.render(f'SCORE: {self.score}', True, (0, 76, 200))
        points_rect = points_surf.get_rect(midleft=(750,830))
        self.screen.blit(points_surf, points_rect)


    def get_boss_shoots(self):
        return self.boss.get_shoot_group()

    def get_multiplier(self):

        if self.killing_streak < 5:
            self.multiplicator = 1
        if self.killing_streak >= 5:
            self.multiplicator = 2
        if self.killing_streak >= 10:
            self.multiplicator = 3
        if self.killing_streak >= 15:
            self.multiplicator = 4
        if self.killing_streak >= 20:
            self.multiplicator = 5


    def display_multiplier(self):
        if self.multiplicator > 1:
            multiplier_surf = self.ac_font.render(f'Points Multiplier: {self.multiplicator} X ', True,(0, 76, 200))
            multiplier_rect = multiplier_surf.get_rect(midleft=(550, 630))
            self.screen.blit(multiplier_surf, multiplier_rect)



    def update(self):
        #Show the current level
        self.level_text_display()

        #If the level animation ended, start the level
        if self.text_timer >= 101:

            # Game Over
            player_alive = self.player.update(self.get_boss_shoots(),
                                              self.horde.shoots_group, len(self.horde.sprites_group))

            if player_alive:
                boss_score = 0
                self.get_multiplier()
                self.display_multiplier()

                #Get the total score (score from shooted horde, coins and the score from the previous level)
                self.score = self.horde.get_score() + self.coin_points + self.previous_score + boss_score
                self.display_score()

                #Display the killing streak
                self.display_killing_streak()
                self.coin_points = self.lucky_coin.update()

                #If the horde gets too close, hit the player:
                if self.horde.player_proximity_check(self.player.sprite_group.sprite.rect):
                    self.player.life -= 1


                #First stage, only horde:
                if self.stage == 1:
                    play,self.killing_streak_total_time,self.killing_streak = self.horde.update(self.multiplicator)


                    #If horde finished, summons the boss:
                    if play:
                        self.multiplicator = 1
                        self.stage = 2

                #Start the boss:
                elif self.stage == 2:
                    #Boss object call
                    boss,self.correct_shoots,self.score = self.boss.update(self.player.get_shoot(),self.score)
                    #If kill the boss:
                    if not boss:
                        self.display_score()
                        return 'passed',self.score

            if not player_alive:
                return False, self.score

        return True,self.score






























