import pygame as py
import sys
from text_display import TextObject



def main():
    screen_widith = 1000
    screen_height = 860


    screen = py.display.set_mode((screen_widith,screen_height))
    clock = py.time.Clock()
    font = py.font.Font(None,50)

    space_x = 30
    space_y = 40

    # alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    alphabet = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    upper_alphabet  = []
    for l in alphabet:
         n_l = l.upper()
         upper_alphabet.append(n_l)

    
    original_pos_x, original_pos_y = 335,500
    
    initial_pos = [original_pos_x,original_pos_y]
    arrow_pos = [initial_pos[0] + space_x, initial_pos[1]]

    forbidden_pos = {
         'up': 500,
         'down':580,
         'left':365,
         'right':635
    }

    chosen_letters_pos = [300,200]
    writting_line = py.surface.Surface((7,25))
    py.draw.line(writting_line,'dark red',(2.5,0),(2.5,25))
    writting_rect = writting_line.get_rect(center=(chosen_letters_pos[0] - 15,chosen_letters_pos[1]))
    
    
    text_underline = [[290,215],[730,215]]
    writting_line_alpha = [255,0]
    text_blink = 0
    blink_speed = 0.03
 


    def display_writting_line(surf):
        writting_rect = surf.get_rect(center=(chosen_letters_pos[0] -15,chosen_letters_pos[1]))
        screen.blit(surf,writting_rect)
        
        
    
    chosen_rects = []
 

    set_arrow = py.surface.Surface((25,25))
    py.draw.rect(set_arrow,'white',(0,0,25,25),1)
    

    
    def get_alphabet(color,font,alpha_list,pos_keybord):

        alphabet_rects = []

        for n, letter in enumerate(alpha_list):    
                if n < 10:
                    alphabet_rects.append(TextObject(screen,font,letter,(pos_keybord[0] + space_x, pos_keybord[1]),color))
                    pos_keybord[0] += space_x
        
        pos_keybord[1] += space_y
        pos_keybord[0] = original_pos_x 

        for n, letter in enumerate(alpha_list):
                if 10 <= n < 20:
                  alphabet_rects.append(TextObject(screen,font,letter,(pos_keybord[0] + space_x, pos_keybord[1]),color))
                  pos_keybord[0] += space_x

        pos_keybord[1] += space_y
        pos_keybord[0] = original_pos_x + (space_x*2) 
        
        for n, letter in enumerate(alpha_list):
             if 20 <= n < 28:
                  alphabet_rects.append(TextObject(screen,font,letter,(pos_keybord[0] + space_x, pos_keybord[1]),color))
                  pos_keybord[0] += space_x

        pos_keybord = [335,500]
        return alphabet_rects,pos_keybord


    # colors = ['brown','white','red','yellow','blue','green','light blue','dark blue','orange']
    # color_n = 1         
    
    # lower_alpha,initial_pos = get_alphabet(colors[color_n],alphabet,initial_pos)
    # upper_alpha,initial_pos = get_alphabet(colors[color_n],upper_alphabet,initial_pos)
    # case_list = [lower_alpha,upper_alpha]
    case_select = 0
  
    colors = ['brown','white','red','yellow','blue','green','light blue','dark blue','orange']
    color_n = 1

    available_fonts = py.font.get_fonts()
    print(available_fonts)
    fonts = [py.font.SysFont(font,30) for font in available_fonts]
    current_font = 0
    font = fonts[current_font]
    print(len(available_fonts))
    


    def display_font(font,color,screen):
         surf = font.render(available_fonts[current_font],False,color)
         screen.blit(surf,(100,750))


    while True:
        mouse_pos = py.mouse.get_pos()
        screen.fill('black')
        
        color = colors[color_n]
        font = fonts[current_font]

        lower_alpha,initial_pos = get_alphabet(color,font,alphabet,initial_pos)
        upper_alpha,initial_pos = get_alphabet(color,font,upper_alphabet,initial_pos)
        case_list = [lower_alpha,upper_alpha]


        set_rect = set_arrow.get_rect(center=(arrow_pos))
        print(arrow_pos)

        screen.blit(set_arrow,set_rect)    
        py.draw.line(screen,'brown',text_underline[0],text_underline[1],3)

        current_alpha = case_list[case_select]

        display_font(font,color,screen)
        

        text_blink += blink_speed
        if text_blink >= len(writting_line_alpha):
             text_blink = 0
        writting_line.set_alpha(writting_line_alpha[int(text_blink)])
        display_writting_line(writting_line)
 
       
        for rect in current_alpha:
                rect.display_text()
        

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

            if event.type == py.KEYDOWN:

                if event.key == py.K_RIGHT and set_rect.centerx != forbidden_pos['right']:
                    arrow_pos[0] += space_x
                
                if event.key == py.K_LEFT and set_rect.centerx != forbidden_pos['left']:
                     arrow_pos[0] -= space_x      

                if event.key == py.K_UP and set_rect.centery != forbidden_pos['up']:
                     arrow_pos[1] -= space_y
                
                if event.key == py.K_DOWN and set_rect.centery != forbidden_pos['down']:
                     arrow_pos[1] += space_y
                    
                if event.key == py.K_SPACE:
                     chosen_letters_pos[0] += space_x
                     writting_rect.centerx += space_x
                     
                if event.key == py.K_RETURN:
                     for rect in current_alpha:
                          if set_rect.center == rect.get_rect().center:
                               chosen_rects.append(TextObject(screen,font,rect.get_text(),chosen_letters_pos,colors[color_n]))
                               chosen_letters_pos[0] += space_x
                               writting_rect.centerx += space_x
                          
                               if chosen_letters_pos[0] >= 750 or writting_rect.centerx >= 750:
                                    chosen_letters_pos[0] = 750
                                    writting_rect.centerx = 735
                                    
                              
                if event.key == py.K_BACKSPACE:
                         chosen_letters_pos[0] -= space_x
                         writting_rect.centerx -= space_x

                         if chosen_letters_pos[0] <= 300:
                            chosen_letters_pos[0] = 300

                         if writting_rect.centerx <= 300:
                            writting_rect.centerx = 285
                
                if event.key == py.K_CAPSLOCK:
                     case_select += 1
                     if case_select > 1:
                          case_select = 0

                if event.key == py.K_c:
                     color_n += 1
                     if color_n >= len(colors):
                          color_n = 0

                if event.key == py.K_f:
                     current_font += 1
                     if current_font >= len(fonts):
                          current_font = 0
                     

        for rect in chosen_rects:
            if writting_rect.centerx < rect.get_rect().centerx:
                chosen_rects.pop(-1)                  

        if len(chosen_rects) > 0:
             for rect in chosen_rects:
                  rect.display_text()

        clock.tick(60)
        py.display.update()



if __name__ == '__main__':
    py.init()
    main()
            
        

