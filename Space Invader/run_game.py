import pygame as py
from random import randint, choice
import pygame.display
from sprites import *
import sys
from text import *


#Functions

#Detect Sprite Colision between Player and Asteroid
def player_collision():
    side = choice([-5, 15])
    if py.sprite.spritecollide(player.sprite,asteroids,False):
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
            asteroid_explode_animation()
            sprite.kill()
            points += 10
            return True


#Asteroid Sprite Explosion Frame
def asteroid_explode_animation():
    for explode_sprite in asteroid_explode:
        for shoot in shoots:
            for asteroid_shooted in asteroids:
                if asteroid_shooted.rect.colliderect(shoot):
                    explode_sprite.rect.center = asteroid_shooted.rect.center
                    asteroid_explode.draw(screen)
                    asteroid_explode.update()
                    py.sprite.spritecollide(shoot, asteroids, True)


#Screen
pygame.init()
width = 1080
height = 920
screen = py.display.set_mode((width, height))

#Sprites Class Call
player = py.sprite.GroupSingle()
player.add(Player())
asteroids = py.sprite.Group()
shoots = py.sprite.Group()
explode = py.sprite.GroupSingle()
explode.add(Player_Explosion())
asteroid_explode= py.sprite.GroupSingle()
asteroid_explode.add(Asteroid_Explosion())

#Game State
game_state = True
points = 0

#BG
background = py.image.load('Images/background.png').convert_alpha()


#FPS
clock = py.time.Clock()


#Event for asteroid spawn
spawn_event = py.USEREVENT + 1
py.time.set_timer(spawn_event,100)


#Event for shoots load
shoot_event = py.USEREVENT + 2
py.time.set_timer(shoot_event,10)



#Main Game Loop
while True:

    screen.fill('black')

    for event in py.event.get():

        if event.type == py.QUIT:
            py.quit()
            sys.exit()

        #Game Running Events
        if game_state:

            if event.type == py.KEYDOWN:
                py.mouse.set_visible(False)
            #Shooting
            if event.type == py.KEYUP:
                if event.key == py.K_SPACE:
                    shoots.add(Shoots_left(),Shoots_right())


            #Points controlw
            if points <= 500:

                if event.type == spawn_event:
                    if randint(0, 2):
                        asteroids.add(Asteroid(choice(['small', 'big', 'small', 'small'])))


        #Game not running
        else:
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    points = 0
                    asteroids.empty()
                    game_state = True




    #Game Running screen
    if game_state:


        screen.blit(background, (0, 0))
        player.draw(screen)
        player.update()
        asteroids.draw(screen)
        asteroids.update()
        #player_shoots()
        shoots.draw(screen)
        shoots.update()
        asteroid_colission = asteroid_killing()
        colision = player_collision()


        #Player Colision Explosion Sprite
        if colision:
            for sprite in explode:
                for asteroid in asteroids:
                    if asteroid.rect.colliderect(player.sprite.rect):
                        sprite.rect.x = player.sprite.rect.x - 20
                        explode.draw(screen)
                        explode.update()

        #Asteroid Colision Sprite Explosion
        if asteroid_colission:
            for explode_sprite in asteroid_explode:
                for shoot in shoots:
                    for asteroid_shooted in asteroids:
                        if asteroid_shooted.rect.colliderect(shoot):
                            explode_sprite.rect.center = asteroid_shooted.rect.center
                            asteroid_explode.draw(screen)
                            asteroid_explode.update()







            #explosion_collide_animation()
        display_points(screen,points)



    else:
        screen.fill('black')


    clock.tick(60)
    pygame.display.update()




