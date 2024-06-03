import pygame
from util import *
import sys
from itertools import cycle

pygame.init()
width = 800
height = 600

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

def set_menu():


    #blink_event = pygame.USEREVENT + 1
    #Choice Icon
    set_icon = pygame.image.load('Images/set_icon.png').convert_alpha()
    set_icon = pygame.transform.rotozoom(set_icon,0,0.5)
    set_icon_rect = set_icon.get_rect(midright = (350,250))

    #Text
    font_base_surf = font_render('Set Dificulty')
    font_base_surf = pygame.transform.rotozoom(font_base_surf,0,1.3)
    font_base_rect = font_base_surf.get_rect(center = (400,200))

    easy_surf = font_render('Easy')
    easy_rect = easy_surf.get_rect(center = (400,250))

    medium_surf = font_render('Medium')
    medium_rect = medium_surf.get_rect(center=(400,300))

    hard_surf = font_render('Hard')
    hard_rect = hard_surf.get_rect(center =(400,350))

    crazy_surf = font_render('Crazy')
    crazy_rect = crazy_surf.get_rect(center = (400,400))


    #Mouse Settings
    mouse_rect_width = 400
    mouse_rect_height= 8

    #Menu Screen Loop
    running = True

    while running:
        #Keyboard menu set
        pygame.key.set_repeat(0)

        #Mouse Settings
        mouse_pos = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect(mouse_pos[0],mouse_pos[1],mouse_rect_width,mouse_rect_height)

        screen.fill('black')


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Mouse Selec:
            if event.type == pygame.MOUSEMOTION:
                pygame.mouse.set_visible(1)
                if mouse_rect.colliderect(easy_rect):
                    set_icon_rect.center = (300,250)

                if mouse_rect.colliderect(medium_rect):
                    set_icon_rect.center = (300,300)

                if mouse_rect.colliderect(hard_rect):
                    set_icon_rect.center = (300,350)

                if mouse_rect.colliderect(crazy_rect):
                    set_icon_rect.center = (300,400)

            if event.type == pygame.MOUSEBUTTONUP:
                if mouse_rect.colliderect(easy_rect):
                    setted = True
                    return setted,1
                if mouse_rect.colliderect(medium_rect):
                    setted = True
                    return setted,2
                if mouse_rect.colliderect(hard_rect):
                    setted = True
                    return setted,3
                if mouse_rect.colliderect(crazy_rect):
                    setted = True
                    return setted,4

            #Keyboard Select:
            if event.type == pygame.KEYDOWN:
                pygame.mouse.set_visible(0)
                if event.key == pygame.K_DOWN:
                    set_icon_rect.y += 50
                if event.key == pygame.K_UP:
                    set_icon_rect.y -= 50
                if set_icon_rect.y >= 400:
                    set_icon_rect.midright = (350,400)
                if set_icon_rect.y <= 250:
                    set_icon_rect.midright = (350,250)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if set_icon_rect.centery == 250:
                        setted = True
                        return setted, 1
                    if set_icon_rect.centery == 300:
                        setted = True
                        return setted, 2
                    if set_icon_rect.centery == 350:
                        setted = True
                        return setted, 3
                    if set_icon_rect.centery == 400:
                        setted = True
                        return setted, 4

        #Screen Elements
        screen.blit(font_base_surf, font_base_rect)
        screen.blit(easy_surf, easy_rect)
        screen.blit(medium_surf, medium_rect)
        screen.blit(hard_surf, hard_rect)
        screen.blit(crazy_surf, crazy_rect)
        screen.blit(set_icon,set_icon_rect)


        clock.tick(60)
        pygame.display.update()


