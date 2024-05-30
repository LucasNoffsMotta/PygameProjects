import pygame
import sys

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
player_stand_surf_rect = player_stand_surf.get_rect(center=(400,130))

#Player Jump
gravity = 0

#Game Estate
game_running = False

#Tempo para os pontos:
game_time = 0

#Sistema de pontos

def score_display():
    game_score = int(pygame.time.get_ticks() /1000) - game_time
    game_score_surf = font.render(f'Score: {game_score}',False,(120,120,120))
    game_score_rect = game_score_surf.get_rect(center=(400,80))
    screen.blit(game_score_surf,game_score_rect)
    return game_score


def save_scores(score):
    points =str(score)
    with open('save_score.txt', 'a+') as file:
        file.write(points + '\n')
        file.close()

def append_scores():
    top_scores = list()
    with open('save_score.txt', 'r+') as file:
        line = file.readlines()
        for item in line:
            item.replace('\n','')
            top_scores.append(item)

    return top_scores


def read_scores(top_scores):
    lista_final = list()
    for score in top_scores:
        new_score = score.replace('\n','')
        lista_final.append(new_score)
    return lista_final


def ranking_pontos():
    top_scores = append_scores()
    scores_list = read_scores(top_scores)
    lista_ordem = sorted(scores_list,reverse=True)
    pos = {'primeiro':(600,100),'segundo':(600,150),'terceiro':(600,200)}
    for count, score in enumerate(lista_ordem):
        if count == 0:
            score_text_surf = font.render(f'{count +1} place:  {score} points', False, (45,43,23))
            score_text_rect = score_text_surf.get_rect(center=(pos['primeiro']))
            screen.blit(score_text_surf,score_text_rect)
        if count == 1:
            score_text_surf = font.render(f'{count + 1} place:  {score} points', False, (45, 43, 23))
            score_text_rect = score_text_surf.get_rect(center=(pos['segundo']))
            screen.blit(score_text_surf, score_text_rect)
        if count == 2:
            score_text_surf = font.render(f'{count + 1} place:  {score} points', False, (45, 43, 23))
            score_text_rect = score_text_surf.get_rect(center=(pos['terceiro']))
            screen.blit(score_text_surf, score_text_rect)







#Game Loop

while True:

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if game_running:

            if event.type == pygame.KEYDOWN and player_rect.bottom == 300:
                if event.key == pygame.K_SPACE:
                    gravity = -20

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                snail_rect.x = 700
                player_rect.x = 40
                game_time = int(pygame.time.get_ticks()/1000)
                game_running = True

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



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
        screen.blit(snail_surf,snail_rect)
        snail_rect.x -= 5
        if snail_rect.right <= 0:
            snail_rect.left = 900

        #Player
        gravity += 1
        player_rect.y += gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        #Colide Player x Snail
        if player_rect.colliderect(snail_rect):
            save_scores(score)
            game_running = False

    else:
        screen.fill((98,124,163))
        screen.blit(player_stand_surf,player_stand_surf_rect)


        #Continue text:
        continue_text = font.render('Press Space to continue',False,(64,64,64))
        continue_text_rect = continue_text.get_rect(center=(400,250))
        screen.blit(continue_text,continue_text_rect)

        #Exit text:
        end_text = font.render('Exit',False,(150,50,20))
        end_text_rect = end_text.get_rect(center=(400,300))
        screen.blit(end_text,end_text_rect)

        #Score display
        ranking_pontos()

























    pygame.display.update()
    clock.tick(60)

