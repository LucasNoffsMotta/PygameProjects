import pygame
from random import randint,choice



class Player(pygame.sprite.Sprite()):
        def __init__(self):     
            super().__init__()
            self.initial_size_x = 5
            self.initial_size_y = 0
            self.color = ('green')
            self.speed = 5
            self.grow = 0
            self.image = pygame.surface(self.initial_size_x,self.initial_size_y)
            self.image.fill(self.color)
            self.rect = self.image.get_rect(center = (0,0))
            self.screen_border_x = (0,800)
            self.screen_border_y = (0,600)
            
        
        def comands(self):
              self.comand_dict = {
            'up':pygame[k_UP],
            'down':pygame[K_DOWN],
            'left':pygame[K_LEFT],
            'right':pygame[K_RIGHT]
            }
              
            
            

              return self.comand_dict

              
        def input(self):
            keys = pygame.key.get_pressed()
            self.comand,self.x,self.y = self.comands()

            if self.rect.midleft > screen_border_x(0) and rect.midright < screen_border_x(1) and 0 < self.rect.top < self.screen_border_y(0) and self.screen_border_y(0) < self.rect.bottom < self.screen_border_y(1): 

                for direction,pressed in self.comand:
                        if direction == 'up':
                            self.rect.y -= self.speed
                        if direction == 'down':
                            self.rect.y += self.speed
                        if direction == 'left':
                            self.rect.x -= self.speed
                        if direction == 'right':
                            self.rect.x += self.speed

        def update(self):
             self.comands()
             self.input()

        
        
                  
                          
                          
                    
                    
            
              
    
                   
              
        



            



                    
                    


        