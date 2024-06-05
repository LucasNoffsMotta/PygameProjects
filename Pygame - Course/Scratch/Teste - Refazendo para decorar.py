import pygame
import sys
from random import randint

pygame.init()

#Tela
width = 800
height = 400
screen = pygame.display.set_mode((width,height))

class player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        player_1 = pygame.image.load('../Images/Player/player_walk_1.png').convert_alpha()
        player_2 = pygame.image.load('../Images/Player/player_walk_2.png').convert_alpha()
        self.jump = pygame.image.load('../Images/Player/jump.png').convert_alpha()
        self.player_states = [player_1, player_2]
        self.player_index = 0


        self.image = self.player_states[self.player_index]
        self.rect = self.image.get_rect(midbottom = (30,300))
        self.player_gravity = 0


    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom == 300:
            self.player_gravity = -20


    def gravity(self):

        self.player_gravity += 1

        self.rect.y += self.player_gravity

        if self.rect.bottom >= 300:
            self.rect.bottom = 300



    def animation(self):

        if self.rect.bottom < 300:
            self.image = self.jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_states):
                self.player_index = 0
            self.image = self.player_states[int(self.player_index)]

    def update(self):
        self.player_input()
        self.gravity()
        self.animation()




class obstacles(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if type == 'Snail':
            snail_surf1 = pygame.image.load('../Images/snail/snail1.png').convert_alpha()
            snail_surf2 = pygame.image.load('../Images/snail/snail2.png').convert_alpha()
            self.list = [snail_surf1, snail_surf2]
            self.index = 0
            self.image = snail_surfs[snail_index]
            self.rect = self.image.get_rect(center=(randint(900, 1200), 300))
        if type == 'Fly':
            fly_surface1 = pygame.image.load('../Images/Fly/Fly1.png').convert_alpha()
            fly_surface2 = pygame.image.load('../Images/Fly/Fly2.png').convert_alpha()
            self.list = [fly_surface1, fly_surface2]
            self.index = 0
            self.image = self.list[self.index]
            self.rect = self.image.get_rect(center=(randint(900, 1200), 230))




    def image_animation(self):
        self.index += 0.1
        if self.index > len(self.list):
            self.index = 0
        self.image = self.list[int(self.index)]

    def move(self):
        self.rect.x -= 5


    def update(self):
        self.image_animation()
        self.move()






#Game Estate
game_active = True


#Clock
clock = pygame.time.Clock()


#Background
ground_background = pygame.image.load('../Images/ground.png')
sky_background = pygame.image.load('../Images/Sky.png')


#Snail
snail_surf1 = pygame.image.load('../Images/snail/snail1.png').convert_alpha()
snail_surf2 = pygame.image.load('../Images/snail/snail2.png').convert_alpha()
snail_surfs = [snail_surf1,snail_surf2]
snail_index = 0
snail_surf = snail_surfs[snail_index]
snail_rect = snail_surf.get_rect(midbottom = (600,300))

#Fly
fly_surface1 = pygame.image.load('../Images/Fly/Fly1.png').convert_alpha()
fly_surface2 = pygame.image.load('../Images/Fly/Fly2.png').convert_alpha()
fly_surfs = [fly_surface1,fly_surface2]
fly_index = 0
fly_surf = fly_surfs[fly_index]


#Player Class
Player = pygame.sprite.GroupSingle()
Player.add(player())

#Enemy Class
enemies = pygame.sprite.Group()




#Text:
font = pygame.font.Font('../Font/Pixeltype.ttf', 40)
text_surf = font.render("My Game",False,(64,64,64))
text_rect = text_surf.get_rect(midbottom = (380,50))


pygame.display.set_caption('My Game')


#Player
#player_walk1 = pygame.image.load('Images/Player/player_walk_1.png').convert_alpha()
#player_walk2 = pygame.image.load('Images/Player/player_walk_2.png').convert_alpha()
#player_walk = [player_walk1,player_walk2]
#player_index = 0
#player_surf = player_walk[player_index]
#player_rect = player_surf.get_rect(midbottom =(40,300))
#player_rect = player_surf.get_rect(midbottom = (50,300))
#player_gravity = 0

#player_jump = pygame.image.load('Images/Player/jump.png')


#Intro Screen
player_stand = pygame.image.load('../Images/Player/player_stand.png')
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))



