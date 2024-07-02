import pygame as py
from random import randint, choice
from methods import *
from moving_AI import *
import pygame.key


py.init()

#Position reference for different sprites
start_position = [540,750]  #Reference to: Player center position, shoots center position (shoots_pos = start_position[1] -10)
#boss_position = [540,50]


#Player Sprites
class Player(py.sprite.Sprite):

    def __init__(self):
        super().__init__()

        #Spaceship Image
        #Still Images
        surface2 = py.image.load('Images/Spaceship/spaceship2.png').convert_alpha()
        surface3 = py.image.load('Images/Spaceship/spaceship3.png').convert_alpha()
        surface4 = py.image.load('Images/Spaceship/spaceship4.png').convert_alpha()
        surface5 = py.image.load('Images/Spaceship/spaceship5.png').convert_alpha()
        surface6 = py.image.load('Images/Spaceship/spaceship6.png').convert_alpha()

        #Acelerating Images
        acel1 = py.image.load('Images/Spaceship/Acelerating Frames/acel1.png').convert_alpha()
        acel2 = py.image.load('Images/Spaceship/Acelerating Frames/acel2.png').convert_alpha()
        acel3 = py.image.load('Images/Spaceship/Acelerating Frames/acel3.png').convert_alpha()
        acel4 = py.image.load('Images/Spaceship/Acelerating Frames/acel4.png').convert_alpha()
        acel5 = py.image.load('Images/Spaceship/Acelerating Frames/acel5.png').convert_alpha()


        self.speed = 5
        self.index = 0
        self.direction = 'still'
        self.still_frames = [surface2,surface3,surface4,surface5,surface6,surface5,surface4,surface3,surface2]
        self.acellerate_frames = [acel1,acel2,acel3,acel4,acel5,acel4,acel3,acel2,acel1]
        self.breaking_frames = [surface2,surface3]
        self.main_anima_list = self.still_frames
        self.image = self.main_anima_list[self.index]
        self.rect = self.image.get_rect(center=(start_position))


        #Movement and damage
        self.balance = [1,0.5]
        self.balance_direction = 0
        self.damage_surf = py.Surface((70,72))
        self.damage_surf.fill('black')
        self.animation_index = 0
        self.damage_frames = [self.damage_surf,self.image]
        self.life = 100


    def input(self):
        keys = pygame.key.get_pressed()
        self.direction = 'still'
        if pygame.KEYDOWN:


            if keys[pygame.K_LEFT]:
                start_position[0] -= self.speed
                self.rect.x -= self.speed
                self.balance_direction = -self.balance[0]

            if keys[pygame.K_RIGHT]:
                start_position[0] += self.speed
                self.rect.x += self.speed
                self.balance_direction = self.balance[1]

            if keys[pygame.K_UP]:
                start_position[1] -= self.speed
                self.rect.y -= self.speed

                if self.rect.y > 500:
                    self.direction = 'acelerate'

            if keys[pygame.K_DOWN]:
                start_position[1] += self.speed
                self.rect.y += self.speed

                if self.rect.y < 700:
                    self.direction = 'break'


    def animation(self):

        if self.direction == 'acelerate':
            self.main_anima_list = self.acellerate_frames

        elif self.direction == 'break':
            self.main_anima_list = self.breaking_frames

        elif self.direction == 'still':
            self.main_anima_list = self.still_frames

        self.index += 0.2
        if self.index >= len(self.main_anima_list):
            self.index = 0
        self.image = self.main_anima_list[int(self.index)]



    def stay_map(self):

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right >= 1080:
            self.rect.right = 1080

        if self.rect.y <= 500:
            self.rect.y = 500
            start_position[1] = self.rect.center[1] - 10


        if self.rect.y >= 700:
            self.rect.y = 700
            start_position[1] = self.rect.center[1] - 10


    def update(self):

        py.key.set_repeat(0)
        self.input()
        self.rect.x += self.balance_direction
        start_position[0] = self.rect.x
        self.animation()
        self.stay_map()
        self.rect.height = 40
        self.rect.width = 100

