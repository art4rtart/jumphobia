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
name = "level_0"
# -----------------------------------------------------------------------------------
jumper, spike = None, None
level, blink, sign, font = None, None, None, None
# -----------------------------------------------------------------------------------


def create_world():
    global jumper, spike, level, blink, sign, font

    # game class import
    jumper = Jumper()
    spike = Spike()

    # game image load
    level = load_image("level_0.png")
    blink = load_image("blink.png")
    sign = load_image("sign.png")
    font = load_font("overwatch.TTF", 25)

    # game initialize
    game.flying = 0
    game.sign_x, game.sign_y = 150, 131
    game.min_x, game.max_x = 40, 1000
    game.gck = 90

    # class initialize
    spike.x, spike.y = 520, 80
    spike.box_x, spike.box_y = 300, 10


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
    # -----------------------------------------
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
    sign.draw(game.sign_x + 400, game.sign_y)
    jumper.draw()
    text(frame_time)
    # draw bounding box -----------------------
    # jumper.draw_bb()
    # spike.draw_bb()
    # -----------------------------------------
    update_canvas()

# -----------------------------------------------------------------------------------


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
        jumper.y -= game.falling

# -----------------------------------------------------------------------------------


def wall(frame_time):
    if jumper.y == game.y:
        if jumper.x < 960:
            game.max_wall = 40
        elif jumper.x >= 960:
            game.max_wall = 0


# -----------------------------------------------------------------------------------

def text(frame_time):
    font.draw(410, 12, "WAIT..  HOW  DO  I  JUMP  ?", (255, 255, 255))

    # text for player :)
    if jumper.x > game.sign_x - 50:
        if jumper.x < game.sign_x + 50:
            font.draw(60, 260, "YOU", (255, 255, 255))
            font.draw(96, 260, "AUTOMATICALLY", (255, 50, 50))
            font.draw(215, 260, "JUMP", (255, 255, 255))

            font.draw(55, 220, "WHEN YOU", (255, 255, 255))
            font.draw(135, 220, "RUN OFF A LEDGE", (255, 50, 50))

    if jumper.x > game.sign_x + 190:
        if jumper.x < game.sign_x + 250:
            if jumper.state == Jumper.STANDRIGHT:
                if game.jumped == 0:
                    font.draw(320, 230, "NICE  JUMP !", (255, 255, 255))
                    game.count += 1
                    if game.count > 10:
                        game.jumped = 1

    if jumper.x < game.sign_x + 190:
        game.count = 0
        game.jumped = 0

    if jumper.x > (game.sign_x + 400) - 50:
        if jumper.x < (game.sign_x + 400) + 50:
            font.draw(440, 280, "PRESS", (255, 255, 255))
            font.draw(490, 280, "RIGHT KEY", (255, 50, 50))
            font.draw(500, 240, "WHILE JUMPING", (255, 255, 255))
            font.draw(550, 200, "TO JUMP FURTHER", (255, 255, 255))

    if jumper.x > (game.sign_x + 400) + 235:
        if jumper.x < (game.sign_x + 400) + 295:
            if jumper.state == Jumper.STANDRIGHT or Jumper.RUNRIGHT:
                if game.jumped == 0:
                    font.draw(750, 230, "BRILLIANT !", (255, 255, 255))
                    game.count += 1
                    if game.count > 10:
                        game.jumped = 1

    if jumper.x < (game.sign_x + 400) + 235:
        game.count = 0
        game.jumped = 0


# -----------------------------------------------------------------------------------

def collision(frame_time):
    if collide(jumper, spike):
        game.reset = True
        framework.push_state(level_0)

        if game.motion:
            jumper.state = Jumper.STANDLEFT


# -----------------------------------------------------------------------------------

def change_level(frame_time):
    if jumper.x >= game.max_x:
        game.x = 20
        jumper.state = Jumper.STANDRIGHT
        game.motion = False
        game.change_level = True
        framework.push_state(level_1)

    game.change_level = False

    if game.reset:
        blink.draw(game.back_x, game.back_y)
        game.temp += 1

    if game.temp > 2:
        game.reset = False

    if game.change_level:
        jumper.state = Jumper.STANDLEFT


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


