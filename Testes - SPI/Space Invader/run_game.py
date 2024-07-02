import pygame as py
from random import randint, choice
import pygame.display
from sprites import *
import sys
from methods import *
from shield_class import *
from menu_class import *
from EnemyClass import *
from horde_class import *


#Functions that handle collisions of sprite classes

#Detect Sprite Colision between Player and other objects
def player_collision():

    side = choice([-5, 15])

    if py.sprite.spritecollide(player.sprite,asteroids,False):
        player.sprite.rect.x += side
        return True

    if py.sprite.spritecollide(player.sprite,boss.get_shoot_group(),True):
        player.sprite.rect.x += side
        return True

    return False

#Detect Collision Between Asteroid and Shoot - Kills both sprites
def asteroid_killing():
    #Game Score
    global points
    for sprite in shoots.sprites():
        if py.sprite.spritecollide(sprite,asteroids,False):
            #Calls the explosion Sprite
            generic_explosion_animation(shoots,asteroids,explosion_animation)
            sprite.kill()
            points += 10

# Generic Sprite Explosion Frame
def generic_explosion_animation(group1,group2,group3):

    #Colisao entre grupos de sprites com mais de um sprite dentro
    #Group1: Rect que causa a explosao (ex: tiro que bate no asteroide)
    #Group2: Rect que ira explodir (ex: asteroide que foi acertado)
    #Group3: Sprite da explosao

    if len(group1) > 1:
        for sprite1 in group1:
            for sprite2 in group2:
                if sprite2.rect.colliderect(sprite1):
                    group3.sprite.rect.center = sprite2.rect.center
                    group3.draw(screen)
                    group3.update()
                    py.sprite.spritecollide(sprite1, group2, True)

    else:
        # Colisao com grupos de sprite single (boss,player)
        for sprite1 in group1:
            for sprite2 in group2:
                if sprite2.rect.colliderect(sprite1):
                    group3.sprite.rect.center = sprite1.rect.center
                    group3.draw(screen)
                    group3.update()
                    sprite1.rect.x += 5
                    sprite1.rect.x -= 5
                    py.sprite.spritecollide(sprite1, group2, True)


#Screen
pygame.init()
width = 1000
height = 920
screen = py.display.set_mode((width, height))

#Sprites Class Call // Objects Assignment
player = py.sprite.GroupSingle()
player.add(Player())
asteroids = py.sprite.Group()
shoots = py.sprite.Group()
explode = py.sprite.GroupSingle()
explode.add(Player_Explosion())
explosion_animation = py.sprite.GroupSingle()
explosion_animation.add(Asteroid_Explosion())
boss = Enemy(screen,player.sprite.rect)
comets = py.sprite.Group()
shield_player = ShieldGroup(screen, font, player.sprite)
menu_screen = Menu(screen,'Space Invaders','Press Space to start')
horde = EnemyHorde(screen,shoots)




#Game State
game_state = False
points = 0
player_life = 6



#BG
background = py.image.load('Images/Background/background_2.png').convert_alpha()


#FPS
clock = py.time.Clock()


#Event for asteroid spawn
spawn_event = py.USEREVENT + 1
py.time.set_timer(spawn_event,100)


#Event for boss shoots load
shoot_event = py.USEREVENT + 2
py.time.set_timer(shoot_event,100)


#Event for BG comet
comet_event = py.USEREVENT + 3
py.time.set_timer(comet_event,4000)


#Main Game Loop
while True:

    screen.fill('black')

    for event in py.event.get():

        if event.type == py.QUIT:
            py.quit()
            sys.exit()

        if event.type == comet_event:
            comets.add(Comets_BG())

        #Game Running Events
        if game_state:

             if event.type == py.KEYDOWN:
                 py.mouse.set_visible(False)


#Player Shooting
             if event.type == py.KEYUP:
                if event.key == py.K_SPACE:
                    shoots.add(Shoots_left(),Shoots_right())


            #Asteroid Spawn
            # if event.type == spawn_event:
            #     if randint(0, 2):
            #         asteroids.add(Asteroid(choice(['small', 'big', 'small', 'small'])))


        #Game not running
        else:
            #Tela de Game Over ou de Inicio do Jogo:
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    player_life = 6
                    points = 500
                    asteroids.empty()
                    boss.set_initial_pos()
                    boss.clear_shoots()
                    player_shield_initial_time = 6
                    py.time.set_timer(comet_event, 5000)
                    menu_screen.frame_count = 0
                    menu_screen.speed = 3
                    menu_screen.rect.centerx,menu_screen.rect.centery = menu_screen.initial_pos
                    shield_player.initial_time = 6
                    game_state = True


    #Game Running screen
    if game_state:
        screen.blit(background, (0, 0))
        comets.draw(screen)
        comets.update()
        player.draw(screen)
        player.update()
        asteroids.draw(screen)
        asteroids.update()
        shoots.draw(screen)
        shoots.update()
        asteroid_killing()
        colision = player_collision()
        boss.update(shoots)
        horde.update()
        horde_alive = horde.horde_end()



        #Activating Shield
        pressed = py.key.get_pressed()

        if pressed[py.K_s]:
            player_shield_initial_time = shield_player.get_show_timer()

            #Show the shield if time > 0:
            if player_shield_initial_time > 0:
                shield_player.update(asteroids,player_shield_initial_time,boss.get_shoot_group())


        #Marca entrada do Boss na tela:
        if points >= 500 and not horde_alive:
            boss.enemy_spawn()





        #Player Colision Explosion Sprite
        if colision:
            player_life -= 1
            generic_explosion_animation(player,asteroids,explosion_animation)

        if player_life == 0:
            shoots.empty()
            asteroids.empty()


            game_state = False

        display_points(screen,points)
        life_bar(player_life, screen, 'center')


    else:
        #Start Menu
        screen.blit(background,(0,0))
        comets.draw(screen)
        comets.update()
        menu_screen.show_text()
        menu_screen.move_text()
        menu_screen.show_subtext()



    clock.tick(60)
    pygame.display.update()




