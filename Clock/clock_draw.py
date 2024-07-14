import pygame as py
from datetime import datetime
import math
from constants import screen_widith,screen_height


#Pointers size
P_widith = screen_widith // 2
p_height = screen_height // 2
radius = p_height - 50


#Current time
t = datetime.now()

radius_dict = {'sec':radius - 55,'min':radius - 70,'hour':radius - 130,'digit':radius - 30}

#Calculate the angle move each time
def get_clock_pos(clock_dict, clock_hand,key):
    x = P_widith + radius_dict[key] *math.cos(math.radians(clock_dict[clock_hand])) - math.pi / 2
    y = p_height + radius_dict[key] *math.sin(math.radians(clock_dict[clock_hand])) - math.pi / 2
    return x,y


class NiceClock():
    def __init__(self
                 ,circle_color:str
                 ,pointers_color:tuple
                 ,inner_color:tuple
                 ,screen:py.display
                 ,pos:tuple
                 ):


        self.circle_color = circle_color
        self.pointers_color = pointers_color
        self.inner_color =  inner_color
        self.screen = screen
        self.pos = pos
        
        

    def circle_draw(self,color,center,radius):
        py.draw.circle(self.screen,color,(center),radius,5)


    
    def pointer_draw(self,sec_color,min_color,h_color):
        # clock12 = dict(zip(range(12), range(0,360,30)))
        clock60 = dict(zip(range(60), range(0, 360, 6)))
        t = datetime.now()
        hours, minutes, seconds = (((t.hour % 12) * 5 + t.minute // 12) ) % 60, t.minute, t.second
        
        #Digits
        for digit , pos in clock60.items():
            radius = 20 if not digit % 3 and not digit % 5 else 8 if not digit % 5 else 2
            py.draw.circle(self.screen,'gainsboro',get_clock_pos(clock60,digit,'digit'),radius,7)

        py.draw.line(self.screen,h_color,(P_widith,p_height),get_clock_pos(clock60,hours,'hour'),10)
        py.draw.line(self.screen,min_color,(P_widith,p_height),get_clock_pos(clock60,minutes,'min'),7)
        py.draw.line(self.screen,sec_color,(P_widith,p_height),get_clock_pos(clock60,seconds,'sec'),4)
        print(P_widith,p_height)
    



    def update(self):
        #Outer Circle
        self.circle_draw('red',(P_widith,p_height),radius)

        #Inner Circle
        # self.circle_draw()

        self.pointer_draw('blue','yellow','green')
        

        

        

    

