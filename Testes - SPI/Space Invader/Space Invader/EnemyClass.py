import pygame
import pygame.examples.testsprite
import pygame.image
from sprites import *
from moving_AI import *
from random import uniform,randint
import math


class BossClass:
    def __init__(self,screen,player_rect,player_shoot):
        #Sprite groups
        self.screen = screen
        self.player_rect = player_rect
        self.player_shoot = player_shoot
        self.moving_speed = 5
        self.enemy_group = py.sprite.GroupSingle()
        self.enemy_group.add(BossSprite(self.player_rect,self.player_shoot))
        self.shoots = py.sprite.Group()

        #Particles
        self.collide_particles = py.sprite.Group()
        self.particles_count = 0


        # self.ai_moves = AIMoves(self.enemy_group.sprite.rect,800,500)

        #Pos control
        self.initial_pos = (500,-200)

        #Life Atributes
        self.enemy_life = 129 #129

        #Waves Controller
        self.dead_time = 0

        #Pos for the exploding sprite
        self.all_pos = []
        self.current_pos = 0,0


        #Shooting atributes
        self.shooting_speed = 2
        self.shoot_time = 0

        #Font for life display
        self.font = py.font.Font('Images/Font/slkscr.ttf', 30)


        #Exploding Frames Animation
        self.counter = 0
        self.explode_list = []
        self.get_explode_frames()
        self.explode_surf = self.explode_list[self.counter]
        self.explode_rect = self.explode_surf.get_rect(center=self.enemy_group.sprite.rect.center)
        self.frame_counter = 0
        self.frame_speed = 0.2

        #Life Bar
        self.life_bar_list = []
        self.image_loader()


        #Correct shoots
        self.correct_shoots = 0



    #Get the last pos for the explosion sprite on the same location
    def get_pos(self):

        if len(self.enemy_group) > 0:
            self.current_pos = self.enemy_group.sprite.rect.center
            self.all_pos.append(self.enemy_group.sprite.rect.center)
        else:
            self.current_pos = self.all_pos[-1]


    def get_sprite_group(self):
        return self.enemy_group


    #Append all of the 11 images related to the explosion frame
    def get_explode_frames(self):
        for i in range(11):
            path = f'Images/Spaceship/Enemy Ship/enemy_exploding/sprite_{i:02}.png'
            self.explode_list.append(pygame.image.load(path).convert_alpha())


    #Death animation
    def explode_animation(self):
        self.counter += self.frame_speed
        if self.counter >= len(self.explode_list):
            self.counter = 10
            self.frame_speed = 0
        self.explode_surf = self.explode_list[int(self.counter)]
        self.explode_rect = self.explode_surf.get_rect(center=self.current_pos)
        self.screen.blit(self.explode_surf,self.explode_rect)


    #Spawn the enemy on screen
    def enemy_spawn(self):
        self.enemy_group.draw(self.screen)
        self.enemy_group.update()


    #Shoot
    #Shoot_time = time getter to shoot in an interval (1/4 of a second)
    def shooting(self):
        self.shoot_time += self.shooting_speed

        if self.enemy_group.sprite.rect.y >= 200 and self.shoot_time % 12 == 0:
            self.shoots.add(Boss_Shoots(self.enemy_group.sprite.rect.center))
        self.shoots.draw(self.screen)
        self.shoots.update()
        for shoot in self.shoots:
            if shoot.rect.y >= 1100:
                shoot.kill()


    #Stop the shoots
    def clear_shoots(self):
        self.shoots.empty()


    #Get the initial pos to reestart the game
    def set_initial_pos(self):
        self.enemy_group.sprite.rect.center = self.initial_pos


    #Get the group of shoot sprites
    def get_shoot_group(self):
        return self.shoots

    #Colision between shoots
    def get_shoot_colision(self,sprite_group):
        for shoot in sprite_group.sprites():
            for enemy_shoot in self.shoots:
                py.sprite.spritecollide(enemy_shoot,sprite_group,True)
                py.sprite.spritecollide(shoot, self.shoots, True)


    def create_particles(self,rect):
        for _ in range(1000):
            direction = pygame.math.Vector2(uniform(1, -1), uniform(1, -1))
            direction = direction.normalize()
            end = randint(10,30)
            speed = uniform(1, end)
            self.collide_particles.add(ParticleSprite(rect.center, ('white'), direction, speed, 1))

    def update_particles(self):
        self.collide_particles.draw(self.screen)
        self.collide_particles.update()


    #Get the colision and the damage
    def get_shooted(self,sprite_group):

        for sprite in sprite_group:
            if self.enemy_group.sprite.rect.colliderect(sprite.rect):
                self.create_particles(sprite.rect)

            if py.sprite.spritecollide(self.enemy_group.sprite, sprite_group, True):

                if self.enemy_group.sprite.rect.y >= 200:
                    self.enemy_life -= 10
                return True
            return False

    def image_loader(self):

    # Append all of the 129 images related to the explosion frame
        for i in range(129, 0, -1):
            image_path = f'Images/Spaceship/Enemy Ship/Enemy_life/sprite_{i:03}.png'
            image = pygame.image.load(image_path).convert_alpha()
            self.life_bar_list.append(image)
        self.life_bar_list.append(pygame.image.load('Images/Spaceship/Enemy Ship/Enemy_life/sprite_000.png'))



    #Animates the life bar accordingly to the enemy life
    def life_bar_animation(self):
        for image_number,image in enumerate(self.life_bar_list):
            if image_number == self.enemy_life:
                life_bar_surf = image
                life_bar_rect = life_bar_surf.get_rect(center=(550,100))
                self.screen.blit(life_bar_surf,life_bar_rect)


    #Shows the life on screen by calling the life bar animation when the enemy is close
    def display_life(self):

        if self.enemy_group.sprite.rect.y >= 200:
            self.life_bar_animation()


    #Call all the methods of this class in a correct order
    def update(self,group,score):

        if self.enemy_life > 0:
            self.pos = self.get_pos()
            self.display_life()
            self.shooting()
            self.get_shoot_colision(group)
            self.get_shooted(group)
            # self.update_particles()
            self.enemy_spawn()

        elif self.enemy_life <= 0:
            score += 1000
            # self.enemy_group.sprite.kill()
            self.dead_time += 1
            if self.dead_time <= 100:
                self.explode_animation()
            self.shoots.draw(self.screen)
            self.shoots.update()
            if self.dead_time >= 100:
                self.all_pos.clear()
                return False,score
        return True,score
















