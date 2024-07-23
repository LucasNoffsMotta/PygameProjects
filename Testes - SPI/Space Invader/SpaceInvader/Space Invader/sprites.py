import pygame as py
from random import randint, choice
from moving_AI import *
import pygame.key


py.init()

#Position reference for different sprites
start_position = [540,750]  #Reference to: Player center position, shoots center position (shoots_pos = start_position[1] -10)
#boss_position = [540,50]


#Player Sprites
class PlayerSprite(py.sprite.Sprite):

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
        self.shooted = False
        self.colision_index = 180
        self.alpha_list = [254,0]
        self.alpha_list_index = 0
        self.image.set_alpha(255)
        self.blinking_time = 0



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


    def blinking_animation(self):

        self.blinking_time += 1

        if 0 < self.blinking_time <= 180:

            self.alpha_list_index += 0.05
            if self.alpha_list_index >= len(self.alpha_list):
                self.alpha_list_index = 0

            self.image.set_alpha(self.alpha_list[int(self.alpha_list_index)])

        else:
            self.blinking_time = 0
            self.alpha_list_index = 0
            self.shooted = False


    def colide_animation(self,colide):

        if colide:
            self.shooted = True

        if self.shooted:
            self.blinking_animation()
        else:
            self.image.set_alpha(255)



    def stay_map(self):

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right >= 980:
            self.rect.right = 980

        if self.rect.y <= 500:
            self.rect.y = 500
            start_position[1] = self.rect.center[1] - 10


        if self.rect.y >= 700:
            self.rect.y = 700
            start_position[1] = self.rect.center[1] - 10


    def update(self,colide):

        py.key.set_repeat(0)
        self.input()
        self.rect.x += self.balance_direction
        start_position[0] = self.rect.x
        self.animation()
        self.colide_animation(colide)
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
        if self.rect.y < -40:
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
        if self.rect.y < -40:
            self.kill()

    def update(self):
        self.shoot_move()
        self.shoot_kill()


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

class BossSprite(py.sprite.Sprite):
    def __init__(self,player_rect,player_shoot):
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
        self.player_shoot = player_shoot
        self.ai_moves = AIMoves(self.rect, 800, 500,self.player_rect,self.player_shoot)


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
        if self.rect.y > 1000 or self.rect.x < -100:
            print('comet KILLED')
            self.kill()


    def update(self):
        self.comet_animation()
        self.comet_move()
        self.comet_del()

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

class HordeSprite(py.sprite.Sprite):
    def __init__(self,player_rect,screen):
        super().__init__()
        self.image = py.image.load('Images/Horde/horder_single.png').convert_alpha()
        self.image = py.transform.rotozoom(self.image,0,3)
        self.rect = self.image.get_rect(center=(50,100))

        self.shoots_group = py.sprite.Group()
        self.shooting_odd = 100
        self.screen = screen
        self.player_rect = player_rect

class LuckyCoinSprite(py.sprite.Sprite):
    def __init__(self,color,pos,speed):
        super().__init__()
        self.color = color
        self.images = []
        self.yellow_image = py.image.load('Images/LuckyGems/yellow_gem-1.png.png').convert_alpha()
        self.red_image = py.image.load('Images/LuckyGems/red_gem-1.png.png').convert_alpha()
        self.green_image = py.image.load('Images/LuckyGems/green_gem-1.png.png').convert_alpha()
        self.blue_image = py.image.load('Images/LuckyGems/blue_gem-1.png.png').convert_alpha()
        self.images = [self.yellow_image,self.red_image,self.green_image,self.blue_image]

        for image in self.images:
            py.transform.rotozoom(image,0,2)

        if self.color == 'yellow':
            self.image = self.yellow_image
        if self.color == 'red':
            self.image = self.red_image
        if self.color == 'green':
            self.image = self.green_image
        if self.color == 'blue':
            self.image = self.blue_image

        self.pos = pos
        self.rect = self.image.get_rect(center =pos)
        self.speed = speed

    def moving(self):
        self.rect.y += self.speed

    def coin_del(self):
        if self.rect.y >= 1000:

            self.kill()

    def update(self):
        self.moving()
        self.coin_del()




class ParticleSprite(py.sprite.Sprite):
    def __init__(self,pos,color,direction,speed,fade_speed):
        super().__init__()
        self.pos = pos
        self.start_pos = pos
        self.color = color
        self.direction = direction
        self.speed = speed
        self.get_surface()
        self.moving = 0
        self.alpha = 255
        self.fadespeed = fade_speed

    def get_surface(self):
        self.image = py.Surface((2,2)).convert_alpha()
        self.image.set_colorkey('black')
        py.draw.circle(self.image, self.color, center=(2, 2), radius=2)
        self.rect = self.image.get_rect(center=self.pos)

    def move(self):
        self.pos += self.direction * self.speed * (60/1000)
        self.rect.center = self.pos
        self.moving += 1

    def fade(self):
        self.alpha -= self.fadespeed
        self.image.set_alpha(self.alpha)

    def kill_particle(self):
         if self.alpha <= 0:
            self.kill()


    def update(self):
        self.move()
        if self.moving >= 25:
            self.fade()
        self.kill_particle()
























