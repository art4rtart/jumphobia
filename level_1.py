# -----------------------------------------------------------------------------------
from pico2d import *
import framework
import game
import level_0
import level_1
# -----------------------------------------------------------------------------------
from jumper import Jumper
from obstacle import Spike
# -----------------------------------------------------------------------------------
name = "level_1"
# -----------------------------------------------------------------------------------
jumper, spike = None, None
level = None
blink = None
# -----------------------------------------------------------------------------------


def create_world():
    global jumper, spike, level, blink

    # game class import
    jumper = Jumper()
    spike = Spike()

    # game image load
    level = load_image("level_0.png")
    blink = load_image("blink.png")

    # game initialize
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
    logic(frame_time)
    collision(frame_time)
    move_to_next_level(frame_time)
    # -----------------------------------------
    update_canvas()


def draw(frame_time):
    clear_canvas()
    # -----------------------------------------
    level.draw(game.back_x, game.back_y)

    jumper.draw()
    jumper.draw_bb()

    spike.draw_bb()

    if game.reset:
        blink.draw(game.back_x, game.back_y)
        game.temp += 1

    if game.temp > 2:
        game.reset = False

    # -----------------------------------------
    update_canvas()


def logic(frame_time):
    if jumper.x > 240 and jumper.x < 350 \
            or jumper.x > 635 and jumper.x < 790:
        if jumper.state == Jumper.RUNRIGHT:
            jumper.state = Jumper.STANDRIGHT
            game.jumping = 1
            jumper.state = Jumper.JUMPRIGHT

        if jumper.state == Jumper.RUNLEFT:
            jumper.state = Jumper.STANDLEFT
            game.jumping = 1
            jumper.state = Jumper.JUMPLEFT

    if jumper.x > 250 and jumper.x < 340 and jumper.y < game.y + 1 \
            or jumper.x > 645 and jumper.x < 780 and jumper.y < game.y + 1:
        jumper.life = 0
    else:
        jumper.life = 1

    if jumper.life == 0:
        jumper.y -= 10


def collision(frame_time):
    if collide(jumper, spike):
        game.reset = True
        framework.push_state(level_0)


def move_to_next_level(frame_time):
    if jumper.x > game.max_x:
        framework.push_state(level_1)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True


# -----------------------------------------------------------------------------------


