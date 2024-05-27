import pygame
import random

pygame.init()

def smoke(smoke1_surf,smoke2_surf,robot_x,robot_y):

    num_x =[90,90,90,100]
    num_y = [0,0,0,10]

    posicoes = [(robot_x +random.choice(num_x),robot_y - random.choice(num_y)),(robot_x +random.choice(num_x),robot_y-random.choice(num_y))]

    smoke1_rect = smoke1_surf.get_rect(midbottom = (random.choice(posicoes)))
    smoke2_rect = smoke2_surf.get_rect(midbottom = (random.choice(posicoes)))


    return smoke1_rect,smoke2_rect

