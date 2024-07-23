import sys
from sprites import Comets_BG
import pygame


class Instructions:

    def __init__(self,screen,color):
        self.screen = screen
        self.color = color

        self.animation_count = 0
        self.animation_speed = 0.015
        self.animation_alpha = [255,0]

        # How to play images
        # Fonts
        self.keybord_font = pygame.font.Font('Images/Font/slkscr.ttf', 10)
        self.instruction_font = pygame.font.Font('Images/Font/slkscr.ttf', 20)

        # Move
        self.kmove_pos = (270, 290)
        self.keybord_move_image = pygame.image.load('Images/Keybord/kmove1.png').convert_alpha()
        self.keybord_move_rect = self.keybord_move_image.get_rect(center=self.kmove_pos)
        self.move_keybord_text = self.instruction_font.render('Move', True, self.color)

        # Spacebar
        # self.mouse_pos = pygame.mouse.get_pos()
        self.kspace_pos = (440, 305)
        self.keybord_spacebar_image = pygame.image.load('Images/Keybord/kspace1.png').convert_alpha()
        self.keybord_spacebar_rect = self.keybord_spacebar_image.get_rect(center=self.kspace_pos)
        self.keybord_spacebar_text = self.keybord_font.render('Space', True, 'white')
        self.keybord_spacebar_image.blit(self.keybord_spacebar_text, (50, 10))
        self.shoot_text = self.instruction_font.render('Shoot', True, self.color)

        # CapsLock
        self.kcaps_pos = (600, 306)
        self.keybord_caps_image = pygame.image.load('Images/Keybord/kcaps.png').convert_alpha()
        self.keybord_caps_rect = self.keybord_caps_image.get_rect(center=self.kcaps_pos)
        self.keybord_caps_text = self.keybord_font.render('Caps', True, 'white')
        self.keybord_caps_image.blit(self.keybord_caps_text, (10, 10))
        self.bomb_text = self.instruction_font.render('Bomb', True, self.color)

        # S
        self.kspos = (736, 307)
        self.keybord_s_image = pygame.image.load('Images/Keybord/ks.png').convert_alpha()
        self.keybord_s_rect = self.keybord_s_image.get_rect(center=self.kspos)
        self.keybord_s_text = self.keybord_font.render('S', True, 'white')
        self.keybord_s_image.blit(self.keybord_s_text, (10, 10))
        self.shield_text = self.instruction_font.render('Shield', True, self.color)

        #Esc
        self.escpos = (50, 800)
        self.keybord_esc_image = pygame.image.load('Images/Keybord/ks.png').convert_alpha()
        self.keybord_esc_image = pygame.transform.rotozoom(self.keybord_esc_image,0,1.2)
        self.keybord_esc_rect = self.keybord_s_image.get_rect(center=self.escpos)
        self.keybord_esc_text = self.keybord_font.render('Esc', True, 'white')

        self.keybord_esc_image.blit(self.keybord_esc_text, (7, 12))
        self.back_text = self.instruction_font.render('Back', True, self.color)
        self.back_rect = self.back_text.get_rect(center=(self.escpos[0] + 5,self.escpos[1] + 40))






        # Score instructions
        #Horde
        self.epos = (160,570)
        self.enemy_image = pygame.image.load('Images/Horde/horder_single.png').convert_alpha()
        self.enemy_image = pygame.transform.rotozoom(self.enemy_image, 0, 3)
        self.enemy_rect = self.enemy_image.get_rect(center=(self.epos))
        self.enemy_text = self.instruction_font.render('10 pts', True, self.color)

        #Boss
        self.bpos = (360,570)
        self.boss_image = pygame.image.load('Images/Spaceship/Enemy Ship/enemy_stand.png').convert_alpha()
        self.boss_image = pygame.transform.rotozoom(self.boss_image, 0, 0.4)
        self.boss_rect = self.boss_image.get_rect(center=self.bpos)
        self.boss_text = self.instruction_font.render('1000 pts', True, self.color)

        #Gem Images
        self.bluepos = (460,570)
        self.blue_gem_image = pygame.image.load('Images/LuckyGems/blue_gem-1.png.png').convert_alpha()
        self.blue_gem_image = pygame.transform.rotozoom(self.blue_gem_image, 0, 4)
        self.blue_gem_rect = self.blue_gem_image.get_rect(center=self.bluepos)



    def animation(self,image_surf,image_rect):
        self.animation_count += self.animation_speed
        if self.animation_count >= len(self.animation_alpha):
            self.animation_count = 0
        image_surf.set_alpha(self.animation_alpha[int(self.animation_count)])
        self.screen.blit(image_surf,image_rect)


    def show_images(self):
        # Images
        # Move

        self.screen.blit(self.keybord_move_image, self.keybord_move_rect)
        self.screen.blit(self.move_keybord_text, (self.kmove_pos[0] - 29, self.kmove_pos[1] + 50))

        # Shoot
        self.keybord_spacebar_rect = self.keybord_spacebar_image.get_rect(center=self.kspace_pos)
        self.screen.blit(self.keybord_spacebar_image, self.keybord_spacebar_rect)
        self.screen.blit(self.shoot_text, (self.kspace_pos[0] - 35, self.kspace_pos[1] + 35))

        # Bomb
        self.screen.blit(self.keybord_caps_image, self.keybord_caps_rect)
        self.screen.blit(self.bomb_text, (self.kcaps_pos[0] - 30, self.kcaps_pos[1] + 35))

        # Shield
        self.keybord_s_rect = self.keybord_s_image.get_rect(center=self.kspos)
        self.screen.blit(self.keybord_s_image, self.keybord_s_rect)
        self.screen.blit(self.shield_text, (self.kspos[0] - 30, self.kspos[1] + 35))


        # Horde icon
        self.enemy_rect = self.enemy_image.get_rect(center=self.epos)
        self.screen.blit(self.enemy_image, self.enemy_rect)
        self.screen.blit(self.enemy_text, (self.epos[0] - 35, self.epos[1] + 35))

        #Boss Icon
        self.screen.blit(self.boss_image,self.boss_rect)
        self.screen.blit(self.boss_text, (self.bpos[0] - 55, self.bpos[1] + 35))


        #Esc
        # self.screen.blit(self.keybord_esc_image,self.keybord_esc_rect)
        self.animation(self.keybord_esc_image,self.keybord_esc_rect)
        self.animation(self.back_text,self.back_rect)




class InstructionsLoop:
    def __init__(self,screen,background,background_comet):
        self.screen = screen
        self.background = background
        self.color = (0,76,200)
        self.instructions = Instructions(self.screen,self.color)
        self.clock = pygame.time.Clock()
        self.background_comet = background_comet
        self.comet_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.comet_event, 5000)



    def main_loop(self):
        instructions = True

        while instructions:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == self.comet_event:
                    self.background_comet.add(Comets_BG())

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True

            self.screen.blit(self.background, (0, 0))
            self.instructions.show_images()
            self.background_comet.draw(self.screen)
            self.background_comet.update()
            self.clock.tick(60)
            pygame.display.update()





