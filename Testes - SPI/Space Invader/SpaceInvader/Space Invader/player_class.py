import pygame as py
from sprites import *
from shield_class import *
from random import choice,uniform,randint




class Player():
    def __init__(self,screen):

        #Shield Class Atributes
        self.screen = screen
        self.font = py.font.Font('Images/Font/slkscr.ttf',40)
        self.player_shield_initial_time = 6

        #Self atributes
        self.sprite_group = py.sprite.GroupSingle()
        self.shoots_group = py.sprite.Group()
        self.sprite_group.add(PlayerSprite())

        #Bomb
        self.particles_group = py.sprite.Group()
        self.bomb_surf = py.Surface((10, 10))
        py.draw.circle(self.bomb_surf, 'red', (5, 5), 5)
        self.bomb_speed = 5
        self.bomb_pos = self.sprite_group.sprite.rect.center
        self.bomb_rect = self.bomb_surf.get_rect(center=self.bomb_pos)
        self.bomb_launched = False
        self.bomb_timer = 7
        self.timer = 0
        self.bomb_counting = self.bomb_timer - self.timer
        self.animation_count = 0


        #Shield + Recoil
        self.shield = ShieldGroup(self.screen,self.font,self.sprite_group.sprite)
        self.life = 6
        self.shoot_recoil = 0
        self.recoil_add = 1
        self.recoil = 60

        #Explosion Colors:
        self.color1 = (218,60,29)
        self.color2 = (85,15,10)
        self.color3 = (230,123,51)

        #Shooted Atributes
        self.hit_timer = 0
        self.shooted = False
        self.damage_particles = py.sprite.Group()

        #All particles groups
        self.particles = [self.particles_group,self.damage_particles]



    def activate_shield(self):
        pressed = py.key.get_pressed()

        if pressed[py.K_s]:
            self.player_shield_initial_time = self.shield.get_show_timer()

            # Show the shield if time > 0:
            if self.player_shield_initial_time > 0:
                self.shield.update(self.player_shield_initial_time)


    def get_colision(self,boss_shoots_group,horde_shoots):
        side = choice([-5, 15])

        if self.sprite_group.sprite.image.get_alpha() < 255:
            self.shooted = True
        else:
            self.shooted = False


        #Boss Hits
        if py.sprite.spritecollide(self.sprite_group.sprite,boss_shoots_group, True) and not self.shooted:
            self.life -= 1
            self.sprite_group.sprite.rect.x += side
            for _ in range(1000):
                particles_pos = self.sprite_group.sprite.rect.center
                particles_color = 'white'
                direction = pygame.math.Vector2(uniform(1, -1), uniform(1, -1))
                direction = direction.normalize()
                speed = uniform(1, 20)
                self.damage_particles.add(ParticleSprite(particles_pos, particles_color, direction, speed, 10))
            return True

        #Horde Hits
        if py.sprite.spritecollide(self.sprite_group.sprite,horde_shoots, True) and not self.shooted:
            self.life -= 1
            self.sprite_group.sprite.rect.x += side
            for _ in range(100):
                particles_pos = self.sprite_group.sprite.rect.center
                particles_color = 'white'
                direction = pygame.math.Vector2(uniform(1, -1), uniform(1, -1))
                direction = direction.normalize()
                speed = uniform(1, 20)
                self.damage_particles.add(ParticleSprite(particles_pos, particles_color, direction, speed, 5))
            return True

        #Shielding
        py.sprite.spritecollide(self.shield.sprite,horde_shoots,True)
        py.sprite.spritecollide(self.shield.sprite,boss_shoots_group,True)
        return False


    def life_bar(self):

        life_bar1 = py.image.load('Images/life_bar/life bar-1.png.png').convert_alpha()
        life_bar2 = py.image.load('Images/life_bar/life bar-2.png.png').convert_alpha()
        life_bar3 = py.image.load('Images/life_bar/life bar-3.png.png').convert_alpha()
        life_bar4 = py.image.load('Images/life_bar/life bar-4.png').convert_alpha()
        life_bar5 = py.image.load('Images/life_bar/life bar-5.png').convert_alpha()
        life_bar6 = py.image.load('Images/life_bar/life bar-6.png').convert_alpha()

        show_life = {
            6: life_bar1,
            5: life_bar2,
            4: life_bar3,
            3: life_bar4,
            2: life_bar5,
            1: life_bar6
        }

        for num, image in show_life.items():
            if self.life == num:
                surf = show_life[num]
                rect = surf.get_rect(center=(500,830))
                self.screen.blit(surf, rect)



    def get_rect(self):
        return self.sprite_group.sprite.rect

    def get_shoot(self):
        return self.shoots_group

    def get_bomb_rect(self):
        return self.bomb_rect

    def get_particles_rect(self):
        return self.particles_group


    def shooting(self,horde_size):

        self.shoot_recoil += self.recoil_add
        pressed = py.key.get_pressed()

        if horde_size == 9:
            self.recoil = 30

        if horde_size == 10:
            self.recoil = 15

        if pressed[py.K_SPACE] and self.shoot_recoil >= self.recoil:
            self.shoots_group.add(Shoots_left(), Shoots_right())
            self.shoot_recoil = 0


    def bomb_shooting(self):
        pressed = py.key.get_pressed()
        self.bomb_counting = self.bomb_timer - self.timer


        if not self.bomb_launched:
            if pressed[py.K_CAPSLOCK]:
                self.bomb_rect.center = self.sprite_group.sprite.rect.center
                # self.
                self.bomb_launched = True


        if self.bomb_launched:

            self.timer += 0.1
            self.bomb_rect.y -= self.bomb_speed

            if self.bomb_counting > 0:
                self.screen.blit(self.bomb_surf, self.bomb_rect)

            if self.bomb_counting <= 0:
                for _ in range(1000):
                    particles_pos = self.bomb_rect.center
                    particles_color = choice((self.color1,self.color2,self.color3))
                    direction = pygame.math.Vector2(uniform(1, -1), uniform(1, -1))
                    direction = direction.normalize()
                    speed = uniform(90,100)
                    self.particles_group.add(ParticleSprite(particles_pos, particles_color, direction, speed,10))
                self.timer = 0
                self.bomb_rect.center = self.sprite_group.sprite.rect.center
                self.bomb_launched = False


    def update(self,boss_shoots_group,horde_shoots,horde_size):
        if self.life > 0:
            self.life_bar()
            self.sprite_group.draw(self.screen)
            colided = self.get_colision(boss_shoots_group, horde_shoots)
            self.sprite_group.update(colided)
            self.shooting(horde_size)
            self.bomb_shooting()
            self.activate_shield()
            self.shoots_group.draw(self.screen)
            self.shoots_group.update()
            for group in self.particles:
                group.draw(self.screen)
                group.update()
            return True
        return False














