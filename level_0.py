# -----------------------------------------------------------------------------------
from pico2d import *
import framework
import game
import level_1

# -----------------------------------------------------------------------------------
from jumper import Jumper

# -----------------------------------------------------------------------------------
name = "level_0"
# -----------------------------------------------------------------------------------
jumper = None
background = None
portal = None
# -----------------------------------------------------------------------------------


def create_world():
    global jumper, background, portal
    jumper = Jumper()

    background = load_image("stage1.png")
    portal = load_image('portal.png')

    game.portal_x, game.portal_y = 750, 160
    game.flying = 0


def enter():
    create_world()
    framework.reset_time()


def exit():
    pass


def pause():
    pass


def resume():
    pass


# -----------------------------------------------------------------------------------

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
            framework.quit()
        if jumper.life == 1:
            if game.jumping == 0:
                if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                    jumper.state = jumper.RUNRIGHT
                if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                    jumper.state = jumper.RUNLEFT
                if (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
                    jumper.state = jumper.STANDRIGHT
                if (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
                    jumper.state = jumper.STANDLEFT

                if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                    game.jumping = 1

            if game.jumping == 1:
                if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                    game.movement = 1

                if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                    game.movement = 2

                if jumper.state == jumper.RUNRIGHT or jumper.state == jumper.STANDRIGHT:
                    jumper.state = jumper.JUMPRIGHT

                if jumper.state == jumper.RUNLEFT or jumper.state == jumper.STANDLEFT:
                    jumper.state = jumper.JUMPLEFT


def update(frame_time):
    # -----------------------------------------
    jumper.update(frame_time)
    collision(frame_time)
    move_to_next_level(frame_time)
    # -----------------------------------------
    update_canvas()


def draw(frame_time):
    clear_canvas()
    # -----------------------------------------
    background.draw(game.back_x, game.back_y)
    portal.draw(game.portal_x, game.portal_y)
    jumper.draw()
    # -----------------------------------------
    update_canvas()


def collision(frame_time):
    if jumper.x > 180 and jumper.x < 270 or jumper.x < 590 and jumper.x > 500:
        if jumper.state == Jumper.RUNRIGHT:
            jumper.state = Jumper.STANDRIGHT
            game.jumping = 1
            jumper.state = Jumper.JUMPRIGHT

        if jumper.state == Jumper.RUNLEFT:
            jumper.state = Jumper.STANDLEFT
            game.jumping = 1
            jumper.state = Jumper.JUMPLEFT

    if jumper.x > 190 and jumper.x < 260 and jumper.y < 158 or jumper.x < 580 and jumper.x > 511 and jumper.y < 158:
        jumper.life = 0
    else:
        jumper.life = 1

    if jumper.life == 0:
        jumper.y -= 10


def move_to_next_level(frame_time):
    if jumper.x > game.portal_x:
        framework.push_state(level_1)
        print("move to next level")

# -----------------------------------------------------------------------------------


