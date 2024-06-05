import pygame
import sys
from random import choice,randint

pygame.init()

#Screen
width = 800
height = 400
screen = pygame.display.set_mode((width,height))

#game_status
game_active = False

#clock /score
clock = pygame.time.Clock()
inicio = 0
score = 0

#background
ground = pygame.image.load('Images/ground.png').convert_alpha()
sky = pygame.image.load('Images/Sky.png').convert_alpha()
ground_floor = 300

#text
#Colors
text_color = (64,64,64)
text_rect_color = (192, 232, 236)
pause_screen_color = (98,124,163)
pause_text_color =(111,196,169)

#Surface/Rect
font = pygame.font.Font('Font/Pixeltype.ttf',40)
text_surf = font.render("My Game",False,(text_color))
text_rect = text_surf.get_rect(midbottom = (400,50))
game_score_pos = (400, 70)


#Initial Screen
start_text = font.render('Press Space to start',False,(pause_text_color))
start_text_rect = start_text.get_rect(center=(400,320))
game_name_text= font.render('Pixel Runner',False,(pause_text_color))
game_name_rect = game_name_text.get_rect(center = (400,70))


#name
pygame.display.set_caption('Pixel Dodge')




#Sprites / Classes / Functions

#Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #Player Images
        player1 = pygame.image.load('Images/Player/player_walk_1.png').convert_alpha()
        player2 = pygame.image.load('Images/Player/player_walk_2.png').convert_alpha()
        self.jump = pygame.image.load('Images/Player/jump.png').convert_alpha()
        self.stand = pygame.image.load('Images/Player/player_stand.png').convert_alpha()

        #Animation
        self.player_moves = [player1,player2]
        self.player_index = 0
        self.image = self.player_moves[self.player_index]
        self.rect = self.image.get_rect(midbottom=(40,ground_floor))

        #Gravity Set
        self.player_gravity = 0

        #Sound
        self.jump_sound = pygame.mixer.Sound('Sounds/jump.mp3')
        self.jump_sound.set_volume(0.5)


    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.rect.bottom == ground_floor:
            pygame.mixer.Sound.play(self.jump_sound)
            self.player_gravity = -20

    def aply_gravity(self):

        self.player_gravity += 1
        self.rect.y += self.player_gravity
        if self.rect.bottom >= ground_floor: self.rect.bottom = ground_floor


    def animation(self):

        if self.rect.bottom < ground_floor:
            self.image = self.jump

        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_moves):
                self.player_index = 0
            self.image = self.player_moves[int(self.player_index)]

    def update(self):
        self.player_input()
        self.aply_gravity()
        self.animation()


#Enemies
class Obstacles(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'snail':
            snail1 = pygame.image.load('Images/snail/snail1.png').convert_alpha()
            snail2 = pygame.image.load('Images/snail/snail2.png').convert_alpha()
            self.frames_list = [snail1,snail2]
            y_pos = ground_floor
        else:
            fly1 = pygame.image.load('Images/Fly/Fly1.png').convert_alpha()
            fly2 = pygame.image.load('Images/Fly/Fly2.png').convert_alpha()
            self.frames_list = [fly1,fly2]
            y_pos = 210

        self.index = 0
        self.image = self.frames_list[self.index]
        self.rect = self.image.get_rect(midbottom=(randint(900,1200),y_pos))

    def obs_animation(self):
        self.index += 0.1
        if self.index >= len(self.frames_list):
            self.index = 0
        self.image = self.frames_list[int(self.index)]



    def update(self):
        self.rect.x -= 10
        self.obs_animation()
        self.destroy()


    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

def display_score():
    score = int(pygame.time.get_ticks()/1000) - inicio
    score_text = font.render(f'Score: {score}',False,text_color)
    score_rect = score_text.get_rect(center = game_score_pos)
    screen.blit(score_text,score_rect)
    return score

def sprite_colision():
    if pygame.sprite.spritecollide(player.sprite,obstacle,False):
        obstacle.empty()
        return False
    return True



#Sprites Groups
player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle = pygame.sprite.Group()

#Obstacles timer
obs_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obs_timer,900)


#Music
music = pygame.mixer.Sound('Sounds/music.wav')
music.set_volume(0.1)
music.play(loops=-1)


while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_active:

            if event.type == obs_timer:
                if randint(0,2):
                    obstacle.add(Obstacles(choice(['snail','snail','snail','fly'])))


        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    score = int(pygame.time.get_ticks()/1000) - inicio




    if game_active:
        screen.blit(sky,(0,0))
        screen.blit(ground,(0,ground_floor))
        player.draw(screen)
        player.update()
        obstacle.draw(screen)
        obstacle.update()
        score = display_score()
        pygame.draw.rect(screen,text_rect_color,text_rect)
        screen.blit(text_surf, text_rect)
        game_active = sprite_colision()

    else:
        screen.fill(pause_screen_color)
        pause_image = pygame.image.load('Images/Player/player_stand.png').convert_alpha()
        pause_image = pygame.transform.rotozoom(pause_image,0,2)
        pause_rect = pause_image.get_rect(center = (400,200))

        if score > 0:
            final_score_text = font.render(f'Your Score: {score}',False,text_color)
            final_score_rect = final_score_text.get_rect(center = (400,350))
            screen.blit(final_score_text,final_score_rect)

        screen.blit(pause_image, pause_rect)
        screen.blit(game_name_text, game_name_rect)
        screen.blit(start_text, start_text_rect)








    clock.tick(60)
    pygame.display.update()
