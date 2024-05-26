import pygame
import sys
from functions import jogo
from lines_draw import team_positions
from lines_draw import cores_times
from lines_draw import variaveis_positions


pygame.init()

#Tela
width = 1200
height = 900
screen = pygame.display.set_mode((width,height))

#Variaveis:
gols_casa_1 = 0
gols_fora_1 = 0
gols_casa_2 = 0
gols_fora_2 = 0
gols_casa_3 = 0
gols_fora_3 = 0
minutos = 0
cont = 0

#Plano de fundo:
background = pygame.image.load('Images/background.png').convert_alpha()


#Contador de tempo:
font = pygame.font.Font(None,30)
text_surf = font.render(f"Tempo: {minutos}'min ",True,'red')
text_surf_rect = text_surf.get_rect(center = (400,50))

#Times:
time1_casa ='Corinthans'
time1_fora = 'Flamengo'
time2_casa = 'Cruzeiro'
time2_fora = 'Santos'
time3_casa = 'Vasco'
time3_fora = 'Fluminense'

#Cores:
cor_1_casa = cores_times(time1_casa.upper())
cor_1_fora = cores_times(time1_fora.upper())
cor_2_casa = cores_times(time2_casa.upper())
cor_2_fora = cores_times(time2_fora.upper())
cor_3_casa = cores_times(time3_casa.upper())
cor_3_fora = cores_times(time3_fora.upper())




#Nomes times linha 0:
#1:
time_1casa_surf,time_1_casa_rect = team_positions('CORINTHANS',0,'CASA',font)
time_1fora_surf,time1_fora_rect = team_positions('FLAMENGO',0,'FORA',font)


#Nomes times linha 1:
time2_casa_surf,time2_casa_rect = team_positions('CRUZEIRO',1,'CASA',font)
time2_fora_surf,time2_fora_rect = team_positions('SANTOS',1,'FORA',font)

#Nomes times linha 2:
time3_casa_surf,time_3_casa_rect = team_positions('VASCO',2,'CASA',font)
time_3_fora_surf,time_3_fora_rect = team_positions('FLUMINENSE',2,'FORA',font)



#Clock
clock = pygame.time.Clock()


#Loop:
screen.blit(background, (0, 0))

while True:
    #Tela

    #Contador de tempo:
    pygame.draw.rect(screen, 'white', text_surf_rect, 10)
    pygame.draw.rect(screen, 'white', text_surf_rect)
    text_surf = font.render(f"Tempo: {minutos}'min ", True, 'black')
    screen.blit(text_surf,text_surf_rect)



    #LINHA 1
    #Times
    pygame.draw.rect(screen, cor_1_casa, time_1_casa_rect)
    screen.blit(time_1casa_surf,time_1_casa_rect)
    pygame.draw.rect(screen, cor_1_fora, time1_fora_rect)
    screen.blit(time_1fora_surf, time1_fora_rect)

    #Placares1:
    placar_casa_l1_surf,placar_casa_l1_rect = variaveis_positions(0,'Placar_casa',font,gols_casa_1,gols_fora_1,minutos)
    placar_fora_l1_surf,placar_fora_l1_rect = variaveis_positions(0,'Placar_fora',font,gols_casa_1,gols_fora_1,minutos)
    pygame.draw.rect(screen,'white',placar_casa_l1_rect)
    screen.blit(placar_casa_l1_surf,placar_casa_l1_rect)
    pygame.draw.rect(screen,'white',placar_fora_l1_rect)
    screen.blit(placar_fora_l1_surf,placar_fora_l1_rect)



    #LINHA2
    #Times linha 2
    pygame.draw.rect(screen,cor_2_casa,time2_casa_rect)
    screen.blit(time2_casa_surf,time2_casa_rect)
    pygame.draw.rect(screen,cor_2_fora,time2_fora_rect)
    screen.blit(time2_fora_surf,time2_fora_rect)

    #Placares2
    placar_casa_l2_surf,placar_casa_l2_rect = variaveis_positions(1,'Placar_casa',font,gols_casa,gols_fora,minutos)
    placar_fora_l2_surf,placar_fora_l2_rect = variaveis_positions(1,'Placar_fora',font,gols_casa,gols_fora,minutos)
    pygame.draw.rect(screen,'white',placar_casa_l2_rect)
    screen.blit(placar_casa_l2_surf,placar_casa_l2_rect)
    pygame.draw.rect(screen,'white',placar_fora_l2_rect)
    screen.blit(placar_fora_l2_surf,placar_fora_l2_rect)






    #LINHA 3
    #Times linha 3:
    pygame.draw.rect(screen,cor_3_casa,time_3_casa_rect)
    screen.blit(time3_casa_surf,time_3_casa_rect)
    pygame.draw.rect(screen,cor_3_fora,time_3_fora_rect)
    screen.blit(time_3_fora_surf,time_3_fora_rect)






    #Contador de minutos e eventos do jogo:
    cont += 1
    if cont % 10 == 0:
        minutos += 1

        #LINHA 1
        acao = jogo(time1_casa, time1_fora)
        if acao == 'gol':
            gols_casa += 1
            evento_l1_surf, evento_l1_rect = variaveis_positions(0, 'Eventos', font, gols_casa, gols_fora, minutos)
            pygame.draw.rect(screen, 'white', evento_l1_rect)
            screen.blit(evento_l1_surf, evento_l1_rect)

        elif acao == 'gol_fora':
            gols_fora += 1
            evento_l1_surf, evento_l1_rect = variaveis_positions(0, 'Eventos', font, gols_casa, gols_fora, minutos)
            pygame.draw.rect(screen, 'white', evento_l1_rect)
            screen.blit(evento_l1_surf, evento_l1_rect)

        #LINHA 2
        acao2 = jogo(time2_casa,time2_fora)
        if acao2 == 'gol':
            gols_casa += 1
            evento_l1_surf, evento_l1_rect = variaveis_positions(1, 'Eventos', font, gols_casa, gols_fora, minutos)
            pygame.draw.rect(screen, 'white', evento_l1_rect)
            screen.blit(evento_l1_surf, evento_l1_rect)

        elif acao2 == 'gol_fora':
            gols_fora += 1
            evento_l1_surf, evento_l1_rect = variaveis_positions(1, 'Eventos', font, gols_casa, gols_fora, minutos)
            pygame.draw.rect(screen, 'white', evento_l1_rect)
            screen.blit(evento_l1_surf, evento_l1_rect)






    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    clock.tick(60)
    pygame.display.update()