#Shoot Sprites -Left Side
class Shoots_left(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=py.Surface((4, 17))
        self.image.fill('white')
        self.rect=self.image.get_rect(center=(start_position[0] +30, start_position[1] -5 ))

    def shoot_move(self):
        self.rect.y -= 10

    def shoot_kill(self):
        if self.rect.midbottom[0] < 0:
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
        self.rect = self.image.get_rect(center=(start_position[0] + 110,start_position[1] - 5))


    def shoot_move(self):
        self.rect.y -= 10

    def shoot_kill(self):
        if self.rect.midbottom[0] < 0:
            self.kill()

    def update(self):
        self.shoot_move()
        self.shoot_kill()


#Asteroid Sprites
class Asteroid(py.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        asteroid1 = py.image.load('Images/Asteroids/asteroid.png').convert_alpha()
        asteroid2 = py.image.load('Images/Asteroids/asteroid2.png').convert_alpha()
        asteroid3 = py.image.load('Images/Asteroids/asteroid3.png').convert_alpha()
        asteroid4 = py.image.load('Images/Asteroids/asteroid4.png').convert_alpha()
        asteroid5 = py.image.load('Images/Asteroids/asteroid5.png').convert_alpha()
        asteroid6 = py.image.load('Images/Asteroids/asteroid6.png').convert_alpha()
        if type == 'small':
            self.image = choice([asteroid1,asteroid2,asteroid3,asteroid4,asteroid5,asteroid6])

        else:
            self.image = asteroid6
        self.speed = 5
        self.rect = self.image.get_rect(center=(randint(10, 1080), -100))


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
        explode_surf1 = py.image.load('Images/Explosion/explosion_frame1.png').convert_alpha()
        explode_surf2 = py.image.load('Images/Explosion/explosion_frame2.png').convert_alpha()
        explode_surf3 = py.image.load('Images/Explosion/explosion_frame3.png').convert_alpha()
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
        explode_surf1 = py.image.load('Images/Explosion/explosion_frame1.png').convert_alpha()
        explode_surf2 = py.image.load('Images/Explosion/explosion_frame2.png').convert_alpha()
        explode_surf3 = py.image.load('Images/Explosion/explosion_frame3.png').convert_alpha()
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
    def __init__(self,player_rect):
        super().__init__()

        #Still frames
        frame1 = py.image.load('Images/Spaceship/Enemy Ship/enemy_stand.png').convert_alpha()
        frame2 = py.image.load('Images/Spaceship/Enemy Ship/enemy_stand 2.png').convert_alpha()
        self.list_still = [frame1,frame2]

        #Shooting Frames
        self.shoot_list = []

        for i in range(12):
            self.shoot_list.append(py.image.load(f'Images/Spaceship/Enemy Ship/enemy_shooting/enemy_shoot_sprite{i:02}.png').convert_alpha())

        self.frame_index = 0
        self.image = self.list_still[self.frame_index]
        self.rect = self.image.get_rect(center=(500,-200))
        self.enter_speed = 5
        self.time_count = 0
        self.timer_add = 1
        self.times_apeared = 0
        self.shoot_time = 0
        self.player_rect = player_rect
        self.ai_moves = AIMoves(self.rect, 800, 500,self.player_rect)


    def sprite_animation(self):

        if self.rect.y <= 200:
            self.sprite_list = self.list_still
        else:
            self.sprite_list = self.shoot_list


        self.frame_index += 1
        if self.frame_index >= len(self.sprite_list):
            self.frame_index = 0
        self.image = self.sprite_list[int(self.frame_index)]


    def boss_enter(self):
        if self.rect.y <= 200:
            self.rect.y += self.enter_speed


    def boss_back(self):
        self.rect.y -= 5

    #Counts the boss time on screen // It goes back after 4 seconds
    def boss_screen_time_control(self):
        if self.timer_add == 1 and self.time_count < 240:
            self.boss_enter()
        if self.rect.y >= 200:
            self.time_count += self.timer_add
        if self.time_count >= 240:
            self.boss_back()
        if self.rect.y <= -1000:
            self.timer_add = 0
            self.time_count = 0
        if self.timer_add == 0:
            self.timer_add = 1

    def update(self):
        self.shoot_time += 0.2
        self.sprite_animation()
        self.boss_screen_time_control()
        self.ai_moves.update()



class Boss_Shoots(py.sprite.Sprite):

    def __init__(self,rect_pos):
        super().__init__()
        self.image = py.Surface((4, 17))
        self.image.fill((214,252,255))
        self.rect = self.image.get_rect(center=rect_pos)


    def shoot_move(self):
        self.rect.y += 7
    def shoot_kill(self):
        if self.rect.y > 1000:
            self.kill()

    def update(self):
        self.shoot_move()
        self.shoot_kill()

class Comets_BG(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        frame0 = py.image.load('Images/Background/Comet/comet0.png').convert_alpha()
        frame1 = py.image.load('Images/Background/Comet/comet1.png').convert_alpha()
        frame2 = py.image.load('Images/Background/Comet/comet2.png').convert_alpha()
        frame3 = py.image.load('Images/Background/Comet/comet3.png').convert_alpha()
        frame4 = py.image.load('Images/Background/Comet/comet4.png').convert_alpha()
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


class Shield(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        frame1 = py.image.load('Images/Forcefield/sprite_0.png').convert_alpha()
        frame2 = py.image.load('Images/Forcefield/sprite_1.png').convert_alpha()
        frame3 = py.image.load('Images/Forcefield/sprite_2.png').convert_alpha()
        frame4 = py.image.load('Images/Forcefield/sprite_3.png').convert_alpha()
        frame5 = py.image.load('Images/Forcefield/sprite_4.png').convert_alpha()
        frame6 = py.image.load('Images/Forcefield/sprite_5.png').convert_alpha()
        frame7 = py.image.load('Images/Forcefield/sprite_6.png').convert_alpha()
        frame8 = py.image.load('Images/Forcefield/sprite_7.png').convert_alpha()
        self.frame_list = [frame1,frame2,frame3,frame4,frame5,frame6,frame7,
                           frame8,frame7,frame6,frame5,frame4,frame3,frame2,frame1]
        self.count = 0
        self.image = self.frame_list[self.count]
        self.image = py.transform.rotozoom(self.image,0,1.5)
        self.rect = self.image.get_rect()


    def animation(self):
        self.count += 0.5
        if self.count >= len(self.frame_list):
            self.count = 0
        self.image = self.frame_list[int(self.count)]

    def update(self):
        self.image = py.transform.rotozoom(self.image, 0, 1.5)
        self.animation()

class Enemy_Horde(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size =(20,20)
        self.image = py.surface.Surface(self.size)
        self.image.fill('red')
        self.rect = self.image.get_rect(center=(10,100))
        self.shoots_group = py.sprite.Group()