def options_menu():

    #blink_event = pygame.USEREVENT + 1
    #Choice Icon
    set_icon = pygame.image.load('Images/set_icon.png').convert_alpha()
    set_icon = pygame.transform.rotozoom(set_icon,0,0.5)
    set_icon_rect = set_icon.get_rect(midright=(350,250))

    #
    options_base_surf = font_render('Options')
    options_base_surf = pygame.transform.rotozoom(options_base_surf, 0, 1.3)
    options_base_rect = options_base_surf.get_rect(center=(400, 200))

    #Text
    resume_base_surf = font_render('Resume')
    resume_base_rect = resume_base_surf.get_rect(center =(400,250))

    settings_surf = font_render('Settings')
    settings_rect = settings_surf.get_rect(center=(400,300))

    back_surf = font_render('Back')
    back_rect = back_surf.get_rect(center=(400,350))


    #Settings Sets:
    options2_base_surf = font_render('Settings')
    options2_base_surf = pygame.transform.rotozoom(options2_base_surf, 0, 1.3)
    options2_base_rect = options2_base_surf.get_rect(center=(400, 200))

    change_color_surf = font_render('Change Color')
    change_color_rect = change_color_surf.get_rect(center = (400,250))

    sound_volume_surf = font_render('Volume')
    sound_volume_rect = sound_volume_surf.get_rect(center = (400,200))




    #Mouse Settings
    mouse_rect_width = 400
    mouse_rect_height = 8

    #Menu Screen Loop
    running = True
    menu_princial = True

    while running:
        #Keyboard menu set
        pygame.key.set_repeat(0)

        #Mouse Settings
        mouse_pos = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect(mouse_pos[0],mouse_pos[1],mouse_rect_width,mouse_rect_height)

        screen.fill('black')


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if menu_princial:

                #Mouse Selec:
                if event.type == pygame.MOUSEMOTION:
                    pygame.mouse.set_visible(1)
                    if mouse_rect.colliderect(resume_base_rect):
                        set_icon_rect.center = (300,250)

                    if mouse_rect.colliderect(settings_rect):
                        set_icon_rect.center = (300,300)

                    if mouse_rect.colliderect(back_rect):
                        set_icon_rect.center = (300,350)

                if event.type == pygame.MOUSEBUTTONUP:
                    if mouse_rect.colliderect(resume_base_rect):
                        running = False

                    if mouse_rect.colliderect(settings_rect):
                        menu_princial = False



                #Keyboard Select:
                if event.type == pygame.KEYDOWN:
                    pygame.mouse.set_visible(0)
                    if event.key == pygame.K_DOWN:
                        set_icon_rect.y += 50
                    if event.key == pygame.K_UP:
                        set_icon_rect.y -= 50
                    if set_icon_rect.y >= 350:
                        set_icon_rect.midright = (350,400)
                    if set_icon_rect.y <= 250:
                        set_icon_rect.midright = (350,250)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if set_icon_rect.centery == 250:
                            running = False
            # Settings Menu
            else:
                # Mouse Selec:
                if event.type == pygame.MOUSEMOTION:
                    pygame.mouse.set_visible(1)
                    if mouse_rect.colliderect(change_color_rect):
                        set_icon_rect.center = (300, 250)

                    if mouse_rect.colliderect(sound_volume_rect):
                        set_icon_rect.center = (300, 300)

                    if mouse_rect.colliderect(back_rect):
                        set_icon_rect.center = (300, 350)

                if event.type == pygame.MOUSEBUTTONUP:
                    if mouse_rect.colliderect(resume_base_rect):
                        running = False

                    if mouse_rect.colliderect(settings_rect):
                        menu_princial = False

                # Keyboard Select:
                if event.type == pygame.KEYDOWN:
                    pygame.mouse.set_visible(0)
                    if event.key == pygame.K_DOWN:
                        set_icon_rect.y += 50
                    if event.key == pygame.K_UP:
                        set_icon_rect.y -= 50
                    if set_icon_rect.y >= 350:
                        set_icon_rect.midright = (350, 400)
                    if set_icon_rect.y <= 250:
                        set_icon_rect.midright = (350, 250)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if set_icon_rect.centery == 250:
                            running = False



        if menu_princial:
            #Screen Elements
            screen.blit(options_base_surf,options_base_rect)
            screen.blit(resume_base_surf, resume_base_rect)
            screen.blit(settings_surf, settings_rect)
            screen.blit(back_surf, back_rect)
            screen.blit(set_icon,set_icon_rect)

        else:
            screen.blit(settings_surf,settings_rect)
            screen.blit(change_color_surf,change_color_rect)
            screen.blit(sound_volume_surf,sound_volume_rect)
            screen.blit(back_surf,back_rect)





        clock.tick(60)
        pygame.display.update()








