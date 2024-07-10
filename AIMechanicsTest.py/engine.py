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
        self.rect.y += self.speed
    
    def move_up(self):
        self.rect.y -= self.speed
    
    def move_left(self):
        self.rect.x -= self.speed
    
    def move_right(self):
        self.rect.x += self.speed


    def get_move(self,other_rect):

        if self.rect.centerx < other_rect.centerx:
            self.move_right()
        
        if self.rect.centerx > other_rect.centerx:
            self.move_left()
        
        if (abs(self.rect.centerx - other_rect.centerx)) < 5:

            if self.rect.centery < other_rect.centery:
                self.move_down()
            
            elif self.rect.centery > other_rect.centery:
                self.move_up()

    
    def get_escape(self,other_rect):
    
        if abs(self.rect.x - other_rect.x) < 50 and abs(self.rect.y - other_rect.y) < 50:
            if self.rect.x > other_rect.x:
                self.move_down()
                
                if self.rect.y > other_rect.y:
                    self.move_down()

                if self.rect.y < other_rect.y:
                    self.move_up()

            if self.rect.x < other_rect.x:
                self.rect.x -= self.speed
                if self.rect.y > other_rect.y:
                    self.move_down()

                if self.rect.y < other_rect.y:
                    self.move_up()

            if self.rect.y > other_rect.y:
                self.move_up()

                if self.rect.x > other_rect.x:
                    self.move_right()

                if self.rect.x < other_rect.x:
                    self.move_left()

            if self.rect.y < other_rect.y:
                self.move_up()

                if self.rect.x > other_rect.x:
                    self.move_right()

                if self.rect.x < other_rect.x:
                    self.move_left()


    def screen_border(self):
               
        if self.rect.x >= 800:
            self.move_left()
        if self.rect.x <= 0:
            self.move_right()
        if self.rect.y >= 600:
            self.move_up()
        if self.rect.y <= 0:
            self.move_right()
        



    
    def get_input(self):
        keys = py.key.get_pressed()

        if keys[py.K_DOWN]:
            self.rect.y += self.speed
        
        if keys[py.K_UP]:
            self.rect.y -= self.speed
        
        if keys[py.K_LEFT]:
            self.rect.x -= self.speed
        
        if keys[py.K_RIGHT]:
            self.rect.x += self.speed
    



    def screen_blit(self):
        self.screen.blit(self.surf,self.rect)

    
    def update(self):
        #self.screen_border()
        self.screen_blit()
    


        


