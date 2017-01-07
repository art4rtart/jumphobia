# -----------------------------------------------------------------------------------
from pico2d import *
import framework
import game
import level_0
import level_1
import level_2
# -----------------------------------------------------------------------------------
from jumper import Jumper
from obstacle import Spike, Flag
# -----------------------------------------------------------------------------------
name = "level_1"
# -----------------------------------------------------------------------------------
jumper, spike, flag = None, None, None
level, blink, sign, font = None, None, None, None
# -----------------------------------------------------------------------------------


def create_world():
    global jumper, spike, flag, level, blink, sign, font

    # game class import
    jumper = Jumper()
    spike = Spike()
    flag = Flag()

    # game image load
    level = load_image("level_1.png")
    blink = load_image("blink.png")
    sign = load_image("sign.png")
    font = load_font("overwatch.TTF", 25)

    # game initialize
    game.gck = 70
    game.flying = 0
    game.wall = 0
    game.sign_x, game.sign_y = 420, 228
    game.min_x, game.max_x = 0, 1000
    game.min_wall, game.max_wall = 0, 0

    # class initialize
    spike.x, spike.y = 575, 130
    spike.box_x, spike.box_y = 300, 10
    flag.x, flag.y = 685, 206


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
    # update ----------------------------------
    jumper.update(frame_time)
    logic(frame_time)
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
    flag.draw()
    jumper.draw()
    text(frame_time)
    # draw bounding box -----------------------
    # jumper.draw_bb()
    # spike.draw_bb()
    # -----------------------------------------
    update_canvas()

# -----------------------------------------------------------------------------------


def logic(frame_time):
    if jumper.x > 95 and jumper.x < 155 \
            or jumper.x > 259 and jumper.x < 365 \
            or jumper.x > 465 and jumper.x < 640 \
            or jumper.x > 705 and jumper.x < 875:
        if jumper.state == Jumper.RUNRIGHT:
            jumper.state = Jumper.STANDRIGHT
            game.jumping = 1
            jumper.state = Jumper.JUMPRIGHT

        if jumper.state == Jumper.RUNLEFT:
            jumper.state = Jumper.STANDLEFT
            game.jumping = 1
            jumper.state = Jumper.JUMPLEFT

    if jumper.x > 105 and jumper.x < 145 and jumper.y <= game.y \
            or jumper.x > 265 and jumper.x < 355 and jumper.y <= game.y + game.wall \
            or jumper.x > 475 and jumper.x < 630 and jumper.y <= game.y + game.wall \
            or jumper.x > 715 and jumper.x < 865 and jumper.y <= game.y + game.wall:
        jumper.life = 0
    else:
        jumper.life = 1

    if jumper.life == 0:
        jumper.y -= game.falling

    if jumper.x > 0:
        if jumper.x < 115:
            game.wall = 0

    if jumper.x > 135:
        if jumper.x < 275:
            game.wall = 54

    if jumper.x > 345:
        if jumper.x < 485:
            game.wall = 96

    if jumper.x > 615:
        if jumper.x < 720:
            game.wall = 74

    if jumper.x > 850:
        if jumper.x < 1000:
            game.wall = 62

    if jumper.x >= flag.x - 10:
        game.checkpoint = True

    if jumper.x > 460:
        game.gck = 100
        game.gak = 260

    elif jumper.x < 460:
        game.gck = 70
        game.gak = 290

    print(game.gak)


# -----------------------------------------------------------------------------------

def wall(frame_time):
    if jumper.x > 40:
        game.min_wall = 40
    elif jumper.x <= 40:
        game.min_wall = 0

    if jumper.x < 960:
        game.max_wall = 40
    elif jumper.x >= 960:
        game.max_wall = 0


# -----------------------------------------------------------------------------------

def text(frame_time):
    font.draw(450, 12, "PEACE  OF  CAKE", (255, 255, 255))

    # text for player :)
    if jumper.x > game.sign_x - 50:
        if jumper.x < game.sign_x + 50:
            font.draw(350, 340, "CHECKPOINT FLAGS", (255, 90, 90))
            font.draw(355, 300, "ARE VERY HELPFUL", (255, 255, 255))

    if jumper.x > game.sign_x + 230:
        if jumper.x < game.sign_x + 235 + 50:
            if jumper.state == Jumper.STANDRIGHT or Jumper.RUNRIGHT:
                if game.jumped == 0:
                    font.draw(650, 280, "EXCELLENT !", (255, 255, 255))
                    game.count += 1
                    if game.count > 10:
                        game.jumped = 1

    if jumper.x < game.sign_x + 190:
        game.count = 0
        game.jumped = 0


# -----------------------------------------------------------------------------------

def collision(frame_time):
    if collide(jumper, spike):
        game.reset = True
        framework.push_state(level_1)
        if game.checkpoint:
            jumper.x = flag.x
            jumper.y = flag.y + 1


# -----------------------------------------------------------------------------------

def change_level(frame_time):
    if game.reset:
        blink.draw(game.back_x, game.back_y)
        game.temp += 1

    if game.temp > 2:
        game.reset = False

    if jumper.x <= game.min_x:
        game.x, game.y = 980, jumper.y
        game.change_level = True
        game.motion = True
        framework.push_state(level_0)

    if jumper.x >= game.max_x:
        game.checkpoint = False
        game.change_level = False
        game.motion = False
        framework.push_state(level_2)


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


