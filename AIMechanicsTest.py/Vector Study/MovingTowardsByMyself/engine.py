import pygame as py


class Being():

    def __init__(self, screen, size, color, initial_pos,speed):
        self.screen = screen
        self.size = size
        self.color = color
        self.surf = py.Surface((self.size))
        self.surf.fill(self.color)
        self.initial_pos = initial_pos
        self.rect = self.surf.get_rect(center=(self.initial_pos))
        self.speed = speed
    

    def get_rect(self):
        return self.rect
    

    def move_down(self):
        self.rect.centery += self.speed
    
    def move_up(self):
        self.rect.centery -= self.speed
    
    def move_left(self):
        self.rect.centerx -= self.speed
    
    def move_right(self):
        self.rect.centerx += self.speed


    def get_move(self,other_rect):

        
        
        if self.rect.centerx < other_rect.centerx and self.rect.centery < other_rect.centery:
            self.move_right()
            self.move_down()
        
        if self.rect.centerx > other_rect.centerx and self.rect.centery < other_rect.centery:
            self.move_left()
            self.move_down()
        
        if self.rect.centerx < other_rect.centerx and self.rect.centery > other_rect.centery:
            self.move_right()
            self.move_up()

        if self.rect.centerx > other_rect.centerx and self.rect.centery > other_rect.centery:
            self.move_left()
            self.move_up()
        
        else:
             if self.rect.centerx < other_rect.centerx:
                self.move_right()
        
             if self.rect.centerx > other_rect.centerx:
                self.move_left()
        

             if self.rect.centery < other_rect.centery:
                self.move_down()
            
             if self.rect.centery > other_rect.centery:
                self.move_up()



        










        

    def screen_blit(self):
        self.screen.blit(self.surf,self.rect)

    
    def update(self):
        #self.screen_border()
        # self.get_input()
 
        self.screen_blit()
    


