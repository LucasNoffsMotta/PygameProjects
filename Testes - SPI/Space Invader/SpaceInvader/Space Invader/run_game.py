import pygame
import pygame.display
from level_class import *
from menu_loop import *
from save_scores import save_score
from pause_loop import PauseLoop


def main():
    #Screen
    pygame.init()
    width = 1000
    height = 860
    screen = py.display.set_mode((width, height))

    def show_fps():
        font = py.font.Font('Images/Font/slkscr.ttf', 30)
        text_surf = font.render(f'{int(clock.get_fps())}', False, 'green')
        text_rect = text_surf.get_rect()
        screen.blit(text_surf, text_rect)


    #BG
    background = py.image.load('Images/Background/background_2.png').convert_alpha()

    # Game State
    game_state = False
    score = 0
    game_over = GameOver(screen, score)

    level_running = True
    current_level = 1
    level = Level(screen, current_level, score)

    shoots = py.sprite.Group()
    explode = py.sprite.GroupSingle()
    explode.add(Player_Explosion())
    explosion_animation = py.sprite.GroupSingle()
    explosion_animation.add(Asteroid_Explosion())
    comets = py.sprite.Group()
    save_file = 'save_jason.json'
    save_score(score, current_level, save_file)
    paused = PauseLoop(screen,background,comets)


    #FPS
    clock = py.time.Clock()
    pygame.key.set_repeat(5000)

    #Event for BG comet
    comet_event = py.USEREVENT + 3
    py.time.set_timer(comet_event,4000)


    #Main Game Loop
    while True:

        for event in py.event.get():

            if event.type == py.QUIT:
                py.quit()
                sys.exit()

            if event.type == comet_event:
                comets.add(Comets_BG())

            #Game Running Events
            if game_state:

                if event.type == py.KEYDOWN:
                     py.mouse.set_visible(False)

                if level_running:

                    if event.type == py.KEYDOWN:

                        if event.key == pygame.K_ESCAPE:
                            game_state = paused.main_loop()
                            continue


        #Game Running screen
        if game_state:
            screen.blit(background, (0, 0))
            comets.draw(screen)
            comets.update()

            if level_running:
                level_status,score = level.update()

                #Player died:
                if not level_status:
                    game_over_screen = game_over.update(score)

                    if not game_over_screen:
                        save_score(score, current_level, save_file)
                        game_state = False

                #Next level
                if level_status == 'passed':
                    current_level += 1
                    level = Level(screen,current_level,score)

        else:
            game_over = GameOver(screen, score)
            menu = MenuLoop(screen, background, comets)
            menu.main_loop()
            score = 0
            current_level = 1
            level = Level(screen, current_level, score)
            level_running = True
            game_state = True

        show_fps()
        clock.tick(60)
        pygame.display.update()


if __name__ == '__main__':
    main()


