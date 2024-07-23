import pydoc
import pygame
import pygame.examples.testsprite
import pygame.image
from sprites import *
from random import randint,uniform
import math



class HordeClass:
    def __init__(self,screen,colide_group,player_rect,moving_timer_control,player_bomb,bomb_particles,level):
        #Sprite group
        self.sprites_group = pygame.sprite.Group()

        #Game Score
        self.score = 0
        self.level = level

        #Initial pos for the first sprite in the group
        self.initial_pos = (50, 100)

        #Distance between each sprite
        self.pos_distribute = 5

        #Distance between each line of enemy
        self.add_to_distribute = 90

        # Pulls the next line to the left, so the horde get a rectangle format
        self.line_adjustment = 500

        #Explosion Particles
        self.explosion = py.sprite.Group()
        self.sprite_pos = (0,0)
        self.counter_shoot = 0
        self.counter_bomb = 0

        #Screen for the argument
        self.screen = screen

        #Speed for each axis
        self.y_speed = 25
        self.x_speed = 20     #IF doubles, need to cut the Times Added condition by 2 times, so they can cover the whole screen


        #How many times each horde size can walk 20 pixels (20px = 1 'step') until reach the end off the screen
        self.can_walk = {
        1 : 42,
        2 : 37,
        3 : 33,
        4 : 28,
        5 : 24,
        6 : 19,
        7 : 15,
        8 : 10,
        9 : 6,
        10 : 1,
        }

        #Variable to calculate the move time
        self.times_added = 0


        #Group to get the colision
        self.colidegroup = colide_group
        self.player_bomb = player_bomb
        self.bomb_particles = bomb_particles


        #Player rect as a reference for the shooting
        self.player_rect = player_rect

        #Control the movment time
        self.moving_timer = 0

        #How many enemies on the horde
        self.horde_size = 5

        #Initial horde size save to not change the calculus on when some are killed
        self.initial_horde_size = 5

        # This number set the interval between each horde moves
        self.moving_timer_control = moving_timer_control

        #Creates the sprite group
        self.create_horde()

        #Control how many times the horde was restarted
        self.times_restarted = 0

        #Shooting
        self.shooting_odd = 1000 - (self.level*100)
        self.shoots_group = py.sprite.Group()

        #Killing Streak
        self.killing_streak = 0
        self.killing_timer = 0
        self.killing_streak_total_time = 6  #Set the time in seconds that a streak least
        self.streak_time_limit = self.killing_streak_total_time * 60 #Number of seconds to the streak duration x 60
        self.killing_streak_time_count = self.streak_time_limit - self.killing_timer

        self.enemy_killed = False

    def shooting_odd_mechanic(self):  # This number set the odd for each sprite on the group to shoot
        return randint(0, self.shooting_odd)

    def shooting(self):
        shoot = self.shooting_odd_mechanic()

        for sprite in self.sprites_group:
            if sprite.rect.centerx == self.player_rect.centerx and randint(0,5) == 1:  #Increase the off if the player is on the same xpos
                self.shoots_group.add(Boss_Shoots((sprite.rect.x,sprite.rect.y)))


            if shoot == 10:
                self.shoots_group.add(Boss_Shoots((sprite.rect.x, sprite.rect.y))) #Makes the random shoot happen


        self.shoots_group.draw(self.screen)
        self.shoots_group.update()


    def create_horde(self):
        #Create horde
        for i in range(0, self.horde_size):
            self.sprites_group.add(HordeSprite(self.player_rect,self.screen))

        #Organize Horde
        for count, sprite in enumerate(self.sprites_group):
            sprite.rect.x = self.initial_pos[0] + self.pos_distribute
            self.pos_distribute += self.add_to_distribute
            if count >= 10:
                sprite.rect.y = self.initial_pos[1] + self.add_to_distribute
                sprite.rect.x -= self.line_adjustment
            if count >= 15:
                sprite.rect.y = self.initial_pos[1] + self.add_to_distribute
                sprite.rect.x -= self.line_adjustment


    def enemy_move(self):
        self.moving_timer += 1  #The move timer makes the enemy move only each half second

        #Logic: The line walks x speed each time moving_timer reach the moving_control number
        #The dictionary calculates how many times the line can walk until get on the edge of the screen before turning back
        #The len(self.sprites_group) associate the horde size with the correct number on the dictionary

        if self.moving_timer == self.moving_timer_control:


            if self.initial_horde_size <= 10:

                for key,item in self.can_walk.items():
                    if self.initial_horde_size == key:
                        for sprite in self.sprites_group:
                            sprite.rect.centerx += self.x_speed
                        self.times_added += 1
                        if self.times_added == item:
                            self.x_speed = -self.x_speed
                            for sprite in self.sprites_group:
                                sprite.rect.y += self.y_speed
                            self.times_added = 0
                        self.moving_timer = 0

            else:
                for sprite in self.sprites_group:
                    sprite.rect.y += self.y_speed



    def get_colision(self):

    #Checks colision with all the possible sprite groups and make the explosion efffect:

        for sprite in self.sprites_group:
            for shoot in self.colidegroup:
                if sprite.rect.colliderect(shoot.rect):
                    if sprite.rect.colliderect(shoot.rect):
                        self.sprite_pos = sprite.rect.center
                        self.counter_shoot += 1
                        if self.counter_shoot <= 60:
                            for _ in range(1000):
                                direction = pygame.math.Vector2(uniform(1, -1), uniform(1, -1))
                                direction = direction.normalize()
                                speed = uniform(1, 40)
                                self.explosion.add(ParticleSprite(self.sprite_pos, ('green'), direction, speed, randint(1,20)))
                    else:
                        self.counter_shoot = 0
                    if py.sprite.spritecollide(shoot, self.sprites_group, True):
                        py.sprite.spritecollide(sprite, self.colidegroup, True)
                        return True


        for sprite in self.bomb_particles:
            for enemy in self.sprites_group:
                if enemy.rect.colliderect(sprite.rect):
                    if enemy.rect.colliderect(sprite.rect):
                        self.sprite_pos = sprite.rect.center
                        self.counter_bomb += 1
                        if self.counter_bomb <= 60:
                            for _ in range(1000):
                                direction = pygame.math.Vector2(uniform(1, -1), uniform(1, -1))
                                direction = direction.normalize()
                                speed = uniform(1, 40)
                                self.explosion.add(ParticleSprite(self.sprite_pos, ('green'), direction, speed, randint(10,20)))
                    else:
                        self.counter_bomb = 0

                if py.sprite.spritecollide(sprite, self.sprites_group, True):
                    py.sprite.spritecollide(enemy, self.bomb_particles, True)
                    return True

        self.explosion.update()
        self.explosion.draw(self.screen)
        return False


    def get_streak(self,multiplicator):

        #If colide with any rect:
        if self.get_colision():
            self.enemy_killed = True
            self.score += (10 * multiplicator)


            #If another enemy is killed and the streak time is > than 0, restart the counting to keep the streak up:
            if self.killing_streak_total_time > 0:
                self.killing_streak += 1
                self.killing_timer = 0

        #If the enemy_killed condition is True, add +1 to the killing timer:
        if self.enemy_killed:
            self.killing_timer += 1

        #If the counting gets to 0, restart the streak back to 0
        if self.killing_streak_total_time == 0:
            self.killing_streak = 0
            self.killing_timer = 0
            self.enemy_killed = False



    def streak_regressive(self):
        #Regressive count using the time limit and the time after some enemy is killed (+1 per frame)
        self.killing_streak_time_count = self.streak_time_limit - self.killing_timer

        # Get the value in seconds
        self.killing_streak_total_time = int(self.killing_streak_time_count / 60)


    def get_score(self):
        return self.score


    def player_proximity_check(self,player_rect):
        for sprite in self.sprites_group:
            if sprite.rect.y >= player_rect.y:
                return True
        return False


    def pos_check(self):
        for sprite in self.sprites_group:
            if sprite.rect.y >= 860:
                return True
        return False


    def atributes_reestart(self,reset_status=''):

    #PROPERLY REESTART THE WHOLE CLASS
        for sprite in self.sprites_group:
            sprite.kill()

    #Two different reset modes:
     # - Reset Horde = increase the horde speed and size after finishing a batch
     # - Reset Game  = Put the horde on the initial size and speed to reiniciate the game

        if reset_status == 'reset horde':
            self.times_added = 0
            self.moving_timer = 0
            self.initial_pos = (50, 100)
            self.pos_distribute = 5
            self.x_speed = 20
            self.moving_timer_control -= 1
            self.horde_size += 1
            self.initial_horde_size += 1
            self.create_horde()

        elif reset_status == 'reset game':
            self.times_added = 0
            self.moving_timer = 0
            self.initial_pos = (50, 100)
            self.pos_distribute = 5
            self.x_speed = 20
            self.moving_timer_control = 20
            self.horde_size = 5
            self.initial_horde_size = 5
            self.create_horde()


    def update(self,multiplicator):

        #Reset the horde if finish killing one batch
        if len(self.sprites_group) <= 0:
            self.atributes_reestart('reset horde')

        #If the horde exist, move it trought the screen
        if len(self.sprites_group) > 0:
            self.sprites_group.draw(self.screen)
            self.shooting()
            self.enemy_move()
            self.streak_regressive()
            self.get_streak(multiplicator)
            #Reestart the hordes if one of the enemies get to the bottom of the screen
            if self.pos_check():
                self.atributes_reestart('reset game')

        #If the horde increase more than 10x, end this part and jumps to the boss
        if self.horde_size > 10:
            for sprite in self.sprites_group:
                sprite.kill()
            self.killing_streak = 0
            self.killing_streak_total_time = 0
            return True, self.killing_streak_total_time, self.killing_streak
        return False,self.killing_streak_total_time,self.killing_streak
















