import pygame as py
from random import randint
from random import choice


class AIMoves:
    #Class that make the object move in a partially smart way the screen
    def __init__(self,rect,width,height,player_rect,player_shoot):
        self.rect = rect
        self.moving_speed = 5

        #Screen atributes, determine the borders
        self.width = width
        self.height = height

        #Player rect as a reference to attack
        self.player_rect = player_rect
        self.player_shoot = player_shoot

        #List of moves
        #Player = move towards the player rect position
        self.input_list = ['player','player','up','left','right']

        #Move handlers - Initial input, duration of each move and time counter to control it
        self.move_duration = randint(50,70)
        self.input = ['left']
        self.time_counter = 0

        #Distance between player shoot and enemy:
        self.safe_distance = 40



    def moving_up(self):
        self.rect.y += self.moving_speed

    def moving_down(self):
        self.rect.y -= self.moving_speed

    def moving_left(self):
        self.rect.x -= self.moving_speed

    def moving_right(self):
        self.rect.x += self.moving_speed

    def moving_to_player(self):
        if self.rect.centerx < self.player_rect.centerx:
            self.rect.centerx += self.moving_speed

        if self.rect.centerx > self.player_rect.centerx:
            self.rect.centerx -= self.moving_speed

    #Does the move action and set the borders
    def move_input(self):

        #Add to the time counter, so the move is done for a while until it changes
        self.time_counter += 1

        #Moves the object if still during the duration of the move
        if self.time_counter <= self.move_duration:

            if self.input == 'up' and self.rect.y <= self.height:
                self.moving_up()
                #Changes the direction if is in screen limits
                if self.rect.y >= self.height:
                    self.moving_down()

            if self.input == 'down' and self.rect.y >= 0:
                self.moving_down()

                if self.rect.y <= 0:
                    self.moving_up()

            if self.input == 'left' and self.rect.x >= 100:
                self.moving_left()
                if self.rect.x <= 0:
                    self.moving_right()

            if self.input == 'right' and self.rect.x <= self.width:
                self.moving_right()
                if self.rect.x >= self.width:
                    self.moving_left()

            if self.input == 'player':
                self.moving_to_player()

        else:
            #Sets the timer to 0 and get a new move input
            self.time_counter = 0
            self.input = choice(self.input_list)
            self.move_duration = randint(10,60)

    def shoots_dodge(self):
        for sprite in self.player_shoot.sprites():
            if (abs(sprite.rect.centery - self.rect.midbottom[1])) < self.safe_distance:

                if (sprite.rect.centerx - self.rect.centerx) < (self.rect.centerx - sprite.rect.centerx):
                    self.rect.centerx += 15

                if (self.rect.centerx - sprite.rect.centerx) < (sprite.rect.centerx - self.rect.centerx):
                    self.rect.centerx -= 15

            if self.rect.midright[0] >= 1000:
                self.moving_left()
            if self.rect.midleft[0] <= 0:
                self.moving_right()


    def update(self):
        if self.rect.y >= 200:
            self.move_input()
            self.shoots_dodge()






















