import pygame
import sys
from random import choice
from util import *



pygame.init()


width = 800
heigh = 600

screen = pygame.display.set_mode((width,heigh))
pygame.display.set_caption('Pixel Pong')


clock = pygame.time.Clock()

player_surf = pygame.Surface((20,100))
player_surf.fill('green')
player_rect = player_surf.get_rect(midleft=(10,300))



bola_surf = pygame.Surface((10,10))
bola_surf.fill('yellow')
bola_rect = bola_surf.get_rect(center = (400,300))

vidas = 3
score = 0
start_time = 0
final_score = 0
game_running = False

font = pygame.font.Font('Font/Pixeltype.ttf',50)

#vidas_surf = font.render(f'Lifes:', False, 'red')
#vidas_rect = vidas_surf.get_rect(midright=(20, 30))

font2 = pygame.font.Font('Font/Pixeltype.ttf',70)
initial_screen_surf = font2.render('Pixel Pong',False,(2, 212, 9))
initial_screen_rect = initial_screen_surf.get_rect(center=(400,300))

initial_screen_surf_2 = font_render('Press Space to start')
initial_screen_rect_2 = initial_screen_surf_2.get_rect(center=(400,360))



timer_event = pygame.USEREVENT + 1
game_timer = pygame.time.set_timer(timer_event,1200)

pygame.key.set_repeat(1,20)


def life_icons(life):


    life_surf = pygame.image.load('Images/heart_icon.png').convert_alpha()
    life_surf = pygame.transform.rotozoom(life_surf, 0, 0.25)
    dark_surf = pygame.Surface((30,30))
    dark_surf.fill('black')
    life_rect_1 = life_surf.get_rect(midleft=(30, 25))
    life_rect_2 = life_surf.get_rect(midleft=(55, 25))
    life_rect_3 = life_surf.get_rect(midleft=(80, 25))


    if life == 3:
        screen.blit(life_surf,life_rect_1)
        screen.blit(life_surf,life_rect_2)
        screen.blit(life_surf,life_rect_3)
    if life == 2:
        screen.blit(life_surf, life_rect_1)
        screen.blit(life_surf, life_rect_2)

    if life == 1:
        screen.blit(life_surf,life_rect_1)

def display_score():
    score = (int(pygame.time.get_ticks() / 1000) - start_time)
    score_text = font.render(f'Score: {score}',False,'green')
    score_rect = score_text.get_rect(center = (400,30))
    screen.blit(score_text,score_rect)
    return score


def lines():
    #Cima
    pygame.draw.lines(screen,'green',True,((0,45),(800,45)),5)
    #Baixo
    pygame.draw.lines(screen, 'green', True, ((0, 555), (800, 555)),5)


velocidade_bola = [5,2]
player_speed = [10,10]

def move_bola():
    bola_rect.x -= velocidade_bola[0]
    bola_rect.y -= velocidade_bola[1]

    if player_rect.colliderect(bola_rect):
        velocidade_bola[0] += 1
        velocidade_bola[1] += 1
        velocidade_bola[0] = - velocidade_bola[0]
        velocidade_bola[1] = + velocidade_bola[1]
        player_speed[0] += 1
        player_speed[1] += 1


    screen.blit(bola_surf,bola_rect)

while True:

    screen.fill('black')
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_running:

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                player_rect.y -= player_speed[0]

            if pressed[pygame.K_DOWN]:
                player_rect.y += player_speed[1]


        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bola_rect.center = (400, 300)
                    velocidade_bola = [5, 2]
                    vidas = 3
                    start_time = int(pygame.time.get_ticks()/1000)
                    player_rect.center = (10,300)
                    game_running = True


    if game_running:

        move_bola()
        score = display_score()
        life_icons(vidas)
        lines()

        if bola_rect.right >= 800:
            velocidade_bola[0] = -velocidade_bola[0]
        if bola_rect.top <=45 or bola_rect.bottom >= 555:
            velocidade_bola[1] = -velocidade_bola[1]
        if bola_rect.left <= 0:
            vidas -=1
            bola_rect.center = (400, 300)
            velocidade_bola = [3, 3]
        if vidas == 0:
            score = (int(pygame.time.get_ticks() / 1000))
            final_score = score
            game_running = False




        if player_rect.bottom >= 555:
            player_rect.bottom = 555

        if player_rect.top <=45:
            player_rect.top = 45


        screen.blit(player_surf,player_rect)
        #screen.blit(vidas_surf, vidas_rect)

    else:
        score_text = font.render(f'Your Score: {final_score}', False, (2, 212, 9))
        score_rect = score_text.get_rect(center=(400, 400))
        screen.fill('black')
        screen.blit(initial_screen_surf, initial_screen_rect)
        if score > 0:
            screen.blit(score_text, score_rect)

        else:
            screen.blit(initial_screen_surf_2, initial_screen_rect_2)




    pygame.display.update()
    clock.tick(60)
