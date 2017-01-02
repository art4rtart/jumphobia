# -----------------------------------------------------------------------------------
from pico2d import *
import framework
import game
import level_1
import level_2
import level_3
# -----------------------------------------------------------------------------------
from jumper import Jumper
from obstacle import Spike
# -----------------------------------------------------------------------------------
name = "level_1"
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
    level = load_image("level_2.png")
    blink = load_image("blink.png")
    sign = load_image("sign.png")
    font = load_font("overwatch.TTF", 25)

    # game initialize
    game.x, game.y = 25, 196
    game.flying = 0
    game.sign_x, game.sign_y = 870, 372
    game.min_x, game.max_x = 0, 1000
    game.min_wall, game.max_wall = 40, 40

    # class initialize
    jumper.x, jumper.y = 25, 196
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
        if game.key:
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
        # 치트키
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            jumper.y += 2

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            jumper.y -= 2

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game.jumping = 1


def update(frame_time):
    # update ----------------------------------
    jumper.update(frame_time)
    logic(frame_time)
    wall(frame_time)
    # collision(frame_time)
    change_level(frame_time)
    # -----------------------------------------
    update_canvas()


def draw(frame_time):
    clear_canvas()
    # draw objects ----------------------------
    level.draw(game.back_x, game.back_y)
    sign.draw(game.sign_x, game.sign_y)
    jumper.draw()
    text(frame_time)
    # draw bounding box -----------------------
    # jumper.draw_bb()
    # spike.draw_bb()
    # -----------------------------------------
    update_canvas()

# -----------------------------------------------------------------------------------


def logic(frame_time):
    if jumper.y < 0:
        collision(frame_time)

    print(jumper.x, jumper.y)
    # print(game.wall)

    if jumper.x > 70 and jumper.y == game.y \
        or jumper.x > 135 and jumper.y == game.y - 46 \
            or (jumper.x < 190 or jumper.x > 330) and jumper.y == game.y + 44 \
            or (jumper.x < 325 or jumper.x > 467) and jumper.y == 314 \
            or (jumper.x < 555 or jumper.x > 605) and jumper.y == 206 \
            or (jumper.x < 685 or jumper.x > 730) and jumper.y == 310 \
            or jumper.x < 740 and jumper.y == 222 \
            or (jumper.x > 920 or jumper.x < 825) and jumper.y == 374:
        if jumper.state == Jumper.RUNRIGHT:
            jumper.state = Jumper.STANDRIGHT
            game.jumping = 1
            jumper.state = Jumper.JUMPRIGHT

        if jumper.state == Jumper.RUNLEFT:
            jumper.state = Jumper.STANDLEFT
            game.jumping = 1
            jumper.state = Jumper.JUMPLEFT

    if jumper.x > 145:
        if jumper.x < 190 and jumper.y <= game.y - 46:
            jumper.life = 0
    else:
        jumper.life = 1

    if jumper.life == 0:
        jumper.y -= game.falling

    if jumper.x > 330:
        game.wall = 314 - game.y

    if jumper.x > 185:
        if jumper.x < 330:
            game.wall = 44

    if jumper.x > 467:
        game.wall = 206 - game.y

    if jumper.x > 685:
        if jumper.x < 730:
            game.wall = 310 - game.y

    if jumper.x > 730:
        if jumper.x < 825:
            game.wall = 222 - game.y

    if jumper.x > 825:
        game.wall = 374 - game.y

    if (jumper.x > 920 or jumper.x < 830) and jumper.y == 374:
        game.key = False
        game.jump_x = 3
        game.jump_y = 10

    elif jumper.x < 800:
        game.jump_x = 11
        game.jump_y = 20

    if jumper.x > 930 and game.seta == 90:
        jumper.y -= 8


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

    if jumper.x > 70:
        if jumper.x < 140:
            game.wall = -46
            if jumper.y < 196:
                game.min_wall = 95
            else:
                game.min_wall = 40

    if jumper.x < 80:
        game.wall = 0
        game.min_wall = 40

    if jumper.y == 222:
        game.key = True
        game.max_wall = 190

    if jumper.y != 222:
        game.max_wall = 40

# -----------------------------------------------------------------------------------


def text(frame_time):
    # text for player :)
    font.draw(350, 12, "YOU  CAN  JUMP  UP  TROUGH  PLATFORM", (255, 255, 255))

    if jumper.x > game.sign_x - 50:
        if jumper.x < game.sign_x + 50:
            font.draw(810, 450, "JUMP DOWN THE", (255, 255, 255))
            font.draw(850, 420, "HOLE !", (255, 255, 255))


# -----------------------------------------------------------------------------------

def collision(frame_time):
    if collide(jumper, spike):
        game.reset = True
        framework.push_state(level_2)


# -----------------------------------------------------------------------------------

def change_level(frame_time):
    if game.reset:
        blink.draw(game.back_x, game.back_y)
        game.temp += 1

    if game.temp > 2:
        game.reset = False

    if jumper.x <= game.min_x:
        game.change_level = True
        game.motion = True
        game.x = 980
        framework.push_state(level_1)

    if jumper.y < 44:
        game.checkpoint = False
        game.change_level = False
        game.motion = False
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


