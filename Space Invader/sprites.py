import pygame as py
from random import randint, choice

import pygame.key
py.init()

#Position reference for different sprites
start_position = [540, 750]


#Player Sprites
class Player(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = (20,20)
        self.color = ('green')
        self.speed = 5
        #self.image = py.Surface((self.size))
        #self.image.fill(self.color)
        self.space_surface = py.image.load('Images/spaceship.pod_.1.yellow_0 (2).png').convert_alpha()
        self.image = self.space_surface
        self.rect = self.image.get_rect(center=(start_position))
        self.balance = [1,0.5]
        self.balance_direction = 0
        self.damage_surf = py.Surface((70,72))
        self.damage_surf.fill('black')
        self.animation_index = 0
        self.damage_frames = [self.damage_surf,self.space_surface]

    def input(self):
        keys = pygame.key.get_pressed()


        if pygame.KEYDOWN:

            if keys[pygame.K_LEFT]:
                start_position[0] -= self.speed
                self.rect.x -= self.speed
                self.balance_direction = -self.balance[0]



            elif keys[pygame.K_RIGHT]:
                start_position[0] += self.speed
                self.rect.x += self.speed
                self.balance_direction = self.balance[1]


    def stay_map(self):
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= 1080:
            self.rect.right = 1080

    def update(self):

        py.key.set_repeat(0)
        self.input()
        self.rect.x += self.balance_direction
        start_position[0] = self.rect.x
        self.stay_map()

#Shoot Sprites -Left Side
class Shoots_left(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=py.Surface((4, 17))
        self.image.fill('white')
        self.rect=self.image.get_rect(center=(start_position[0] + 10,start_position[1]))

   # def colision(self):
   #     if self.rect.colliderect(Asteroid):


    def shoot_move(self):
        self.rect.y -= 10



    def shoot_kill(self):
        if self.rect.y < -100:
            self.kill()

    def update(self):
        self.shoot_move()

#Shoot Sprites - Right Side
class Shoots_right(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=py.Surface((4, 17))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=(start_position[0] + 60,start_position[1]))

   # def colision(self):
   #     if self.rect.colliderect(Asteroid):


    def shoot_move(self):
        self.rect.y -= 10

    def shoot_kill(self):
        if self.rect.y < -100:
            self.kill()

    def update(self):
        self.shoot_move()


#Asteroid Sprites
class Asteroid(py.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        asteroid1 = py.image.load('Images/asteroid.png').convert_alpha()
        asteroid2 = py.image.load('Images/asteroid2.png').convert_alpha()
        asteroid3 = py.image.load('Images/asteroid3.png').convert_alpha()
        asteroid4 = py.image.load('Images/asteroid4.png').convert_alpha()
        asteroid5 = py.image.load('Images/asteroid5.png').convert_alpha()
        asteroid6 = py.image.load('Images/asteroid6.png').convert_alpha()
        if type == 'small':
            self.image = choice([asteroid1,asteroid2,asteroid3,asteroid4,asteroid5,asteroid6])

        else:
            self.image = asteroid6
            self.speed = randint(1,3)
        self.rect = self.image.get_rect(center=(randint(10, 1080), -100))
        self.speed = (randint(3,9))





    def kill_obj(self):
        if self.rect.y >= 900:
            self.kill()


    def update(self):

        self.rect.y += self.speed
        self.kill_obj()

#Player Explosion Sprite
class Player_Explosion(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.explode_index = 0
        explode_surf1 = py.image.load('Images/explosion_frame1.png').convert_alpha()
        explode_surf2 = py.image.load('Images/explosion_frame2.png').convert_alpha()
        explode_surf3 = py.image.load('Images/explosion_frame3.png').convert_alpha()
        self.explode_list = [explode_surf1, explode_surf2,explode_surf3]
        self.image = self.explode_list[self.explode_index]
        self.rect = self.image.get_rect(center=start_position)

    def animation(self):

        self.explode_index += 0.1
        if self.explode_index >= len(self.explode_list):
            self.explode_index = 0
        self.image = self.explode_list[int(self.explode_index)]
        self.rect = self.image.get_rect(center=start_position)


    def update(self):
        self.animation()

#Asteriod Explosion Sprite
class Asteroid_Explosion(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.explode_index = 0
        explode_surf1 = py.image.load('Images/explosion_frame1.png').convert_alpha()
        explode_surf2 = py.image.load('Images/explosion_frame2.png').convert_alpha()
        explode_surf3 = py.image.load('Images/explosion_frame3.png').convert_alpha()
        explode_surf4 = py.image.load('Images/pixil-frame-0 (8).png').convert_alpha()
        self.explode_list = [explode_surf3]
        self.image = self.explode_list[self.explode_index]
        self.rect = self.image.get_rect(center=start_position)



    def animation(self):

        self.explode_index += 0.1
        if self.explode_index >= len(self.explode_list):
           self.explode_index = 0
        self.image = self.explode_list[int(self.explode_index)]
        self.rect = self.image.get_rect(center=start_position)


    def update(self):
        self.animation()







#class Boss(py.sprite.Sprite):
#    def __init__(self):
#        super().__init__()
#        self.image = py.image.load('Images/spaceship.pod_.1.yellow_0 (2).png').convert_alpha()













