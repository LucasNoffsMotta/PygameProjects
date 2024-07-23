import pygame
from instructions import Instructions

class Text:
    def __init__(self
                 , text: str
                 , font: pygame.font.Font
                 , color: tuple
                 , pos: tuple
                 ):

        self.text = text
        self.font = font
        self.color = color
        self.pos = pos

        # Blinking (optional)
        self.blink_speed = 0.04
        self.blink_count = 0
        self.text_alpha = [255, 0]
        #Create regular text surface and rect
        self.create_rect()


    def create_rect(self,blinking=0):
        self.text_surf = self.font.render(self.text,True,self.color)
        self.text_rect = self.text_surf.get_rect(center=self.pos)
        self.text_surf.set_alpha(self.text_alpha[int(blinking)])
        print(self.text_surf.get_alpha())


    #Make text blink (optional use)
    def blinking_text(self,
                      screen: pygame.display
                      ):

        #Changing alpha value
        self.blink_count += self.blink_speed
        if self.blink_count >= len(self.text_alpha):
            self.blink_count = 0

        # Passing as an argument to the text render (make it blink):
        self.create_rect(self.blink_count)
        screen.blit(self.text_surf,self.text_rect)


    def __str__(self):
        return f'{self.text}'


class InitialScreen():
    def __init__(self, screen, main_text, subtext):
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
        if self.frame_count >= 150:
            self.subtext_blink()
            self.screen.blit(self.image2,self.rect2)



    def update(self):
        self.show_text()
        self.move_text()
        self.show_subtext()



class MainMenu(InitialScreen):
    def __init__(self,screen,main_text,subtext,subtext2,subtext3,subtext4):
        #*subtext
        self.screen = screen

        super().__init__(self.screen, ' ', ' ')
        self.initial_pos = (self.initial_pos[0],self.initial_pos[1] - 183)

        #Text
        self.subtext_str = subtext
        self.subtext2_str = subtext2
        self.subtext3_str = subtext3
        self.subtext4_str = subtext4


        self.main_text = Text(main_text, self.font1, self.color, self.initial_pos)
        self.subtext = Text(self.subtext_str,self.font2,self.color,(self.initial_pos[0],self.initial_pos[1] + 100))
        self.subtext2 = Text(self.subtext2_str,self.font2,self.color,(self.initial_pos[0],self.initial_pos[1] + 200))
        self.subtext3 = Text(self.subtext3_str, self.font2, self.color,(self.initial_pos[0], self.initial_pos[1] + 300))
        self.subtext4 = Text(self.subtext4_str,self.font2,self.color,(self.initial_pos[0],self.initial_pos[1] + 400))

        #Counter
        self.frame_counter = 1

        #Scrolling Arrow
        self.arrow_surf = pygame.image.load('Images/Horde/horder_single.png')
        self.arrow_rect1 = self.arrow_surf.get_rect(center=(360, self.initial_pos[1] + 100))
        self.arrow_rect2 = self.arrow_surf.get_rect(center=(640, self.initial_pos[1] + 100))
        self.arrow_blink = [0,255]
        self.blinking_count = 0

        #Keyboard repeat avoid
        self.key_repeat = 0
        self.key_pressed = False

        self.instructions = Instructions(self.screen,self.color)

    def show_title(self):
        self.screen.blit(self.main_text.text_surf,self.main_text.text_rect)

    def show_options(self):

        self.screen.blit(self.subtext.text_surf, self.subtext.text_rect)
        self.screen.blit(self.subtext2.text_surf, self.subtext2.text_rect)
        self.screen.blit(self.subtext3.text_surf, self.subtext3.text_rect)
        self.screen.blit(self.subtext4.text_surf,self.subtext4.text_rect)

    def show_scrolling_arrow(self):
        self.blinking_count += 0.05
        if self.blinking_count >= len(self.arrow_blink):
            self.blinking_count = 0
        self.arrow_surf.set_alpha(self.arrow_blink[int(self.blinking_count)])
        self.screen.blit(self.arrow_surf,self.arrow_rect1)
        self.screen.blit(self.arrow_surf, self.arrow_rect2)

    def move_text(self):
        self.frame_count += self.frame_counter
        if self.frame_count >= 60:
            self.main_text.text_rect.y -= self.speed
        if self.frame_count >= 90:
            self.speed = 0
            self.frame_counter = 0

    def moving_arrow(self):

        #Stops the arrow if it is at the top or bottom of the options icons
        static_pos_up = [self.initial_pos[1] + 100]
        static_pos_down = [self.initial_pos[1] + 400]

        #Check what was the selected option
        options_pos = {
            1: (self.initial_pos[1]+100),
            2: (self.initial_pos[1]+200),
            3: (self.initial_pos[1]+300),
            4: (self.initial_pos[1]+400)
        }

        #Get the user inputs
        pressed = pygame.key.get_pressed()
        arrows = [self.arrow_rect1,self.arrow_rect2]

        for rect in arrows:

            if pressed[pygame.K_DOWN] and rect.centery not in static_pos_down and self.key_repeat == 0:
                rect.centery += 100
                self.key_pressed = True

            if pressed[pygame.K_UP] and rect.centery not in static_pos_up and self.key_repeat == 0:
                rect.centery -= 100
                self.key_pressed = True


        for key,pos in options_pos.items():

                if pressed[pygame.K_RETURN] and self.arrow_rect1.centery == pos:
                    return key

        #Control the speed of the input to not scroll very fast
        if self.key_pressed:
            self.key_repeat += 1
            if self.key_repeat >= 10:
                self.key_pressed = False
                self.key_repeat = 0


    def update(self):
        self.show_title()
        self.move_text()
        if self.main_text.text_rect.centery <= 227:
            self.show_options()
            self.show_scrolling_arrow()

            choice = self.moving_arrow()

            return choice




        
class GameOver:
    def __init__(self,
                 screen: pygame.display,
                 score: int
                 ):

        self.screen = screen
        self.score = score
        self.font1 = pygame.font.Font('Images/Font/slkscr.ttf', 80)
        self.font2 = pygame.font.Font('Images/Font/slkscr.ttf', 30)
        self.color = (167,0,0)
        self.pos = (500,317)
        self.main_text = Text('Game Over',self.font1,self.color,self.pos)
        self.score_text = Text(f'Score: {self.score}',self.font2,self.color,(self.pos[0],self.pos[1] + 100))
        self.subtext = Text('Press Enter to continue',self.font2,self.color,(self.pos[0],self.pos[1] + 200))


    def show_text(self,score):
        #Update score
        self.score = score
        self.score_text = Text(f'Score: {self.score}', self.font2, self.color, (self.pos[0], self.pos[1] + 100))

        #Blit the text
        self.screen.blit(self.main_text.text_surf,self.main_text.text_rect)
        self.screen.blit(self.score_text.text_surf,self.score_text.text_rect)
        self.subtext.blinking_text(self.screen)

    def get_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RETURN]:
            return True

    def update(self,score):
        self.show_text(score)
        if self.get_input():
            return False
        return True



class Scorebord:
    def __init__(self,score):
        self.score_list = []
        self.score = score


















