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
from platform import Triangle, Gravity
# -----------------------------------------------------------------------------------
name = "level_1"
# -----------------------------------------------------------------------------------
jumper, triangle_1, triangle_2 = None, None, None
spike_1, spike_2, spike_3, spike_4, spike_5, spike_6 = None, None, None, None, None, None
level, blink, sign, font = None, None, None, None
gravity = None
# -----------------------------------------------------------------------------------


def create_world():
    global jumper, level, blink, sign, font
    global spike_1, spike_2, spike_3, spike_4, spike_5, spike_6, triangle_1, triangle_2
    global gravity

    # game class import
    jumper = Jumper()
    gravity = Gravity()
    spike_1, spike_2, spike_3, spike_4, spike_5, spike_6 = Spike(), Spike(), Spike(), Spike(), Spike(), Spike()
    triangle_1, triangle_2 = Triangle(), Triangle()

    # game image load
    level = load_image("resource/image/levels/level_8.png")
    blink = load_image("resource/image/objects/blink.png")
    sign = load_image("resource/image/objects/sign.png")
    font = load_font("resource/font/overwatch.TTF", 25)

    # game initialize
    game.gravity_stage = True
    game.gravity = False
    game.flying = 0
    game.jumping = 0
    game.x, game.y = 50, 130
    game.gck, game.gak = 90, 270
    game.height = 0
    game.sign_x, game.sign_y = 590, 182
    game.min_x, game.max_x = 0, 1000
    game.min_wall, game.max_wall = 40, 40
    game.jump_x, game.jump_y = 7, 16

    # class initialize
    spike_1.x, spike_1.y = 372, 83
    spike_1.box_x, spike_1.box_y = 226, 10
    spike_2.x, spike_2.y = 415, 351
    spike_2.box_x, spike_2.box_y = 135, 10
    spike_3.x, spike_3.y = 394, 458
    spike_3.box_x, spike_3.box_y = 363, 10
    spike_4.x, spike_4.y = 871, 458
    spike_4.box_x, spike_4.box_y = 91, 10
    spike_5.x, spike_5.y = 768, 192
    spike_5.box_x, spike_5.box_y = 12, 12
    spike_6.x, spike_6.y = 888, 337
    spike_6.box_x, spike_6.box_y = 12, 12

    triangle_1.x_1, triangle_1.y_1 = 220, 210
    triangle_1.x_2, triangle_1.y_2 = 320, 210
    triangle_1.x_3, triangle_1.y_3 = 420, 210

    triangle_2.x_1, triangle_2.y_1 = 270, 210
    triangle_2.x_2, triangle_2.y_2 = 370, 210
    triangle_2.x_3, triangle_2.y_3 = 470, 210

    triangle_1.x_4, triangle_1.y_4 = 169, 351
    triangle_2.x_4, triangle_2.y_4 = 209, 351
    triangle_1.x_5, triangle_1.y_5 = 169, 351
    triangle_2.x_5, triangle_2.y_5 = 209, 351

    gravity.x_1, gravity.y_1 = 100, 135
    gravity.x_2, gravity.y_2 = 620, 345
    gravity.x_3, gravity.y_3 = 700, 150  # handle it

    jumper.x, jumper.y = 50, 130
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
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game.movement = 1

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            game.movement = 2

        if game.key:
            if jumper.life == 1:
                if game.gravity is False:
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

                if game.gravity:
                    if game.jumping == 0:
                        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                            jumper.state = jumper.RUNRIGHTDOWN
                        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                            jumper.state = jumper.RUNLEFTDOWN
                        if (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
                            jumper.state = jumper.STANDRIGHTDOWN
                        if (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
                            jumper.state = jumper.STANDLEFTDOWN

                        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                            game.jumping = 1

                    if game.jumping == 1:
                        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                            game.movement = 1

                        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
                            game.movement = 0

                        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                            game.movement = 2

                        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
                            game.movement = 0

                        if jumper.state == jumper.RUNRIGHTDOWN or jumper.state == jumper.STANDRIGHTDOWN:
                            jumper.state = jumper.JUMPRIGHTDOWN

                        if jumper.state == jumper.RUNLEFTDOWN or jumper.state == jumper.STANDLEFTDOWN:
                            jumper.state = jumper.JUMPLEFTDOWN


def update(frame_time):
    # update ----------------------------------
    jumper.update(frame_time)
    # logic(frame_time)
    wall(frame_time)
    height(frame_time)
    collision(frame_time)
    upside(frame_time)
    # change_level(frame_time)
    # -----------------------------------------
    update_canvas()


def draw(frame_time):
    clear_canvas()
    # draw objects ----------------------------
    level.draw(game.back_x, game.back_y)
    sign.draw(game.sign_x, game.sign_y)
    gravity.draw()
    triangle_1.draw()
    triangle_2.draw()
    jumper.draw()
    text(frame_time)
    # draw bounding box -----------------------
    # jumper.draw_bb()
    gravity.draw_bb_1()
    gravity.draw_bb_2()
    gravity.draw_bb_3()
    # spike_1.draw_bb()
    # spike_2.draw_bb()
    # spike_3.draw_bb()
    # spike_4.draw_bb()
    # spike_5.draw_bb()
    # spike_6.draw_bb()
    # -----------------------------------------
    update_canvas()

# -----------------------------------------------------------------------------------

def upside(frame_time):
    if game.gravity and game.temp == 1:
        game.count += 2
        if jumper.y < 209:
            jumper.y += game.count
            jumper.life = 0

        if jumper.y >= 209:
            jumper.y = 209
            jumper.state = Jumper.STANDLEFTDOWN
            game.count = 0
            game.temp = 0
            game.change_motion = False
            jumper.frame2 = 0
            jumper.life = 1

    if game.gravity is False and game.temp == 0:
        game.move += 2
        if jumper.y > 129:
            jumper.y -= game.move
            jumper.life = 0

        if jumper.x < 500:
            if jumper.y <= 129:
                jumper.y = 129
                jumper.state = Jumper.STANDRIGHT
                game.move = 0
                game.temp = 1
                game.change_motion = False
                jumper.frame2 = 0
                jumper.life = 1

        if jumper.x > 500:
            if jumper.y <= 183:
                jumper.y = 183
                jumper.state = Jumper.STANDRIGHT
                game.move = 0
                game.temp = 1
                game.change_motion = False
                jumper.frame2 = 0
                jumper.life = 1

def logic(frame_time):
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

def wall(frame_time):
    print(jumper.x, jumper.y)

    if jumper.x > 50:
        game.min_wall = 50

    if jumper.x <= 50 and jumper.y == 130:
        game.min_wall = 0

    if jumper.x >= 635 and jumper.y == 185:
        game.max_wall = 375

    if jumper.x >= 635 and jumper.y == 367:
        game.max_wall = 265


# -----------------------------------------------------------------------------------

def height(frame_time):
    if jumper.x < 145:
        if jumper.y <= 230:
            game.height = 0

    if jumper.x > 115:
        if jumper.x < 145:
            game.height = 0

    if jumper.x > 40:
        if jumper.x < 115:
            if jumper.y >= 250:
                game.height = 250 - game.y

    if jumper.x > 605:
        if jumper.x < 640:
            game.height = 185 - game.y

    if jumper.x > 195:
        if jumper.x < 650:
            if jumper.y >= 390:
                game.height = 390 - game.y


# -----------------------------------------------------------------------------------

def text(frame_time):
    # text for player :)
    font.draw(450, 12, "NEED  TO  USE  YOUR  BRAIN !", (255, 255, 255))

    font.draw(535, 285, "DID YOU LEAVE", (255, 255, 255))
    font.draw(550, 255, "YOURSELF..", (255, 255, 255))
    font.draw(535, 225, "A WAY BACK ?", (255, 50, 50))

    if jumper.x > game.sign_x - 20:
        if jumper.x < game.sign_x + 20:
            font.draw(535, 285, "DID YOU LEAVE", (255, 255, 255))
            font.draw(555, 255, "YOURSELF", (255, 255, 255))
            font.draw(535, 225, "A WAY BACK ?", (255, 50, 50))


# -----------------------------------------------------------------------------------

def collision(frame_time):
    if collide(jumper, spike_1):
        game.reset = True
        framework.push_state(level_3)

    if collide_1(jumper, gravity):
        game.gravity = True
        jumper.state = Jumper.CHANGEUP
        game.temp = 1
        game.move = 0
        game.change_motion = True

    if collide_2(jumper, gravity):
        game.gravity = False
        jumper.state = Jumper.CHANGEDOWN
        game.temp = 0
        game.count = 0
        game.change_motion = True

    if collide_3(jumper, gravity):
        game.gravity = False
        jumper.state = Jumper.CHANGEDOWN
        game.temp = 0
        game.count = 0
        game.change_motion = True

    if game.change_motion:
        if jumper.frame2 < 10:
            jumper.frame2 += 1


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


