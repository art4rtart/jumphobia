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
from platform import Jump
# -----------------------------------------------------------------------------------
name = "level_1"
# -----------------------------------------------------------------------------------
jumper, spike = None, None
level, blink, sign, font = None, None, None, None
jump = None
# -----------------------------------------------------------------------------------


def create_world():
    global jumper, spike, level, blink, sign, font, jump

    # game class import
    jumper = Jumper()
    spike = Spike()
    jump = Jump()

    # game image load
    level = load_image("level_7.png")
    blink = load_image("blink.png")
    sign = load_image("sign.png")
    font = load_font("overwatch.TTF", 25)

    # game initialize
    game.flying = 0
    game.jumping = 0
    game.x, game.y = 50, 199
    game.gck, game.gak = 90, 290
    game.height = 0
    game.jump_x, game.jump_y = 12, 25
    game.seta = 90
    game.min_x, game.max_x = 0, 1000
    game.min_wall, game.max_wall = 40, 40

    # class initialize
    spike.x, spike.y = 575, 130
    jumper.x, jumper.y = 50, 199
    jumper.life = 1
    jumper.state = Jumper.STANDRIGHT


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
            jumper.y += 2

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            jumper.y -= 2


def update(frame_time):
    # update ----------------------------------
    jumper.update(frame_time)
    jump.update(frame_time)
    logic(frame_time)
    height(frame_time)
    wall(frame_time)
    collision(frame_time)
    change_level(frame_time)
    # -----------------------------------------
    update_canvas()


def draw(frame_time):
    clear_canvas()
    # draw objects ----------------------------
    level.draw(game.back_x, game.back_y)
    sign.draw(game.sign_x, game.sign_y)
    jumper.draw()
    jump.draw()
    text(frame_time)
    # draw bounding box -----------------------
    # jumper.draw_bb()
    # spike.draw_bb()
    # -----------------------------------------
    update_canvas()

# -----------------------------------------------------------------------------------


def logic(frame_time):
    print(jumper.x, jumper.y)
    if jumper.x > 100 and jumper.x < 225 \
            or jumper.x > 295 and jumper.x < 420 \
            or jumper.x > 490 and jumper.x < 620 \
            or jumper.x > 730 and jumper.x < 850:
        if jumper.state == Jumper.RUNRIGHT:
            jumper.state = Jumper.STANDRIGHT
            game.jumping = 1
            jumper.state = Jumper.JUMPRIGHT

        if jumper.state == Jumper.RUNLEFT:
            jumper.state = Jumper.STANDLEFT
            game.jumping = 1
            jumper.state = Jumper.JUMPLEFT


# -----------------------------------------------------------------------------------

def height(frame_time):
    if jumper.x < 850:
        game.height = 0

    if jumper.x > 850:
        game.height = 244 - game.y


# -----------------------------------------------------------------------------------

def wall(frame_time):
    if jumper.x > 40:
        game.min_wall = 40

    if jumper.x <= 40:
        game.min_wall = 0

    if jumper.x < 950:
        game.max_wall = 40

    if jumper.x >= 950:
        game.max_wall = 0

# -----------------------------------------------------------------------------------

def text(frame_time):
    # text for player :)
    font.draw(450, 12, "PEACE  OF  CAKE", (255, 255, 255))


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


