import pygame
import sys
from random import randint

pygame.init()

#Tela:
width = 800
height = 400
screen = pygame.display.set_mode((width,height))

#Clock
clock = pygame.time.Clock()

#Font /Text
font = pygame.font.Font('Font/Pixeltype.ttf',40)
my_game_text = font.render('My Game',False,(64,64,64))
my_game_text_rect = my_game_text.get_rect(center = (400,50))


#Background images
ground = pygame.image.load('Images/ground.png').convert_alpha()
sky = pygame.image.load('Images/Sky.png')


#Snail images
snail_surf = pygame.image.load('Images/snail/snail1.png')
snail_rect = snail_surf.get_rect(midbottom=(600,300))

#Player image
player_surf = pygame.image.load('Images/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(50,300))

#Player Stand
player_stand_surf = pygame.image.load('Images/Player/player_stand.png').convert_alpha()
player_stand_surf = pygame.transform.rotozoom(player_stand_surf,0,2)
player_stand_surf_rect = player_stand_surf.get_rect(center=(400,190))

#Initial Screen
start_text = font.render('Press Space to start',False,(111,196,169))
start_text_rect = start_text.get_rect(center=(400,320))
game_name_text= font.render('Pixel Runner',False,(111,196,169))
game_name_rect = game_name_text.get_rect(center = (400,60))



#Player Jump
gravity = 0

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


def move_enemy(enemy_list):
    if enemy_list:
        for rect in enemy_list:
            rect.x -= randint(2,7)
            screen.blit(snail_surf,rect)
        return enemy_list
    else:
        return []





def score_display():
    game_score = int(pygame.time.get_ticks() /1000) - game_time
    game_score_surf = font.render(f'Score: {game_score}',False,(120,120,120))
    game_score_rect = game_score_surf.get_rect(center=(400,80))
    screen.blit(game_score_surf,game_score_rect)
    return game_score











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

            if event.type == obastacle_timer:
                enemy_list.append(snail_surf.get_rect(bottomright=(randint(900,1200),300)))








        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                snail_rect.x = 700
                player_rect.x = 40
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
        gravity += 1
        player_rect.y += gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        #Colide Player x Snail
        if player_rect.colliderect(snail_rect):
            game_running = False
        enemy_list = move_enemy(enemy_list)




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

