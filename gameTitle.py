from pico2d import *
import framework
import game
import level_0

name = "title"
background = None
title = None
key = None
opacify_0, opacify_1, opacify_2, opacify_3, opacify_4 = 0.001, 0.001, 0.001, 0.001, 0.001
play_game, create_game, exit_game = None, None, None
p1, c1, e1 = None, None, None

def enter():
    global background, title, key, play_game, create_game, exit_game, p1, c1, e1
    background = load_image("back.png")
    title = load_image("title.png")
    key = load_image("key.png")
    play_game = load_image('play.png')
    create_game = load_image('level_design.png')
    exit_game = load_image('exit.png')
    p1 = load_image('play1.png')
    c1 = load_image('level_design1.png')
    e1 = load_image('exit1.png')

def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                framework.quit()
            if (event.type, event.key) != (SDL_KEYDOWN, SDLK_SPACE) and opacify_0 > 1:
                game.event = True
            if event.type == SDL_MOUSEMOTION and opacify_4 >= 1:
                if event.x > 603 and event.y > 125 and event.x < 757 and event.y < 160:
                    game.menu = 1

                elif event.x > 603 and event.y > 213 and event.x < 785 and event.y < 250:
                    game.menu = 2

                elif event.x > 603 and event.y > 304 and event.x < 744 and event.y < 340:
                    game.menu = 3

                else:
                    game.menu = 0

            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                if game.menu == 1:
                    framework.push_state(level_0)

                elif game.menu == 3:
                    framework.quit()

def update(frame_time):
    global opacify_0

    game.move -= 0.5
    opacify_0 += 0.008

    if game.event:
        if game.title_x > 350:
            game.title_x -= 5


def draw(frame_time):
    global opacify_1, opacify_2, opacify_3, opacify_4

    clear_canvas()
    for i in range(10):
        for j in range(10):
            background.draw(game.background_x + 1000 * i + game.move, game.background_y + 500 * j + game.move)

    if opacify_0 > 0.001:
        title.draw(game.title_x, game.title_y)
    if opacify_0 < 1:
        title.opacify(opacify_0)

    if opacify_0 > 1 and game.event is False:
        key.draw(495, 80)
        opacify_1 += 0.02 * game.dir

        if opacify_1 > 1:
            game.dir *= -1

        if opacify_1 < 0:
            opacify_1 = 0.001
            game.dir *= -1

    key.opacify(opacify_1)

    if game.title_x <= 350:
        play_game.draw(690, 360)
        create_game.draw(690, 270)
        exit_game.draw(690, 180)

        opacify_2 += 0.008

        if opacify_2 > 1:
            opacify_2 = 1

        if opacify_3 > 1:
            opacify_3 = 1

        if opacify_4 > 1:
            opacify_4 = 1

        if opacify_2 > 0.3:
            if opacify_3 < 1:
                opacify_3 += 0.008

        if opacify_2 > 0.6:
            if opacify_4 < 1:
                opacify_4 += 0.008

    play_game.opacify(opacify_2)
    create_game.opacify(opacify_3)
    exit_game.opacify(opacify_4)

    if game.menu == 1:
        p1.draw(690, 360)

    if game.menu == 2:
        c1.draw(690, 270)

    if game.menu == 3:
        e1.draw(690, 180)

    update_canvas()



