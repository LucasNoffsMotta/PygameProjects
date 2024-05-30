import pygame
from sys import exit

#Primeiro passo:
pygame.init()

#Segundo: Iniciar a tela

#Variavel de largura e altura:
width,height = (800,400)

#Tela:
screen = pygame.display.set_mode((width,height))

#Nome no titulo:
pygame.display.set_caption('Teste')

#Clock para controlar framerate:
clock = pygame.time.Clock()

#Imagem de fundo:
sky_surface = pygame.image.load('Images/Sky.png')

#Segunda imagem de fundo
ground_surface = pygame.image.load('Images/ground.png')

#Fonte para texto:
fonte = pygame.font.Font('Font/Pixeltype.ttf',50)


#Surface para a fonte:
text_surface = fonte.render(f'My Game',False,(64,64,64))
text_surface_rect = text_surface.get_rect(center = (400,50))

#Snail:
snail = pygame.image.load('Images/snail/snail1.png').convert_alpha()
snail_rect = snail.get_rect(midbottom = (0,300))


#Player
player_surface = pygame.image.load('Images/Player/player_walk_1.png').convert_alpha()
player_surface_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0


#Funcao para mostrar o score na tela:

game_time = 0

def display_score():
    game_score = (int(pygame.time.get_ticks() / 1000) - game_time)
    score_surf = fonte.render(f'Score: {game_score}',False,(64,64,64))
    score_rect = score_surf.get_rect(midtop = (400,70))
    screen.blit(score_surf,score_rect)






#Todo o codigo acontece dentro de um while True:

#loop do jogo
run = True

#Game estate
game_state = True



#Snail Speed
snail_speed = 5


while run:

    #Loop para checar os eventos de input:
    for event in pygame.event.get():

        if game_state:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_surface_rect.bottom == 300:
                    player_gravity = - 20

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_surface_rect.collidepoint(event.pos):
                    player_gravity = -20

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_time = pygame.time.get_ticks()
                snail_rect.right = 800
                game_state = True

        #Checa se o evento foi um input no botao de exit:
        if event.type == pygame.QUIT:
            #Encerrando pygame:
            pygame.quit()
            #Encerrando o loop:
            exit()

    if game_state:
        # Desenhando a superficie na tela:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        # Snail
        screen.blit(snail, snail_rect)

        # Text
        pygame.draw.rect(screen, (192, 232, 236), text_surface_rect)
        pygame.draw.rect(screen, (192, 232, 236), text_surface_rect, 10)
        screen.blit(text_surface, text_surface_rect)

        #Score
        display_score()

        # Snail move
        snail_rect.left -= snail_speed
        if snail_rect.left < -72:
            snail_rect.right = 800

        #Player
        player_gravity += 1
        player_surface_rect.y += player_gravity
        if player_surface_rect.bottom >= 300:
            player_surface_rect.bottom = 300
        screen.blit(player_surface, player_surface_rect)

        #Colision:
        if player_surface_rect.colliderect(snail_rect):
            game_state = False

    else:
        screen.fill('black')








    #Atualiza a tela(abaixo dos outros comandos do loop):
    pygame.display.update()
    #Chamando o clock:
    clock.tick(60)



