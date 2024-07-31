import pygame as py
from text_display import TextObject


class PlayerData:
    def __init__(self,name,score,level,gems,screen,pos1):
        self.name = name
        self.score = score
        self.level = level
        self.gems = gems

        self.screen = screen
        self.font = py.font.Font(None,30)
        self.pos1 = pos1[0], pos1[1]
        self.pos2 = self.pos1[0],self.pos1[1] + 40
        self.pos3 = self.pos2[0],self.pos2[1] + 40
        self.gem_pos = [self.pos3[0], self.pos3[1] + 40]
        self.color = 'blue'
    
    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def get_level(self):
        return self.level
    
    def get_gems(self):
        return self.gems
    
    def get_name_object(self):
        return TextObject(self.screen, self.font, f'Name: {self.name}', self.pos1, self.color)
    
    def get_score_object(self):
        return TextObject(self.screen, self.font, f'Score: {self.score}', self.pos2, self.color)
    
    def get_level_object(self):
        return TextObject(self.screen, self.font, f'Level: {self.level}', self.pos3, self.color)
    
    def get_gems_object(self):

        gems = []
        for key, item in self.gems.items():
            gems.append(TextObject(self.screen, self.font, f'{key}: {self.gems[key]}',(self.gem_pos[0],self.gem_pos[1]), self.color))
            self.gem_pos[1] += 40
            
        return gems

    def __lt__ (self,other):
        return self.score < other.score
    
    def __str__(self):
        return f'{self.score}'

    


    



    




    