#Funcao para mostrar a pontuacao na tela:
score = 0
start_time = 0

def display_score():
    game_time = (int(pygame.time.get_ticks() / 1000) - start_time)
    score_surf = font.render(f'Score: {game_time}',False,(150,64,40))
    score_rect = score_surf.get_rect(midtop = (380,70))
    screen.blit(score_surf,score_rect)

#Enemy Spawn
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer,1200)
enemy_list = []

#Snail Animation Timer
snail_event = pygame.USEREVENT + 2
pygame.time.set_timer(snail_event,500)

#Fly Animation Event
fly_event = pygame.USEREVENT + 3
pygame.time.set_timer(fly_event,200)



def enemy_spawn(enemy_list):
    if enemy_list:
        for rect in enemy_list:
            rect.x -= 5
            if rect.bottom == 300:
                screen.blit(snail_surf,rect)
            else:
                screen.blit(fly_surf,rect)
            enemy_list = [rect for rect in enemy_list if rect.x > -100]
        return enemy_list
    else:
        return []

def collision(player,spawn_list):

    if spawn_list:
        for enemy in spawn_list:
            if player.colliderect(enemy):
                return False
    return True



#def player_animation():
   # global player_surf,player_index


  #  if player_rect.bottom < 300:
       #= #player_jump
    #else:
     #   player_index += 0.1
       # if player_index >= len(player_walk):
      #      player_index = 0
       # else:
            #player_surf = player_walk[int(player_index)]




while True:

    # Mouse Position:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_active:
           # if event.type == pygame.KEYDOWN:
               # if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
             #       player_gravity = -20
              #  if event.key == pygame.K_LEFT:
               #     player_rect.x -= 20
               # if event.key == pygame.K_RIGHT:
               #     player_rect.x += 20



            #if event.type == pygame.mouse.get_pressed():
                ##if player_rect.collidepoint(mouse_pos):
                #    player_gravity = -30

            if event.type == enemy_timer:
                if randint(0,2):
                    enemies.add(obstacles('Snail'))
                    #enemy_list.append(snail_surf.get_rect(bottomright = (randint(900,1200),300)))
                    #enemy_list.append(fly_surf.get_rect(bottomright = (randint(900,1200),230)))

            if event.type == snail_event:
                if snail_index == 0: snail_index = 1
                else:
                    snail_index = 0
                snail_surf = snail_surfs[int(snail_index)]

            if event.type == fly_event:
                if fly_index == 0: fly_index = 1
                else:
                    fly_index = 0
                fly_surf = fly_surfs[fly_index]


        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
                #player_rect.midbottom = (40,300)
                enemy_list.clear()
                snail_rect.x = 600


    if game_active:
        #Background
        screen.blit(sky_background,(0,0))
        screen.blit(ground_background,(0,300))
        #Text
        pygame.draw.rect(screen, (192, 232, 236), text_rect)
        screen.blit(text_surf,text_rect)
        Player.draw(screen)
        Player.update()
        #Snail


       # screen.blit(snail_surf,snail_rect)
       # snail_rect.x -= 5
       # if snail_rect.right < 0:
        #    snail_rect.left = 900
        #Player:
        #player_animation()

       # player_gravity += 1
       # player_rect.y += player_gravity

       # if player_rect.bottom >= 300:
       #     player_rect.bottom = 300
       # screen.blit(player_surf,player_rect)

        display_score()


        #Collision:

        enemy_list = enemy_spawn(enemy_list)
        #game_active = collision(player_rect, enemy_list)



    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)


    clock.tick(60)
    pygame.display.update()
