# -----------------------------------------------------------------------------------
from pico2d import *
import framework
import game
import level_3
import level_4
import level_5
# -----------------------------------------------------------------------------------
from jumper import Jumper
from obstacle import Spike
from platform import Brick
# -----------------------------------------------------------------------------------
name = "level_4"
# -----------------------------------------------------------------------------------
jumper, spike, brick = None, None, None
level, blink, font = None, None, None
# -----------------------------------------------------------------------------------


def create_world():
    global jumper, spike, level, blink, font, brick

    # game class import
    jumper = Jumper()
    spike = Spike()
    brick = Brick()

    # game image load
    level = load_image("level_4.png")
    blink = load_image("blink.png")
    font = load_font("overwatch.TTF", 25)

    # game initialize
    game.flying = 0
    game.x, game.y = 950, 196
    game.min_x, game.max_x = 0, 1000
    game.min_wall, game.max_wall = 0, 40
    game.jump_x, game.jump_y = 10, 20
    game.gck, game.gak = 90, 270

    # class initialize
    jumper.x, jumper.y = 950, 196
    jumper.life = 1
    jumper.state = Jumper.STANDLEFT
    spike.x, spike.y = 495, 110
    spike.box_x, spike.box_y = 365, 10


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
    brick.update(frame_time)
    logic(frame_time)
    height(frame_time)
    wall(frame_time)
    collision(frame_time)
    change_level(frame_time)
    # -----------------------------------------
    update_canvas()


def draw(frame_time):
    # print(jumper.x, jumper.y)
    clear_canvas()
    # draw objects ----------------------------
    level.draw(game.back_x, game.back_y)
    brick.draw()
    jumper.draw()
    text(frame_time)
    # draw bounding box -----------------------
    # jumper.draw_bb()
    # spike.draw_bb()
    # brick.draw_bb_1()
    # brick.draw_bb_2()
    # brick.draw_bb_3()
    # -----------------------------------------
    update_canvas()

# -----------------------------------------------------------------------------------


def logic(frame_time):
    if jumper.x < 865 and jumper.y == 196 \
            or jumper.x >= 170 and jumper.y == 317\
            or (jumper.x <= brick.x_1 - 50 or jumper.x >= brick.x_1 + 50) and jumper.y == brick.y_1 + 27 \
            or (jumper.x <= brick.x_2 - 50 or jumper.x >= brick.x_2 + 50) and jumper.y == brick.y_2 + 27 \
            or (jumper.x <= brick.x_3 - 50 or jumper.x >= brick.x_3 + 50) and jumper.y == brick.y_3 + 27:
        if jumper.state == Jumper.RUNRIGHT:
            jumper.state = Jumper.STANDRIGHT
            game.jumping = 1
            jumper.state = Jumper.JUMPRIGHT

        if jumper.state == Jumper.RUNLEFT:
            jumper.state = Jumper.STANDLEFT
            game.jumping = 1
            jumper.state = Jumper.JUMPLEFT

    if jumper.x >= brick.x_1 - 50:
        if jumper.x <= brick.x_1 + 50:
            if jumper.y <= brick.y_1 + 28:
                jumper.y = brick.y_1 + 28
                jumper.x -= brick.move_1

    if jumper.x >= brick.x_2 - 50:
        if jumper.x <= brick.x_2 + 50:
            if jumper.y <= brick.y_2 + 28:
                jumper.y = brick.y_2 + 28
                jumper.x -= brick.move_2

    if jumper.x >= brick.x_3 - 50:
        if jumper.x <= brick.x_3 + 50:
            if jumper.y <= brick.y_3 + 28:
                jumper.y = brick.y_3 + 28
                jumper.x -= brick.move_3

    if jumper.state == Jumper.JUMPRIGHT:
        if jumper.y <= brick.y_2 + 28:
            game.gck = 90
        else:
            game.gck = 120


# -----------------------------------------------------------------------------------


def wall(frame_time):
    if jumper.x < 950:
        game.max_wall = 40

    if jumper.x >= 950:
        game.max_wall = 0

# -----------------------------------------------------------------------------------


def height(frame_time):
    if jumper.x > 865:
        game.height = 0

    if jumper.x < 170:
        game.height = 317 - game.y

    if jumper.x >= 170 and jumper.x <= brick.x_3 + 50 \
            or jumper.x >= brick.x_3 - 50 and jumper.x <= brick.x_2 + 50 \
            or jumper.x >= brick.x_2 - 50 and jumper.x <= brick.x_1 + 50\
            or jumper.x >= brick.x_1 - 50 and jumper.x <= 865:
                game.height = -54
                jumper.y -= 1


# -----------------------------------------------------------------------------------

def text(frame_time):
    # text for player :)
    font.draw(450, 12, "TIMING  IS  KEY", (255, 255, 255))


# -----------------------------------------------------------------------------------

def collision(frame_time):
    if collide(jumper, spike):
        game.reset = True
        framework.push_state(level_4)


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
        framework.push_state(level_5)

    if jumper.x >= game.max_x:
        framework.push_state(level_3)


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


