import pygame as py
from random import randint, choice

import pygame.key
py.init()

#Position reference for different sprites
start_position = [540, 750]
boss_position = [540,50]


#Player Sprites
class Player(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 5
        #Spaceship Image
        surface2 = py.image.load('Images/spaceship2.png').convert_alpha()
        surface3 =  py.image.load('Images/spaceship3.png').convert_alpha()
        surface4 = py.image.load('Images/spaceship4.png').convert_alpha()
        surface5 = py.image.load('Images/spaceship5.png').convert_alpha()
        surface6 = py.image.load('Images/spaceship6.png').convert_alpha()
        surface7 = py.image.load('Images/spaceship5.png').convert_alpha()
        surface8 = py.image.load('Images/spaceship4.png').convert_alpha()
        surface9 = py.image.load('Images/spaceship3.png').convert_alpha()
        surface10 = py.image.load('Images/spaceship2.png').convert_alpha()
        self.index = 0
        self.frames = [surface2,surface3,surface4,surface5,surface6,surface7,surface8,surface9,surface10]
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(center=(start_position))

        #Movement and damage
        self.balance = [1,0.5]
        self.balance_direction = 0
        self.damage_surf = py.Surface((70,72))
        self.damage_surf.fill('black')
        self.animation_index = 0
        self.damage_frames = [self.damage_surf,self.image]



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

    def animation(self):
        self.index += 0.2
        if self.index >= len(self.frames):
            self.index = 0
        self.image = self.frames[int(self.index)]

    def stay_map(self):
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= 1080:
            self.rect.right = 1080

    def update(self):

        py.key.set_repeat(0)
        self.input()
        self.animation()
        self.rect.x += self.balance_direction
        start_position[0] = self.rect.x
        self.stay_map()

#Shoot Sprites -Left Side
class Shoots_left(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=py.Surface((4, 17))
        self.image.fill('white')
        self.rect=self.image.get_rect(center=(start_position[0] +30,start_position[1] -10))

   # def colision(self):
   #     if self.rect.colliderect(Asteroid):


    def shoot_move(self):
        self.rect.y -= 10



    def shoot_kill(self):
        if self.rect.y < -100:
            self.kill()

    def update(self):
        self.shoot_move()
        self.shoot_kill()

#Shoot Sprites - Right Side
class Shoots_right(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=py.Surface((4, 17))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=(start_position[0] + 110,start_position[1] -10 ))

   # def colision(self):
   #     if self.rect.colliderect(Asteroid):


    def shoot_move(self):
        self.rect.y -= 10

    def shoot_kill(self):
        if self.rect.y < -100:
            self.kill()

    def update(self):
        self.shoot_move()
        self.shoot_kill()

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
        #explode_surf4 = py.image.load('Images/pixil-frame-0 (8).png').convert_alpha()
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

class Boss(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load('Images/spaceship.pod_.1.yellow_0 (2).png').convert_alpha()
        #self.image = py.transform.rotozoom(self.image,180,0)
        self.rect = self.image.get_rect(center=(540,50))
        self.enter_speed = 3
        self.moving_speed = 5

    def boss_enter(self):
        if self.rect.y <= 200:
           self.rect.y += self.enter_speed
        if self.rect.y >= 200:
            self.rect.x += self.moving_speed

    def boss_move(self):
        if self.rect.y == 200:
            self.rect.x += self.moving_speed
        if self.rect.x >= 900:
            self.moving_speed = -self.moving_speed
        elif self.rect.x <= 100:
            self.moving_speed = 5

    def update(self):
        self.boss_enter()
        self.boss_move()


class Boss_Shoots(py.sprite.Sprite):

    def __init__(self,rect_pos):
        super().__init__()
        self.image = py.Surface((4, 17))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=rect_pos)
        self.moving_speed = 5

    def shoot_move(self):
        self.rect.y += 5
    def shoot_kill(self):
        if self.rect.y > 1000:
            self.kill()

    def update(self):
        self.shoot_move()
        self.shoot_kill()

class Comets_BG(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        frame0 = py.image.load('Images/comet0.png').convert_alpha()
        frame1 = py.image.load('Images/comet1.png').convert_alpha()
        frame2 = py.image.load('Images/comet2.png').convert_alpha()
        frame3 = py.image.load('Images/comet3.png').convert_alpha()
        frame4 = py.image.load('Images/comet4.png').convert_alpha()
        self.index = 0
        self.frames_list = [frame0,frame1,frame2,frame3,frame4]
        self.image = self.frames_list[self.index]
        self.rect = self.image.get_rect(center=(randint(1000,1200), - randint(100,500)))
        self.comet_direction = randint(5,10)

    def comet_animation(self):
        self.index += 0.1
        if self.index >= len(self.frames_list):
            self.index = 0
        self.image = self.frames_list[int(self.index)]


    def comet_move(self):
        self.rect.x -= self.comet_direction
        self.rect.y += self.comet_direction

    def comet_del(self):
        if self.rect.y > 1000:
            self.kill()


    def update(self):
        self.comet_animation()
        self.comet_move()











