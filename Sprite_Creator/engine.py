import pygame as py
py.init()

#Class that creates surfaces
#Receives as argument the color and the size of the surface to be created
#Those arguments will be passed trough another class

class CreateSurface():

    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.surface = py.Surface((size))
        self.surface.fill(self.color)
    
    def get_surface(self):
        return self.surface
    
    @classmethod

    def create_surface(cls, color, size):
        object = cls(color, size)
        return object.get_surface()


#Class that creates the list of frames passing the color and size arguments, as well as the amount of frames to be created

class FramesGenerator():
    color = 'blue'
    size = (5,5)
    def __init__(self,frames_qtd,color,size):

        self.frames = []
        self.frames_qtd = frames_qtd
        self.color = color
        self.size = size

        for i in range(0,frames_qtd):
            self.frames.append(CreateSurface(color,(size[0]+ (i+5),(size[1] + (i+5)))).get_surface())
    
    def get_frames(self):
        return self.frames
    

#Class that animates the object. Receive as argument the list created, the position of the rect, the animation speed (float) and the screen
#The object of this class should be created on the main screen

class FramesAnimation():
    def __init__(self,surf_list, rectpos, animation_speed, screen):
        self.surf_list = surf_list
        self.rectpos = rectpos
        self.animation_speed = animation_speed
        self.screen = screen
        self.counter = 0
        self.image = self.surf_list[self.counter]
        self.rect = self.image.get_rect(center=(self.rectpos[0],self.rectpos[1]))
    
    def animation(self):
        self.counter += self.animation_speed
        if self.counter >= len(self.surf_list):
            self.counter = 0
        self.image = self.surf_list[int(self.counter)]
    
    def screen_blit(self):
        self.screen.blit(self.image,self.rect)





    


    

    



