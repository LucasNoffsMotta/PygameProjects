import pygame
import sys
from random import randint

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk1 = pygame.image.load('../Images/Player/player_walk_1.png').convert_alpha()
        player_walk2 = pygame.image.load('../Images/Player/player_walk_2.png').convert_alpha()
        player_jump = pygame.image.load('../Images/Player/jump.png').convert_alpha()
        self.player_walk = [player_walk1, player_walk2]
        self.player_jump = player_jump
        self.player_index = 0
        self.image = self.player_walk[self.player_index]

        self.rect = self.image.get_rect(midbottom=(300,300))
        self.gravity = 0

    def player_input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.rect.bottom == 300:
            self.gravity = -20

    def apply_gravity(self):

        self.gravity += 1
        self.rect.y += self.gravity

        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def player_animation(self):

        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[(int(self.player_index))]



    def update(self):
        self.player_input()
        self.apply_gravity()
        self.player_animation()


class Enemy(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'fly':
            fly1 = pygame.image.load('../Images/Fly/Fly1.png').convert_alpha()
            fly2 = pygame.image.load('../Images/Fly/Fly2.png').convert_alpha()
            self.frames = [fly1, fly2]
            y_pos = 210
        else:
            snail1 = pygame.image.load('../Images/snail/snail1.png').convert_alpha()
            snail2 = pygame.image.load('../Images/snail/snail2.png').convert_alpha()
            self.frames = [snail1, snail2]
            y_pos = 300


        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(100,200),y_pos))

    def animation(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation()







#Tela:
width = 800
height = 400
screen = pygame.display.set_mode((width,height))

#Clock
clock = pygame.time.Clock()

#Font /Text
font = pygame.font.Font('../Font/Pixeltype.ttf', 40)
my_game_text = font.render('My Game',False,(64,64,64))
my_game_text_rect = my_game_text.get_rect(center = (400,50))


#Background images
ground = pygame.image.load('../Images/ground.png').convert_alpha()
sky = pygame.image.load('../Images/Sky.png')


#Snail images
snail_surf1 = pygame.image.load('../Images/snail/snail1.png').convert_alpha()
snail_surf2 = pygame.image.load('../Images/snail/snail2.png').convert_alpha()
snail_surf_list = [snail_surf1,snail_surf2]
snail_index = 0
snail_surf = snail_surf_list[snail_index]


#snail_rect = snail_surf.get_rect(midbottom=(600,300))

#Fly Image
fly_surface1 =pygame.image.load('../Images/Fly/Fly1.png').convert_alpha()
fly_surface2 = pygame.image.load('../Images/Fly/Fly2.png').convert_alpha()
fly_list = [fly_surface1,fly_surface2]
fly_index = 0
fly_surface = fly_list[fly_index]
fly_y_move = -5


#Player image
player_walk1 = pygame.image.load('../Images/Player/player_walk_1.png').convert_alpha()
player_walk2 = pygame.image.load('../Images/Player/player_walk_2.png')
player_walk = [player_walk1,player_walk2]
player_index = 0

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (40,300))

player_jump = pygame.image.load('../Images/Player/jump.png')
#player_rect = player_surf.get_rect(midbottom=(50,300))

#Player Stand
player_stand_surf = pygame.image.load('../Images/Player/player_stand.png').convert_alpha()
player_stand_surf = pygame.transform.rotozoom(player_stand_surf,0,2)
player_stand_surf_rect = player_stand_surf.get_rect(center=(400,190))

#Initial Screen
start_text = font.render('Press Space to start',False,(111,196,169))
start_text_rect = start_text.get_rect(center=(400,320))
game_name_text= font.render('Pixel Runner',False,(111,196,169))
game_name_rect = game_name_text.get_rect(center = (400,60))



#Player Jump
player_gravity = 0

#Game Estate
game_running = False

#Tempo para os pontos:
game_time = 0

#Sistema de pontos
score = 0

#Enemy Spawn

#Enemy List
enemy_list = []

#Enemy Timer
obastacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obastacle_timer,900)

#Animation Timer
snail_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_timer,500)

fly_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_timer,200)




def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]



def move_enemy(enemy_list):
    global fly_y_move

    if enemy_list:
        for rect in enemy_list:
            rect.x -= 5
            if rect.bottom == 300:
                screen.blit(snail_surf,rect)
            else:
                fly_y_move += 0.1
                rect.y += fly_y_move
                if fly_y_move >= 5:
                    fly_y_move = -5

                screen.blit(fly_surface,rect)
        return enemy_list
    else:
        return []


def collisions(player,obstacles):
    if obstacles:
        for rect in obstacles:
            if player.colliderect(rect):
                return False
    return True





def score_display():
    game_score = int(pygame.time.get_ticks() /1000) - game_time
    game_score_surf = font.render(f'Score: {game_score}',False,(120,120,120))
    game_score_rect = game_score_surf.get_rect(center=(400,80))
    screen.blit(game_score_surf,game_score_rect)
    return game_score



player = pygame.sprite.GroupSingle()
player.add(Player())

obstacles = pygame.sprite.Group()




#Game Loop

while True:

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_running:

            if event.type == pygame.KEYDOWN and player_rect.bottom == 300:
                if event.key == pygame.K_SPACE:
                    gravity = -20

                if event.key == pygame.K_w:
                    gravity = -35



            if event.type == obastacle_timer:
                if randint(0,2):
                    obstacles.add(Enemy('Snail'))
                    enemy_list.append(snail_surf.get_rect(bottomright=(randint(900,1200),300)))
                else:
                    enemy_list.append(fly_surface.get_rect(bottomright=(randint(900,1200),210)))

            if event.type == snail_timer:
                if snail_index == 0: snail_index = 1
                else:
                    snail_index = 0
                snail_surf = snail_surf_list[snail_index]

            if event.type == fly_timer:
                if fly_index == 0: fly_index = 1
                else:
                    fly_index = 0
                fly_surface = fly_list[fly_index]


        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #    snail_rect.x = 700
                player_rect.midbottom = (40,300)
                enemy_list.clear()
                game_time = int(pygame.time.get_ticks()/1000)
                game_running = True





    if game_running:

        #Background
        screen.blit(ground,(0,300))
        screen.blit(sky,(0,0))

        #Text
        pygame.draw.rect(screen,(192, 232, 236),my_game_text_rect)
        screen.blit(my_game_text,my_game_text_rect)

        #Score display
        score = score_display()

        #Snail
        #screen.blit(snail_surf,snail_rect)
        #snail_rect.x -= 10
        #if snail_rect.right <= 0:
        #    snail_rect.left = 900

        #Player



        #player_rect.y += gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        player_animation()

        screen.blit(player_surf,player_rect)

        #Enemy Spawn
        enemy_list = move_enemy(enemy_list)

        #Colisions
        game_running = collisions(player_rect,enemy_list)

        player.draw(screen)
        player.update()
        obstacles.draw(screen)
        obstacles.update()



    else:
        screen.fill((98,124,163))
        screen.blit(player_stand_surf,player_stand_surf_rect)

        #Score display
        game_score_text = font.render(f'Game Score: {score}', False, (111, 196, 169))
        game_score_rect = game_score_text.get_rect(center=(400, 350))
        screen.blit(game_name_text, game_name_rect)
        if score > 0:
            screen.blit(game_score_text,game_score_rect)
        else:
            # Continue text:
            screen.blit(start_text, start_text_rect)

























    pygame.display.update()
    clock.tick(60)

