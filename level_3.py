# -----------------------------------------------------------------------------------
from pico2d import *
import framework
import game
import level_2
import level_3
import level_4
# -----------------------------------------------------------------------------------
from jumper import Jumper
from obstacle import Spike
# -----------------------------------------------------------------------------------
name = "level_1"
# -----------------------------------------------------------------------------------
jumper, spike = None, None
level, blink, sign, font = None, None, None, None
falling_state = True
# -----------------------------------------------------------------------------------


def create_world():
    global jumper, spike, level, blink, sign, font

    # game class import
    jumper = Jumper()
    spike = Spike()

    # game image load
    level = load_image("level_3.png")
    blink = load_image("blink.png")
    sign = load_image("sign.png")
    font = load_font("overwatch.TTF", 25)

    # game initialize
    game.flying = 0
    game.sign_x, game.sign_y = 420, 228
    game.min_x, game.max_x = 0, 1000
    game.min_wall, game.max_wall = 40, 40

    # class initialize
    jumper.x, jumper.y = 950, 474
    jumper.state = Jumper.STANDLEFT
    # spike.x, spike.y = 575, 130


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
                # 치트키
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
        # 치트키
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            jumper.y += 20

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            jumper.y -= 20


def update(frame_time):
    global falling_state
    # update ----------------------------------
    jumper.update(frame_time)
    jumper.life = 1

    if jumper.y > 170 and falling_state:
        jumper.y -= 8

    if jumper.y == 170:
        falling_state = False

    print(jumper.x, jumper.y)
    # logic(frame_time)
    # collision(frame_time)
    # change_level(frame_time)
    # -----------------------------------------
    update_canvas()


def draw(frame_time):
    clear_canvas()
    # draw objects ----------------------------
    level.draw(game.back_x, game.back_y)
    # sign.draw(game.sign_x, game.sign_y)
    jumper.draw()
    text(frame_time)
    # draw bounding box -----------------------
    # jumper.draw_bb()
    # spike.draw_bb()
    # -----------------------------------------
    update_canvas()

# -----------------------------------------------------------------------------------


def logic(frame_time):
    print(jumper.x, jumper.y)
    if jumper.x > 95 and jumper.x < 155 \
            or jumper.x > 255 and jumper.x < 365 \
            or jumper.x > 465 and jumper.x < 660 \
            or jumper.x > 705 and jumper.x < 885:
        if jumper.state == Jumper.RUNRIGHT:
            jumper.state = Jumper.STANDRIGHT
            game.jumping = 1
            jumper.state = Jumper.JUMPRIGHT

        if jumper.state == Jumper.RUNLEFT:
            jumper.state = Jumper.STANDLEFT
            game.jumping = 1
            jumper.state = Jumper.JUMPLEFT

    if jumper.x > 105 and jumper.x < 145 and jumper.y < game.y + 1 \
            or jumper.x > 265 and jumper.x < 355 and jumper.y < game.y + game.wall + 1 \
            or jumper.x > 475 and jumper.x < 650 and jumper.y < game.y + game.wall + 1 \
            or jumper.x > 715 and jumper.x < 875 and jumper.y < game.y + game.wall + 1:
        jumper.life = 0
    else:
        jumper.life = 1

    if jumper.life == 0:
        jumper.y -= game.falling

    if jumper.x <= 105:
        game.wall = 0

    if jumper.x > 145:
        game.wall = 54

    print(jumper.x)

    if jumper.x > 355:
        game.wall = 96

    if jumper.x > 650:
        game.wall = 74

    if jumper.x > 875:
        game.wall = 62


# -----------------------------------------------------------------------------------

def text(frame_time):
    # text for player :)
    font.draw(440, 12, "TIMING  IS  KEY", (255, 255, 255))


# -----------------------------------------------------------------------------------

def collision(frame_time):
    if collide(jumper, spike):
        game.reset = True
        framework.push_state(level_3)


# -----------------------------------------------------------------------------------

def change_level(frame_time):
    if game.reset:
        blink.draw(game.back_x, game.back_y)
        game.temp += 1

    if game.temp > 2:
        game.reset = False

    if jumper.x <= game.min_x:
        game.x = 980
        game.change_level = True
        game.motion = True
        framework.push_state(level_2)

    if jumper.x >= game.max_x:
        framework.push_state(level_4)


# -----------------------------------------------------------------------------------

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


