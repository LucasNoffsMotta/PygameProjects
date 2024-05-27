import pygame
import sys
from menu_2 import menu_secundario
from robot_smoke import smoke


pygame.init()
pygame.mixer.init()

#Tela:
width,height = 800,400
screen = pygame.display.set_mode((width,height))


#Fontes:
font = pygame.font.Font('Font/Pixeltype.ttf',45)
fonte_copyright = pygame.font.Font('Font/Pixeltype.ttf',30)




#Static text:
#Menu Icon
text_surface_menu = font.render("MP3 Player",True,'black')
text_position_x = 395
text_position_y = 40

#Copyright:
text_surface_copyright = fonte_copyright.render('Lucas Studios Inc - 2024  @Copyright',True,'black')


#Interactive text:
snail_loop = 0
text_surface_play = font.render("Play Music",True,'red')
text_surface_exit = font.render("Exit",True,'red')
text_surface_score = font.render(f"Snail Loop: {snail_loop}",True,'red')

#Text rect:
text_surface_play_rect = text_surface_play.get_rect(topleft = (text_position_x,text_position_y +50))
text_surface_exit_rect = text_surface_exit.get_rect(topleft = (text_position_x,text_position_y +100))
text_surface_score_rect = text_surface_score.get_rect(topleft = (text_position_x - 300,text_position_y))


#Robot Smoke:
smoke1_surf = pygame.image.load('Images/Player/fumacinha_1.png')
smoke2_surf = pygame.image.load('Images/Player/fumacinha 2.png')
smoke3_surf = pygame.image.load('Images/Player/fumacinha 3.png')
smoke4_surf = pygame.image.load('Images/Player/fumacinha 4.png')


#Mouse(size and collision detect):
mouse_rect_size = 8



def mouse_colide(rect1,rect2):
    return pygame.Rect.colliderect(rect1,rect2)



#Fundo:
sky_image = pygame.image.load('Images/Sky.png').convert_alpha()
ground_image = pygame.image.load('Images/ground.png').convert_alpha()
ground_y = 265


#Snail Image:
snail_surface = pygame.image.load('Images/snail/snail1.png').convert_alpha()
snail_x = 0
snail_y = 265


#Robot Image:
robot_x = 150
robot_y = 265
robot_surface = pygame.image.load('Images/Player/robot.png').convert_alpha()
robot_rect = robot_surface.get_rect(midbottom = (robot_x,robot_y))




#Window name:
pygame.display.set_caption('MP3 Player')




#Clock:
clock = pygame.time.Clock()


#Loop principal:
while True:

    #Mouse detect:
    mouse_pos = pygame.mouse.get_pos()
    mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], mouse_rect_size, mouse_rect_size)

    #Background:
    screen.blit(sky_image, (0, 0))
    screen.blit(ground_image, (0, 265))


    #Snail:
    snail_rect = snail_surface.get_rect(midbottom=(snail_x, snail_y))
    screen.blit(snail_surface, snail_rect)

    #Robot:
    robot_rect = robot_surface.get_rect(midbottom = (robot_x,robot_y))
    screen.blit(robot_surface,robot_rect)




    #Text:
    text_surface_score = font.render(f"Snail Loop: {snail_loop}", True, 'red')
    screen.blit(text_surface_menu,(text_position_x,text_position_y))
    screen.blit(text_surface_play,text_surface_play_rect)
    screen.blit(text_surface_exit,text_surface_exit_rect)
    screen.blit(text_surface_score,text_surface_score_rect)
    screen.blit(text_surface_copyright,(10,378))


    if mouse_colide(mouse_rect,text_surface_play_rect):
        text_surface_play = font.render("Play Music", True, 'yellow')
    else:
        text_surface_play = font.render("Play Music", True, 'red')

    if mouse_colide(mouse_rect,text_surface_exit_rect):
        text_surface_exit = font.render("Exit", True, 'yellow')
    else:
        text_surface_exit = font.render("Exit",True,'red')






    snail_x -= 5
    robot_x -= 5
    #smoke1_rect,smoke2_rect = smoke(smoke1_surf,smoke2_surf,robot_x,robot_y)
    #screen.blit(smoke1_surf,smoke1_rect)
    #screen.blit(smoke2_surf,smoke2_rect)


    if snail_x < -100:
        snail_loop += 1
        snail_x = 900


    if robot_x < -100:
        robot_x = 900



    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONUP:
            if mouse_colide(mouse_rect,text_surface_play_rect):
                snail_x,snail_y,snail_loop,robot_x,robot_y = menu_secundario(width,height,font,sky_image,ground_image,clock,text_position_x,text_position_y,mouse_rect_size,snail_surface,snail_x,snail_y,snail_loop,text_surface_copyright,robot_surface,robot_rect,robot_x,robot_y)


            if mouse_colide(mouse_rect,text_surface_exit_rect):
                pygame.quit()
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer_music.set_volume(0)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
    clock.tick(60)







