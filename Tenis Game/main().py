import pygame
import sys
from random import choice
from util import *
from game_mode import *


pygame.init()

#Tela
width = 800
heigh = 600
screen = pygame.display.set_mode((width,heigh))
screen_rect =screen.get_rect()

pygame.display.set_caption('Pixel Pong')

#FPS
clock = pygame.time.Clock()

#Player 1
player_surf = pygame.Surface((20,100))
player_surf.fill('green')
player_rect = player_surf.get_rect(midleft=(10,300))

#Player 2
player2_rect = player_surf.get_rect(midright=(790,300))


#Bola
bola_surf = pygame.Surface((10,10))
bola_surf.fill('yellow')
bola_rect = bola_surf.get_rect(center = (400,400))

#Variables

#Booleans
game_running = False
win_status = False
setted = False

#Movement
velocidade_bola = [4,2]
vel = 2
player_speed = [10,10]

#Score and time set
start_time = 0
score1 = 0
score2 = 0
winner = ' '


#Fonte
font = pygame.font.Font('Font/Pixeltype.ttf',50)

#Textos
font2 = pygame.font.Font('Font/Pixeltype.ttf',90)
initial_screen_surf = font2.render('Pixel Pong',False,(2, 212, 9))
initial_screen_rect = initial_screen_surf.get_rect(midbottom=(400,250))
initial_screen_surf_2 = font_render('Press Space to start')
initial_screen_rect_2 = initial_screen_surf_2.get_rect(midbottom=(400,300))

#Timer
timer_event = pygame.USEREVENT + 1
game_timer = pygame.time.set_timer(timer_event,1200)

#Input Teclado
pygame.key.set_repeat(1,20)


#Functions
def display_time():
    time = int(pygame.time.get_ticks()/1000) - start_time
    time_text = font.render(f'Time: {time}',False,'green')
    time_rect = time_text.get_rect(center = (400,30))
    screen.blit(time_text,time_rect)

def display_scores(score1,score2):
    font_3 = pygame.font.Font('Font/Pixeltype.ttf',40)
    #Score1:
    score1_surf = font_3.render(f'{score1}',False,(255, 209, 59))
    score1_rect = score1_surf.get_rect(midleft = (150,30))

    #Score2:
    score2_surf = font_3.render(f'{score2}',False,(255, 209, 59))
    score2_rect = score2_surf.get_rect(midright = (650,30))

    screen.blit(score1_surf,score1_rect)
    screen.blit(score2_surf,score2_rect)

def lines():
    #Cima
    pygame.draw.lines(screen,'green',True,((0,45),(800,45)),5)
    #Baixo
    pygame.draw.lines(screen, 'green', True, ((0, 555), (800, 555)),5)

def move_bola():
    bola_rect.x -= velocidade_bola[0]
    bola_rect.y -= velocidade_bola[1]
    screen.blit(bola_surf, bola_rect)

def colide_p1(vel):
    if player_rect.colliderect(bola_rect):
        velocidade_bola[0] = vel
        velocidade_bola[0] = - velocidade_bola[0]
        velocidade_bola[1] = + velocidade_bola[1]

def colide_p2(vel):
    if player2_rect.colliderect(bola_rect):
        velocidade_bola[0] = -vel
        velocidade_bola[0] = - velocidade_bola[0]
        velocidade_bola[1] = + velocidade_bola[1]

def display_winner(winner):
    winner_text = font.render(f'Winner: {winner}', False, (235, 219, 52))
    winner_rect = winner_text.get_rect(center=(400,400))
    screen.blit(winner_text, winner_rect)


while True:

    screen.fill('black')


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_running:

            #Movendo Players
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                player2_rect.y -= player_speed[0]

            if pressed[pygame.K_DOWN]:
                player2_rect.y += player_speed[1]

            if pressed[pygame.K_w]:
                player_rect.y -= player_speed[0]

            if pressed[pygame.K_s]:
                player_rect.y += player_speed[1]

            #Esc
            if pressed[pygame.K_ESCAPE]:
                #Back to the dificulty choice menu:
                options_menu()
                #Setting back the start conditionals:




        #Eventos Tela inicial(Game not running):
        else:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #Starting Game
                    bola_rect.center = (400, 300)
                    vidas = 3
                    score1 = score2 = 0
                    start_time = int(pygame.time.get_ticks()/1000)
                    player_rect.center = (10,300)
                    game_running = True


    if game_running:

        if not setted:
            setted, dif = set_menu()
            vel = move_mode(dif)
            start_time = int(pygame.time.get_ticks() / 1000)
            pygame.key.set_repeat(1, 20)

        else:
        #Game Running
            move_bola()
            colide_p1(vel)
            colide_p2(vel)
            display_time()
            display_scores(score1,score2)

            #life_icons(vidas)
            lines()

        #Ball Mechanic
        #Player 1 point
        if bola_rect.right >= 800:
            score1 += 1
            bola_rect.center = (400,300)
            velocidade_bola[0] = 4


        #Top and bottom kicks
        if bola_rect.top <=45 or bola_rect.bottom >= 555:
            velocidade_bola[1] = -velocidade_bola[1]

        #Player 2 Point
        if bola_rect.left <= 0:
            velocidade_bola[0] = 4
            score2 += 1
            bola_rect.center = (400, 300)




        #Game Over
        if score1 ==10 or score2 == 10:
            if score1 == 10:
                winner = 'Player 1'
            if score2 == 10:
                winner = 'Player 2'

            #End of the game
            score1 = 0
            score2 = 0
            win_status = True
            start_time = int(pygame.time.get_ticks() / 1000)
            game_running = False
            setted = False

        #Players Screen Limit:

        #Player 1
        if player_rect.bottom >= 555:
            player_rect.bottom = 555

        if player_rect.top <= 45:
            player_rect.top = 45

        #Player 2
        if player2_rect.top <= 45:
            player2_rect.top = 45

        if player2_rect.bottom >= 555:
            player2_rect.bottom = 555


        screen.blit(player_surf,player_rect)
        screen.blit(player_surf,player2_rect)
        #screen.blit(vidas_surf, vidas_rect)


    #Tela Inicial - Game not running
    else:
        screen.fill('black')
        screen.blit(initial_screen_surf, initial_screen_rect)

        if win_status:
            display_winner(winner)
            screen.blit(initial_screen_surf_2, initial_screen_rect_2)

        else:
            screen.blit(initial_screen_surf_2, initial_screen_rect_2)


    #FPS
    pygame.display.update()
    clock.tick(60)
