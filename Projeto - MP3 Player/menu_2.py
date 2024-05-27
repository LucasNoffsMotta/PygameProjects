import sys
import pygame

pygame.init()

def mouse_colide(rect1,rect2):
    return pygame.Rect.colliderect(rect1,rect2)



def menu_secundario(width,height,font,sky_image,ground_image,clock,text_position_x,text_position_y,mouse_rect_size,snail_surface,snail_x,snail_y,snail_loop,text_surface_copyright,robot_surf,robot_rect,robot_x,robot_y):


    screen = pygame.display.set_mode((width,height))

    #Text top:
    text_surface_menu = font.render("MP3 Player", True, 'black')

    #Music menu icons:

    #Play
    play_icon_x,play_icon_y = (text_position_x - 300,text_position_y+90)
    play_icon_surface = pygame.image.load('Images/Buttoms/play_icon.png').convert_alpha()
    play_icon_rect = play_icon_surface.get_rect(topleft = (play_icon_x,play_icon_y))
    play_icon_light_up = pygame.image.load('Images/Buttoms/play_icon_light_up.png').convert_alpha()
    play_icon_light_up_rect = play_icon_light_up.get_rect(topleft = (play_icon_x,play_icon_y))


    #Pause
    pause_icon_x,pause_icon_y = (text_position_x - 150,text_position_y+90)
    pause_icon_surface = pygame.image.load('Images/Buttoms/pause_icon.png').convert_alpha()
    pause_icon_rect = pause_icon_surface.get_rect(topleft = (text_position_x - 150,text_position_y+90))
    pause_icon_light_up = pygame.image.load('Images/Buttoms/pause_icon_light_up.png').convert_alpha()
    pause_icon_light_up_rect = pause_icon_light_up.get_rect(topleft = (pause_icon_x,pause_icon_y))



    #Music options:
    #1
    music1_text = font.render('Music 1',True,'red')
    music1_text_rect = music1_text.get_rect(topleft = (text_position_x,text_position_y +50))

    #2
    music2_text = font.render('Music 2',True,'red')
    music2_text_rect = music2_text.get_rect(topleft = (text_position_x,text_position_y + 100))

    #Voltar:
    back_text = font.render('Back',True,'red')
    back_text_rect = back_text.get_rect(topleft = (text_position_x,text_position_y + 150))







    run = True
    play = False
    pause = False

    while run:


        # Mouse detect:
        mouse_pos = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], mouse_rect_size, mouse_rect_size)

        #Background
        screen.blit(sky_image,(0,0))
        screen.blit(ground_image,(0,265))

        # Snail counter:
        text_surface_score = font.render(f"Snail Loop: {snail_loop}", True, 'red')
        text_surface_score_rect = text_surface_score.get_rect(topleft=(text_position_x - 300, text_position_y))

        #Text:
        screen.blit(text_surface_menu,(text_position_x,text_position_y))
        screen.blit(music1_text,music1_text_rect)
        screen.blit(music2_text,music2_text_rect)
        screen.blit(back_text,back_text_rect)
        screen.blit(text_surface_copyright,(10,378))

        #Snail:
        snail_rect = snail_surface.get_rect(midbottom=(snail_x, snail_y))
        screen.blit(snail_surface, snail_rect)
        screen.blit(text_surface_score,text_surface_score_rect)

        #Robot:
        robot_rect = robot_surf.get_rect(midbottom =(robot_x,robot_y))
        screen.blit(robot_surf,robot_rect)

        #Play and pause:
        screen.blit(play_icon_surface, play_icon_rect)
        screen.blit(pause_icon_surface, pause_icon_rect)

        snail_x -= 5
        if snail_x < -100:
            snail_loop += 1
            snail_x = 900

        robot_x -= 5
        if robot_x < -100:
            robot_x = 900

        #Play / Pause icon light up:
        if mouse_colide(mouse_rect, play_icon_rect):
            screen.blit(play_icon_light_up, play_icon_light_up_rect)
        else:
            screen.blit(play_icon_surface, play_icon_rect)

        if mouse_colide(mouse_rect,pause_icon_light_up_rect):
            screen.blit(pause_icon_light_up,pause_icon_light_up_rect)
        else:
            screen.blit(pause_icon_surface,pause_icon_rect)


        #Text light up:
        if mouse_colide(mouse_rect,music1_text_rect):
            music1_text = font.render('Music 1', True, 'yellow')
        else:
            music1_text = font.render('Music 1', True, 'red')

        if mouse_colide(mouse_rect,music2_text_rect):
            music2_text = font.render('Music 2', True, 'yellow')
        else:
            music2_text = font.render('Music 2', True, 'red')

        if mouse_colide(mouse_rect,back_text_rect):
            back_text = font.render('Back', True, 'yellow')
        else:
            back_text = font.render('Back', True, 'red')




        for event in pygame.event.get():


            if event.type == pygame.MOUSEBUTTONUP:
                if mouse_colide(mouse_rect,back_text_rect):
                    return snail_x,snail_y,snail_loop,robot_x,robot_y

                if mouse_colide(mouse_rect,music1_text_rect):
                    play = True
                    pygame.mixer_music.load('Music/music_1.mp3')
                    pygame.mixer_music.set_volume(0.7)
                    pygame.mixer_music.play()

                if mouse_colide(mouse_rect,music2_text_rect):
                    play = True
                    pygame.mixer_music.load('Music/music_2.mp3')
                    pygame.mixer_music.set_volume(0.7)
                    pygame.mixer_music.play()

                if play and mouse_colide(mouse_rect,pause_icon_rect):
                    play = False
                    pause = True
                    pygame.mixer_music.pause()

                if pause and mouse_colide(mouse_rect,play_icon_rect):
                    play = True
                    pause = False
                    pygame.mixer_music.unpause()





            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



        pygame.display.update()

        clock.tick(60)



