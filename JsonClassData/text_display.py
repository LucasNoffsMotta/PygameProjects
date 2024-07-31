import pygame as py

py.init()

class TextObject:

    def __init__(self,
                 screen:py.display,
                 font: py.font.Font,
                 text:str,
                 pos: tuple,
                 color:str
                 ):
        
        self.screen =screen
        self.font = font
        self.text = text
        self.pos = pos
        self.color = color
        
        self.text_surf = self.font.render(f'{self.text}',True,self.color)
        self.text_rect = self.text_surf.get_rect(center=(pos))

    
    def display_text(self):
        self.screen.blit(self.text_surf,self.text_rect)
    
    def get_text(self):
        return self.text
    
    def get_rect(self):
        return self.text_rect
    
    def change_pos(self,new_pos):
        self.text_surf = self.font.render(self.text,True,self.color)
        self.text_rect = self.text_surf.get_rect(center=(new_pos))
        
    def __str__(self):
        return self.text
    
    def __add__(self,other):
        return self.text + other.text
  



























  