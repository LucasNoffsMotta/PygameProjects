import pygame
import sys

pygame.init()

#Tela
width = 800
height = 400
screen = pygame.display.set_mode((width,height))


#Game Estate
game_active = True


#Clock
clock = pygame.time.Clock()


#Background
ground_background = pygame.image.load('Images/ground.png')
sky_background = pygame.image.load('Images/Sky.png')


#Snail
snail_surf = pygame.image.load('Images/snail/snail1.png')
snail_rect = snail_surf.get_rect(midbottom = (600,300))

#Text:
font = pygame.font.Font('Font/Pixeltype.ttf',40)
text_surf = font.render("My Game",False,(64,64,64))
text_rect = text_surf.get_rect(midbottom = (380,50))


pygame.display.set_caption('My Game')


#Player
player_surf = pygame.image.load('Images/Player/player_stand.png')
player_rect = player_surf.get_rect(midbottom = (50,300))
player_gravity = 0

#Intro Screen
player_stand = pygame.image.load('Images/Player/player_stand.png')
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



while True:

    # Mouse Position:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
                if event.key == pygame.K_LEFT:
                    player_rect.x -= 20
                if event.key == pygame.K_RIGHT:
                    player_rect.x += 20



            if event.type == pygame.mouse.get_pressed():
                if player_rect.collidepoint(mouse_pos):
                    player_gravity = -30

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
                player_rect.x = 50
                snail_rect.x = 600





        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    if game_active:
        #Background
        screen.blit(sky_background,(0,0))
        screen.blit(ground_background,(0,300))
        #Text
        pygame.draw.rect(screen, (192, 232, 236), text_rect)
        screen.blit(text_surf,text_rect)
        #Snail
        screen.blit(snail_surf,snail_rect)
        snail_rect.x -= 5
        if snail_rect.right < 0:
            snail_rect.left = 900
        #Player:
        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        display_score()
        #Collision:

        if player_rect.colliderect(snail_rect):
            game_active = False
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)


    clock.tick(60)
    pygame.display.update()
