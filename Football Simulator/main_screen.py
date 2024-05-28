import pygame
import sys
from functions import *
from lines_draw import *
from midgame_screen import *


pygame.init()
def main(minutos=0,cont=0,time_speed=10,extra=0,gols_casa_1=0,gols_fora_1=0,gols_casa_2=0,gols_fora_2=0,gols_casa_3=0,gols_fora_3=0,gols_casa_4=0,gols_fora_4=0,gols_casa_5=0,gols_fora_5=0,gols_casa_6=0,gols_fora_6=0,gols_casa_7=0,gols_fora_7=0):
    #Tela
    width = 1200
    height = 900
    screen = pygame.display.set_mode((width,height))



    #Plano de fundo e imagens:
    background = pygame.image.load('Images/background_field.png').convert_alpha()
    goal_icon = pygame.image.load('Images/goal_icon.png').convert_alpha()



    #Contador de tempo:
    font = pygame.font.Font(None,30)
    text_surf = font.render(f"Tempo: {minutos}'min ",True,'red')
    text_surf_rect = text_surf.get_rect(center = (400,50))


    #Barra de contagem:
    barra_surf = pygame.surface.Surface((300,30))
    barra_surf.fill('green')
    barra_rect = barra_surf.get_rect(center = (400,50))






    #Times:
    time1_casa,time1_fora,time2_casa,time2_fora,time3_casa,time3_fora,time4_casa,time4_fora,time5_casa,time5_fora = times()


    #Cores:
    cor_1_casa = cores_times(time1_casa)
    cor_1_fora = cores_times(time1_fora)
    cor_2_casa = cores_times(time2_casa)
    cor_2_fora = cores_times(time2_fora)
    cor_3_casa = cores_times(time3_casa)
    cor_3_fora = cores_times(time3_fora)
    cor_4_casa = cores_times(time4_casa)
    cor_4_fora = cores_times(time4_fora)
    cor_5_casa = cores_times(time5_casa)
    cor_5_fora = cores_times(time5_fora)




    #Nomes times linha 0:
    time_1casa_surf,time_1_casa_rect = team_positions(time1_casa,0,'CASA',font)
    time_1fora_surf,time1_fora_rect = team_positions(time1_fora,0,'FORA',font)


    #Nomes times linha 1:
    time2_casa_surf,time2_casa_rect = team_positions(time2_casa,1,'CASA',font)
    time2_fora_surf,time2_fora_rect = team_positions(time2_fora,1,'FORA',font)

    #Nomes times linha 2:
    time3_casa_surf,time_3_casa_rect = team_positions(time3_casa,2,'CASA',font)
    time_3_fora_surf,time_3_fora_rect = team_positions(time3_fora,2,'FORA',font)

    #Nomes times linha 3:
    time4_casa_surf,time_4_casa_rect = team_positions(time4_casa,3,'CASA',font)
    time_4_fora_surf,time_4_fora_rect = team_positions(time4_fora,3,'FORA',font)

    #Nomes times linha 4:
    time5_casa_surf,time_5_casa_rect = team_positions(time5_casa,4,'CASA',font)
    time_5_fora_surf,time_5_fora_rect = team_positions(time5_fora,4,'FORA',font)



    #Clock
    clock = pygame.time.Clock()


    #Loop:

    while True:
        screen.blit(background, (0, 0))


        #Tela


        #Contador de tempo:
        screen.blit(barra_surf, barra_rect)

        #pygame.draw.rect(screen, 'white', text_surf_rect, 10)
        #pygame.draw.rect(screen, 'white', text_surf_rect)
        text_surf = font.render(f"Tempo: {minutos}'min ", True, 'black')
        screen.blit(text_surf, text_surf_rect)





        #LINHA 0
        #Times
        pygame.draw.rect(screen, cor_1_casa, time_1_casa_rect,1000)
        screen.blit(time_1casa_surf,time_1_casa_rect)
        pygame.draw.rect(screen, cor_1_fora, time1_fora_rect)
        screen.blit(time_1fora_surf, time1_fora_rect)

        #Placares0:
        placar_casa_l1_surf,placar_casa_l1_rect = variaveis_positions(0,'Placar_casa',font,gols_casa_1,gols_fora_1,minutos)
        placar_fora_l1_surf,placar_fora_l1_rect = variaveis_positions(0,'Placar_fora',font,gols_casa_1,gols_fora_1,minutos)
        pygame.draw.rect(screen,'white',placar_casa_l1_rect)
        screen.blit(placar_casa_l1_surf,placar_casa_l1_rect)
        pygame.draw.rect(screen,'white',placar_fora_l1_rect)
        screen.blit(placar_fora_l1_surf,placar_fora_l1_rect)



        #LINHA1
        #Times linha 1
        pygame.draw.rect(screen,cor_2_casa,time2_casa_rect)
        screen.blit(time2_casa_surf,time2_casa_rect)
        pygame.draw.rect(screen,cor_2_fora,time2_fora_rect)
        screen.blit(time2_fora_surf,time2_fora_rect)

        #Placares1
        placar_casa_l2_surf,placar_casa_l2_rect = variaveis_positions(1,'Placar_casa',font,gols_casa_2,gols_fora_2,minutos)
        placar_fora_l2_surf,placar_fora_l2_rect = variaveis_positions(1,'Placar_fora',font,gols_casa_2,gols_fora_2,minutos)
        pygame.draw.rect(screen,'white',placar_casa_l2_rect)
        screen.blit(placar_casa_l2_surf,placar_casa_l2_rect)
        pygame.draw.rect(screen,'white',placar_fora_l2_rect)
        screen.blit(placar_fora_l2_surf,placar_fora_l2_rect)





        #LINHA 2
        #Times linha 2:
        pygame.draw.rect(screen,cor_3_casa,time_3_casa_rect)
        screen.blit(time3_casa_surf,time_3_casa_rect)
        pygame.draw.rect(screen,cor_3_fora,time_3_fora_rect)
        screen.blit(time_3_fora_surf,time_3_fora_rect)

        #Placares2
        placar_casa_l3_surf, placar_casa_l3_rect = variaveis_positions(2, 'Placar_casa', font, gols_casa_3, gols_fora_3,
                                                                       minutos)
        placar_fora_l3_surf, placar_fora_l3_rect = variaveis_positions(2, 'Placar_fora', font, gols_casa_3, gols_fora_3,
                                                                       minutos)
        pygame.draw.rect(screen, 'white', placar_casa_l3_rect)
        screen.blit(placar_casa_l3_surf, placar_casa_l3_rect)
        pygame.draw.rect(screen, 'white', placar_fora_l3_rect)
        screen.blit(placar_fora_l3_surf, placar_fora_l3_rect)



        # LINHA 3
        #Times linha 3:
        pygame.draw.rect(screen, cor_4_casa, time_4_casa_rect)
        screen.blit(time4_casa_surf, time_4_casa_rect)
        pygame.draw.rect(screen, cor_4_fora, time_4_fora_rect)
        screen.blit(time_4_fora_surf, time_4_fora_rect)

        # Placares3
        placar_casa_l4_surf, placar_casa_l4_rect = variaveis_positions(3, 'Placar_casa', font, gols_casa_4, gols_fora_4,
                                                                       minutos)
        placar_fora_l4_surf, placar_fora_l4_rect = variaveis_positions(3, 'Placar_fora', font, gols_casa_4, gols_fora_4,
                                                                       minutos)
        pygame.draw.rect(screen, 'white', placar_casa_l4_rect)
        screen.blit(placar_casa_l4_surf, placar_casa_l4_rect)
        pygame.draw.rect(screen, 'white', placar_fora_l4_rect)
        screen.blit(placar_fora_l4_surf, placar_fora_l4_rect)



        # LINHA 4
        pygame.draw.rect(screen, cor_5_casa, time_5_casa_rect)
        screen.blit(time5_casa_surf, time_5_casa_rect)
        pygame.draw.rect(screen, cor_5_fora, time_5_fora_rect)
        screen.blit(time_5_fora_surf, time_5_fora_rect)

        # Placares4
        placar_casa_l5_surf, placar_casa_l5_rect = variaveis_positions(4, 'Placar_casa', font, gols_casa_5, gols_fora_5,
                                                                       minutos)
        placar_fora_l5_surf, placar_fora_l5_rect = variaveis_positions(4, 'Placar_fora', font, gols_casa_5, gols_fora_5,
                                                                       minutos)
        pygame.draw.rect(screen, 'white', placar_casa_l5_rect)
        screen.blit(placar_casa_l5_surf, placar_casa_l5_rect)
        pygame.draw.rect(screen, 'white', placar_fora_l5_rect)
        screen.blit(placar_fora_l5_surf, placar_fora_l5_rect)









        #Contador de minutos e eventos do jogo:
        cont += 1
        minutos = time_counter(cont,time_speed,minutos)







        if minutos == 1:
            extra = extra_time()

        #Event item position:
        event_icon_x = 880

        #LINHA 1
        acao = jogo(time1_casa, time1_fora)
        if acao == 'gol':
            gols_casa_1 += 1
            evento_l1_surf, evento_l1_rect = variaveis_positions(0, 'Eventos', font, gols_casa_1, gols_fora_1, minutos)
            pygame.draw.rect(screen, 'white', evento_l1_rect)
            screen.blit(evento_l1_surf, evento_l1_rect)
            goal_icon_rect = goal_icon.get_rect(midright=(event_icon_x, 100))
            screen.blit(goal_icon,goal_icon_rect)


        elif acao == 'gol_fora':
            gols_fora_1 += 1
            evento_l1_surf, evento_l1_rect = variaveis_positions(0, 'Eventos', font, gols_casa_1, gols_fora_1, minutos)
            pygame.draw.rect(screen, 'white', evento_l1_rect)
            screen.blit(evento_l1_surf, evento_l1_rect)
            goal_icon_rect = goal_icon.get_rect(midright=(event_icon_x, 100))
            screen.blit(goal_icon, goal_icon_rect)


        #LINHA 2
        acao2 = jogo(time2_casa,time2_fora)
        if acao2 == 'gol':
            gols_casa_2 += 1
            evento_l1_surf, evento_l1_rect = variaveis_positions(1, 'Eventos', font, gols_casa_2, gols_fora_2, minutos)
            pygame.draw.rect(screen, 'white', evento_l1_rect)
            screen.blit(evento_l1_surf, evento_l1_rect)
            goal_icon_rect = goal_icon.get_rect(midright=(event_icon_x, 140))
            screen.blit(goal_icon, goal_icon_rect)

        elif acao2 == 'gol_fora':
            gols_fora_2 += 1
            evento_l1_surf, evento_l1_rect = variaveis_positions(1, 'Eventos', font, gols_casa_2, gols_fora_2, minutos)
            pygame.draw.rect(screen, 'white', evento_l1_rect)
            screen.blit(evento_l1_surf, evento_l1_rect)
            goal_icon_rect = goal_icon.get_rect(midright=(event_icon_x, 140))
            screen.blit(goal_icon, goal_icon_rect)


        #LINHA 3
        acao3 = jogo(time3_casa, time3_fora)
        if acao3 == 'gol':
            gols_casa_3 += 1
            evento_l3_surf, evento_l3_rect = variaveis_positions(2, 'Eventos', font, gols_casa_3, gols_fora_3, minutos)
            pygame.draw.rect(screen, 'white', evento_l3_rect)
            screen.blit(evento_l3_surf, evento_l3_rect)
            goal_icon_rect = goal_icon.get_rect(midright=(event_icon_x, 180))
            screen.blit(goal_icon, goal_icon_rect)

        elif acao3 == 'gol_fora':
            gols_fora_3 += 1
            evento_l3_surf, evento_l3_rect = variaveis_positions(2, 'Eventos', font, gols_casa_3, gols_fora_3, minutos)
            pygame.draw.rect(screen, 'white', evento_l3_rect)
            screen.blit(evento_l3_surf, evento_l3_rect)
            goal_icon_rect = goal_icon.get_rect(midright=(event_icon_x, 180))
            screen.blit(goal_icon, goal_icon_rect)

        #LINHA 4
        acao4 = jogo(time4_casa, time4_fora)
        if acao4 == 'gol':
            gols_casa_4 += 1
            evento_l4_surf, evento_l4_rect = variaveis_positions(3, 'Eventos', font, gols_casa_4, gols_fora_4,
                                                                 minutos)
            pygame.draw.rect(screen, 'white', evento_l4_rect)
            screen.blit(evento_l4_surf, evento_l4_rect)
            goal_icon_rect = goal_icon.get_rect(midright=(event_icon_x, 220))
            screen.blit(goal_icon, goal_icon_rect)

        elif acao4 == 'gol_fora':
            gols_fora_4 += 1
            evento_l4_surf, evento_l4_rect = variaveis_positions(3, 'Eventos', font, gols_casa_4, gols_fora_4,
                                                                 minutos)
            pygame.draw.rect(screen, 'white', evento_l4_rect)
            screen.blit(evento_l4_surf, evento_l4_rect)
            goal_icon_rect = goal_icon.get_rect(midright=(event_icon_x, 220))
            screen.blit(goal_icon, goal_icon_rect)


        #LINHA 5
        acao5 = jogo(time5_casa, time5_fora)
        if acao5 == 'gol':
            gols_casa_5 += 1
            evento_l5_surf, evento_l5_rect = variaveis_positions(4, 'Eventos', font, gols_casa_5, gols_fora_5,
                                                                 minutos)
            pygame.draw.rect(screen, 'white', evento_l5_rect)
            screen.blit(evento_l5_surf, evento_l5_rect)
            goal_icon_rect = goal_icon.get_rect(midright=(event_icon_x, 260))
            screen.blit(goal_icon, goal_icon_rect)

        elif acao5 == 'gol_fora':
            gols_fora_5 += 1
            evento_l5_surf, evento_l5_rect = variaveis_positions(4, 'Eventos', font, gols_casa_5, gols_fora_5,
                                                                 minutos)
            pygame.draw.rect(screen, 'white', evento_l5_rect)
            screen.blit(evento_l5_surf, evento_l5_rect)
            goal_icon_rect = goal_icon.get_rect(midright=(event_icon_x, 260))
            screen.blit(goal_icon, goal_icon_rect)


        if minutos == 45 + extra:
            midgame_screen()






        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    midgame_screen()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



        clock.tick(60)
        pygame.display.update()

main()