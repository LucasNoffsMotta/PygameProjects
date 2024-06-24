import pygame

class Menu():
    def __init__(self,screen,main_text,subtext):
        #Main Atributes
        self.screen = screen
        self.font1 = pygame.font.Font('Images/Font/slkscr.ttf',80)
        self.font2 = pygame.font.Font('Images/Font/slkscr.ttf',30)
        #Main Text
        self.main_text = main_text
        self.subtext = subtext
        self.color = (0,76,200)
        self.initial_pos = (500,500)
        self.image = self.font1.render(self.main_text, True, self.color)
        self.rect = self.image.get_rect(center=self.initial_pos)
        #Subtext
        self.animation_count = 0
        self.text2_color = [self.color,'black']
        self.frame_count = 0
        self.speed = 3

    def show_text(self):
        self.screen.blit(self.image,self.rect)

    def move_text(self):
        self.frame_count += 1
        if self.frame_count >= 60:
            self.rect.y -= self.speed
        if self.frame_count >= 120:
            self.speed = 0

    def subtext_blink(self):
        self.animation_count += 0.04
        if self.animation_count >= len(self.text2_color):
            self.animation_count = 0
        self.image2 = self.font2.render(self.subtext, True, self.text2_color[int(self.animation_count)])
        self.rect2 = self.image2.get_rect(center=(500, self.rect.centery + 200))


    def show_subtext(self):
        if self.frame_count >=150:
            self.subtext_blink()
            self.screen.blit(self.image2,self.rect2)







