import pygame as py
from sprites import LuckyCoinSprite
from random import choice,randint

class LuckyCoin():
    def __init__(self,screen,player_shoots,level,player_bomb_particles):
        #Atributes
        self.screen = screen

        #Colide groups:
        self.player_shoots = player_shoots
        self.player_bomb_particles = player_bomb_particles
        self.level = level
        self.points = 0
        self.pos = (randint(20,800),(-50))
        self.current_chance = 1000
        self.spawn_chance = int(self.current_chance/self.level)

        #Sprite Groups
        self.yellow_group = py.sprite.Group()
        self.red_group = py.sprite.Group()
        self.green_group = py.sprite.Group()
        self.blue_group = py.sprite.Group()



        self.all_gorups = [self.yellow_group,self.red_group,self.green_group,self.blue_group]

        #Create list of coins based on rarity
        self.color_list = []
        for i in range(0,1):
            self.create_list('yellow',2)
            self.create_list('red',5)
            self.create_list('green',10)
            self.create_list('blue',15)

        self.points_value = {
            'yellow':self.yellow_group,
            'red':self.red_group,
            'green':self.green_group,
            'blue':self.blue_group
        }


    def create_list(self,color,rarity):
        for i in range(0,rarity):
            self.color_list.append(color)

    def create_object(self):
        self.speed = 5
        self.color = choice(self.color_list)

        for key, value in self.points_value.items():
            if self.color == key:
                value.add(LuckyCoinSprite(self.color,self.pos,self.speed))



    def get_colision(self,coin_group,shoot_group,particles_group,points):

        #Shoot colision
        for sprite in coin_group:
            for shoot_sprite in shoot_group:
                if py.sprite.spritecollide(shoot_sprite,coin_group,True):
                    py.sprite.spritecollide(sprite,shoot_group,True)
                    sprite.kill()
                    self.points += points

        #Bomb Colision
        for particle in particles_group:
            for sprite in coin_group:
                if py.sprite.spritecollide(particle,coin_group,True):
                    py.sprite.spritecollide(sprite,particles_group,True)
                    self.points += points


    def update(self):

        if randint(0,self.spawn_chance) == 1:
            self.pos = (randint(20,800),(-50))
            self.create_object()


        self.get_colision(self.yellow_group,self.player_shoots,self.player_bomb_particles,200)
        self.get_colision(self.red_group,self.player_shoots,self.player_bomb_particles,50)
        self.get_colision(self.green_group,self.player_shoots,self.player_bomb_particles,25)
        self.get_colision(self.blue_group,self.player_shoots,self.player_bomb_particles,10)

        for group in self.all_gorups:
            group.draw(self.screen)
            group.update()

        return self.points
















