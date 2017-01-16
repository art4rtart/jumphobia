from pico2d import *
import framework
import gameTitle
import game

name = "copyright"
background = None
wix = None
ncs = None
opacify = 0.001


def enter():
    global background, ncs, wix
    background = load_image("back.png")
    wix = load_image("wix.png")
    ncs = load_image("ncs.png")


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
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                framework.push_state(gameTitle)


def update(frame_time):
    global opacify

    game.move -= 1
    opacify += 0.02 * game.dir

    if opacify > 1:
        game.dir *= -1

    if opacify < 0:
        framework.push_state(gameTitle)


def draw(frame_time):
    clear_canvas()
    for i in range(10):
        for j in range(10):
            background.draw(game.background_x + 1000 * i + game.move, game.background_y + 500 * j + game.move)

    if opacify > 0.001:
        wix.draw(350, 250)
        ncs.draw(650, 250)

    wix.opacify(opacify)
    ncs.opacify(opacify)
    update_canvas()



