# -----------------------------------------------------------------------------------
from pico2d import *
import framework
import game
import level_4
import level_5
import level_6
# -----------------------------------------------------------------------------------
from jumper import Jumper
from obstacle import Spike, Spike2, Monster
from platform import Triangle

# -----------------------------------------------------------------------------------
name = "level_5"
# -----------------------------------------------------------------------------------
jumper, spike, spike2, monster, triangle = None, None, None, None, None
level, blink, sign, font = None, None, None, None


# -----------------------------------------------------------------------------------


def create_world():
    global jumper, spike, spike2, triangle, monster, level, blink, sign, font

    # game class import
    jumper = Jumper()
    spike = Spike()
    spike2 = Spike2()
    triangle = Triangle()
    monster = Monster()

    # game image load
    level = load_image("level_5.png")
    blink = load_image("blink.png")
    sign = load_image("sign.png")
    font = load_font("overwatch.TTF", 25)

    # game initialize
    game.flying = 0
    game.height = 0
    game.x, game.y = 950, 316
    game.min_x, game.max_x = 0, 1000
    game.min_wall, game.max_wall = 40, 0
    game.jump_x, game.jump_y = 10, 20
    game.sign_x, game.sign_y = 745, 291
    game.gck, game.gak = 90, 270
    game.t1, game.t2, game.t3, game.t4 = False, False, False, False
    game.godown = False
    game.key = True
    game.monster = True

    # class initialize
    jumper.x, jumper.y = 950, 316
    spike.x, spike.y = 395, 127
    spike.box_x, spike.box_y = 310, 10
    spike2.x, spike2.y = 843, 165
    spike2.box_x, spike2.box_y = 57, 10
    monster.x, monster.y = 174, 250
    triangle.opacify_1, triangle.opacify_2, triangle.opacify_3, triangle.opacify_4 = 1, 1, 1, 1
    jumper.life = 1
    jumper.state = Jumper.STANDLEFT


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


def update(frame_time):
    # update ----------------------------------
    jumper.update(frame_time)
    triangle.update(frame_time)
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
    triangle.draw()
    if game.monster:
        monster.draw()
    text(frame_time)
    # draw bounding box -----------------------
    # jumper.draw_bb()
    # spike.draw_bb()
    # spike2.draw_bb()
    # monster.draw_bb()
    # triangle.draw_bb_1()
    # triangle.draw_bb_2()
    # triangle.draw_bb_3()
    # triangle.draw_bb_4()
    # -----------------------------------------
    update_canvas()


# -----------------------------------------------------------------------------------

def logic(frame_time):
    if jumper.x < 905 and jumper.x > 785 \
            or jumper.x < 280:
        if jumper.state == Jumper.RUNRIGHT:
            jumper.state = Jumper.STANDRIGHT
            game.jumping = 1
            jumper.state = Jumper.JUMPRIGHT

        if jumper.state == Jumper.RUNLEFT:
            jumper.state = Jumper.STANDLEFT
            game.jumping = 1
            jumper.state = Jumper.JUMPLEFT

    if jumper.x > 608 and triangle.opacify_1 > 0 and game.t1 is True\
            or jumper.x < 470 and triangle.opacify_4 > 0 \
            or jumper.x > 375 and jumper.y == 293 \
            or jumper.x < 705 and jumper.y == 294:
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
    if jumper.x > 905:
        game.height = 0

    if jumper.x > 785:
        if jumper.x < 905:
            game.height = -70
            if jumper.y <= 250:
                game.key = False
                jumper.y -= 6

    if jumper.x < 785:
        if jumper.x > 705:
            game.height = 294 - game.y

    if jumper.x < 470:
        if jumper.x > 375:
            game.height = -70
            if jumper.y <= 250:
                game.key = False
                jumper.y -= 6

    if jumper.x < 705:
        if jumper.x > 608:
            game.height = -70
            if jumper.y <= 250:
                game.key = False
                jumper.y -= 6

    if jumper.x < 608:
        if jumper.x > 475:
            if jumper.x > triangle.x_1 - 19:
                if jumper.x < triangle.x_1 + 17:
                    if triangle.opacify_1 > 0:
                        game.height = 292 - game.y
                    elif triangle.opacify_1 < 0:
                        game.height = -70
                        game.godown = True

            if jumper.x > triangle.x_2 - 19:
                if jumper.x < triangle.x_2 + 17:
                    if triangle.opacify_2 > 0:
                        game.height = 292 - game.y
                    elif triangle.opacify_2 < 0:
                        game.height = -70
                        game.godown = True

            if jumper.x > triangle.x_3 - 19:
                if jumper.x < triangle.x_3 + 17:
                    if triangle.opacify_3 > 0:
                        game.height = 292 - game.y
                    elif triangle.opacify_3 < 0:
                        game.height = -70
                        game.godown = True

            if jumper.x > triangle.x_4 - 19:
                if jumper.x < triangle.x_4 + 17:
                    if triangle.opacify_4 > 0:
                        game.height = 292 - game.y
                    elif triangle.opacify_4 < 0:
                        game.height = -70
                        game.godown = True

    if jumper.x < 375:
        if jumper.x > 280:
            game.height = 293 - game.y

    if jumper.x < 280:
        game.gak = 290
        game.height = -70
        if jumper.y <= 250:
            game.key = False
            jumper.y -= 9

    if game.godown:
        jumper.y -= 6


# -----------------------------------------------------------------------------------

def wall(frame_time):
    if jumper.x > 375:
        if jumper.x < 705:
            if jumper.y < 292:
                game.max_wall = 310
                game.min_wall = 390

    if jumper.x < 280:
        game.max_wall = 850

    if jumper.state == Jumper.JUMPLEFT:
        if jumper.x < 905:
            if jumper.x > 785:
                game.max_wall = 100

        if jumper.x < 705:
            if jumper.x > 375:
                game.max_wall = 320

    if jumper.state == Jumper.JUMPRIGHT:
        if jumper.x < 905:
            if jumper.x > 795:
                game.min_wall = 800

        if jumper.x < 705:
            if jumper.x > 375:
                game.min_wall = 400


# -----------------------------------------------------------------------------------

def text(frame_time):
    # text for player :)
    font.draw(450, 12, "PEACE  OF  CAKE", (255, 255, 255))

    if jumper.x > game.sign_x - 50:
        if jumper.x < game.sign_x + 50:
            if jumper.y == 294:
                font.draw(655, 380, "FALLING PLATFORMS RESET", (255, 255, 255))
                font.draw(697, 340, "WHEN YOU DIE", (255, 255, 255))


# -----------------------------------------------------------------------------------

def collision(frame_time):
    if collide(jumper, spike) or collide(jumper, spike2):
        game.reset = True
        framework.push_state(level_5)

    if collide(jumper, monster):
        jumper.y += 45
        jumper.state = Jumper.STANDLEFT
        game.jumping = 1
        jumper.state = Jumper.JUMPLEFT
        game.monster = False

    if collide_1(jumper, triangle) and triangle.opacify_1 > 0:
        game.t1 = True

    if collide_2(jumper, triangle):
        game.t2 = True

    if collide_3(jumper, triangle):
        game.t3 = True

    if collide_4(jumper, triangle):
        game.t4 = True


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
        framework.push_state(level_4)

    if jumper.y <= 39:
        framework.push_state(level_6)


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


def collide_1(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb_1()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True


def collide_2(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb_2()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True


def collide_3(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb_3()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True


def collide_4(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb_4()

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


