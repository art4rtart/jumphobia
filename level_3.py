# -----------------------------------------------------------------------------------
from pico2d import *
import framework
import game
import level_3
import level_4
# -----------------------------------------------------------------------------------
from jumper import Jumper
from obstacle import Spike, Spike2, Monster, Flag
# -----------------------------------------------------------------------------------
name = "level_3"
# -----------------------------------------------------------------------------------
jumper, spike, spike2, monster, flag = None, None, None, None, None
level, blink, sign, font = None, None, None, None
falling_state = None
monster_collide = None
# -----------------------------------------------------------------------------------


def create_world():
    global jumper, spike, spike2, monster, flag, level, blink, sign, font, monster_collide, falling_state

    # game class import
    jumper = Jumper()
    spike = Spike()
    spike2 = Spike2()
    monster = Monster()
    flag = Flag()

    # game image load
    level = load_image("level_3.png")
    blink = load_image("blink.png")
    sign = load_image("sign.png")
    font = load_font("overwatch.TTF", 25)

    # game initialize
    game.gak = 280
    game.gck = 80
    game.flying = 0
    game.jumping = 0
    game.min_x, game.max_x = 0, 1000
    game.min_wall, game.max_wall = 40, 40
    game.jump_x, game.jump_y = 11, 20
    game.x, game.y = 950, 322

    # class initialize
    jumper.life = 1
    jumper.x, jumper.y = 950, 474
    jumper.state = Jumper.STANDLEFT
    spike.x, spike.y = 743, 200
    spike2.x, spike2.y = 412, 125
    spike.box_x, spike.box_y = 147, 10
    spike2.box_x, spike2.box_y = 108, 10
    monster.x, monster.y = 400, 180
    flag.x, flag.y = 590, 320

    # boolean initialize
    game.monster = True
    falling_state = True
    monster_collide = 0


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
    # update ----------------------------------
    jumper.update(frame_time)
    logic(frame_time)
    wall(frame_time)
    height(frame_time)
    collision(frame_time)
    change_level(frame_time)
    # -----------------------------------------
    update_canvas()


def draw(frame_time):
    global monster_collide
    clear_canvas()
    # draw objects ----------------------------
    level.draw(game.back_x, game.back_y)
    flag.draw()
    jumper.draw()
    text(frame_time)
    if monster_collide == 0:
        monster.draw()
    # draw bounding box -----------------------
    # jumper.draw_bb()
    # monster.draw_bb()
    # spike.draw_bb()
    # spike2.draw_bb()
    # -----------------------------------------
    update_canvas()


# -----------------------------------------------------------------------------------

def logic(frame_time):
    global falling_state

    if (jumper.x < 845 and jumper.x > 630) and jumper.y == 322 \
            or jumper.x > 430 and jumper.x < 525 and jumper.y == 182 \
            or jumper.x > 300 and jumper.y == 286 \
            or jumper.x < 365 and jumper.y == 182\
            or jumper.x < 525 and jumper.y >= 322 \
            or jumper.x < 230 and jumper.y == 286 \
            or monster_collide == 1:

        if jumper.state == Jumper.RUNRIGHT:
            jumper.state = Jumper.STANDRIGHT
            game.jumping = 1
            jumper.state = Jumper.JUMPRIGHT

        if jumper.state == Jumper.RUNLEFT:
            jumper.state = Jumper.STANDLEFT
            game.jumping = 1
            jumper.state = Jumper.JUMPLEFT

        if jumper.state == Jumper.STANDLEFT:
            game.jumping = 1
            jumper.state = Jumper.JUMPLEFT

    if jumper.y >= 324 and falling_state is True:
        jumper.y -= 8

    if jumper.y == 322:
        falling_state = False
        game.key = True

    if jumper.x <= flag.x - 10:
        game.checkpoint = True

    print(game.jump_y)
    if jumper.state == Jumper.JUMPLEFT:
        if jumper.x < 845:
            game.gak = 270
            game.jump_x = 15

        if jumper.x < 525:
            if game.monster is False:
                game.jump_x = 10
                game.gak = 210

        if jumper.x < 250:
            game.jump_x = 10
            game.gak = 300

    if jumper.state == Jumper.JUMPRIGHT:
        if jumper.x > 300:
            game.gck = 120

        if jumper.x > 525:
            game.gck = 90

    if jumper.x < 525:
        game.jump_x = 11


# -----------------------------------------------------------------------------------

def height(frame_time):
    if jumper.x < 525:
        if jumper.x > 360:
            game.height = -140
            game.jump_x = 11
            game.jump_y = 24

    if jumper.x > 430:
        if jumper.x < 525:
            jumper.y -= 3
            game.height = -160
            if jumper.y >= 140:
                jumper.y -= 3.5

    if jumper.x < 360:
        if jumper.x > 300:
            game.height = -160
            if jumper.y >= 140:
                jumper.y -= 3.5

    if jumper.x > 230:
        if jumper.x < 300:
            game.height = -36

    if jumper.x < 230:
        game.height = -127

    if jumper.x < 895:
        if jumper.x > 595:
            # if jumper.state == Jumper.JUMPLEFT:
            game.height = -90

    if jumper.x > 630:
        if jumper.state == Jumper.JUMPRIGHT:
            game.height = -90

    if game.height == -90 and jumper.y <= 232:
        jumper.y -= 1

    if jumper.x < 630 and jumper.x > 525:
        game.height = 0

    if jumper.x > 845:
        game.height = 0


# -----------------------------------------------------------------------------------

def wall(frame_time):
    if jumper.x < 450:
        game.max_wall = 490

    if jumper.x <= 40:
        game.min_wall = 0
    if jumper.x > 40:
        game.min_wall = 40

    if jumper.x < 230:
        game.max_wall = 790

    if jumper.state == Jumper.JUMPRIGHT:
        if jumper.x > 300:
            if jumper.x < 350:
                game.min_wall = 320


# -----------------------------------------------------------------------------------

def text(frame_time):
    # text for player :)
    font.draw(390, 12, "JUMP  ON  THE  HEAD  TO  KILL  IT", (255, 255, 255))


# -----------------------------------------------------------------------------------

def collision(frame_time):
    global monster_collide, falling_state

    if collide(jumper, spike) or collide(jumper, spike2):
        game.reset = True
        framework.push_state(level_3)
        if game.checkpoint:
            jumper.x = flag.x
            jumper.y = flag.y + 2
            falling_state = False
            game.seta = 90

    if jumper.y <= monster.y + 35 and jumper.x >= monster.x - 35 and jumper.x <= monster.x + 25 and game.monster:
        jumper.y += 35
        jumper.x -= 5
        monster_collide = 1

    if monster_collide == 1:
        game.gak = 250

    if jumper.x < 300:
        monster_collide = 2
        game.monster = False


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


