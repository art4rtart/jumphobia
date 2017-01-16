# -----------------------------------------------------------------------------------
from pico2d import *
import framework
import game
import level_6
import level_7
import level_8
# -----------------------------------------------------------------------------------
from jumper import Jumper
from obstacle import Spike, Spike2, Flag, Monster, MonsterGravity
from platform import Gravity, P1, P2, P3, P4, P5
# -----------------------------------------------------------------------------------
name = "level_7"
# -----------------------------------------------------------------------------------
jumper, spike, spike2, gravity, monster_1, monster_2 = None, None, None, None, None, None
level, blink, sign, font = None, None, None, None
p1, p2, p3, p4, p5, mg_1, mg_2, flag = None, None, None, None, None, None, None, None
monster1, monster2 = True, True
# -----------------------------------------------------------------------------------


def create_world():
    global jumper, spike, spike2, level, blink, sign, font, gravity, monster_1, monster_2, mg_1, mg_2, flag
    global p1, p2, p3, p4, p5, monster1, monster2

    # game class import
    jumper = Jumper()
    spike = Spike()
    spike2 = Spike2()
    gravity = Gravity()
    mg_1 = MonsterGravity()
    mg_2 = MonsterGravity()
    flag = Flag()

    monster_1, monster_2 = Monster(), Monster()
    p1, p2, p3, p4, p5 = P1(), P2(), P3(), P4(), P5()

    # game image load
    level = load_image("level_7.png")
    blink = load_image("blink.png")
    sign = load_image("sign2.png")
    font = load_font("overwatch.TTF", 25)

    # game initialize
    game.gravity_stage = True
    game.flying, game.jumping, game.falling = 0, 0, 1
    game.x, game.y = 30, 129
    game.jump_x, game.jump_y = 10, 22
    game.gck, game.gak = 90, 290

    game.count = 0
    game.temp = 1

    game.seta = 90
    game.sign_x, game.sign_y = 120, 398
    game.min_x, game.max_x = 0, 1000
    game.min_wall, game.max_wall = 40, 50
    game.gravity = False
    game.goup, game.godown = False, False

    # class initialize
    jumper.x, jumper.y = 30, 129
    jumper.life = 1
    jumper.state = Jumper.STANDRIGHT

    gravity.x_1, gravity.y_1 = 180, 140
    gravity.x_2, gravity.y_2 = 50, 380
    gravity.x_3, gravity.y_3 = 875, 380

    spike.x, spike.y = 576, 425
    spike.box_x, spike.box_y = 386, 10
    spike2.x, spike2.y = 525, 90
    spike2.box_x, spike2.box_y = 328, 10

    monster_1.x, monster_1.y = 660, 350
    monster_2.x, monster_2.y = 765, 350
    mg_1.x, mg_1.y = 660, 350
    mg_2.x, mg_2.y = 765, 350

    p2.x, p2.y = 350, 350
    p3.x, p3.y = 490, 280

    flag.x, flag.y = 500, 262
    monster1, monster2 = True, True


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
    gravity.update(frame_time)
    logic(frame_time)
    height(frame_time)
    wall(frame_time)
    upside(frame_time)
    collision(frame_time)
    change_level(frame_time)
    # -----------------------------------------
    update_canvas()


def draw(frame_time):
    global monster1, monster2
    clear_canvas()
    # draw objects ----------------------------
    level.draw(game.back_x, game.back_y)
    sign.draw(game.sign_x, game.sign_y)
    gravity.draw()
    flag.draw()
    jumper.draw()
    text(frame_time)
    p2.draw()
    p3.draw()
    if monster1 is True:
        mg_1.draw()
    if monster2 is True:
        mg_2.draw()
    # draw bounding box -----------------------
    # p2.draw_bb()
    # p3.draw_bb()
    # jumper.draw_bb()
    # gravity.draw_bb_1()
    # gravity.draw_bb_2()
    # gravity.draw_bb_3()
    # monster_1.draw_bb()
    # monster_2.draw_bb()
    # spike.draw_bb()
    # spike2.draw_bb()
    # -----------------------------------------
    update_canvas()

# -----------------------------------------------------------------------------------


def logic(frame_time):
    if jumper.x > 185 and jumper.x < p2.x - 92 \
        or jumper.x > p2.x + 90 and jumper.y == 329 \
            or jumper.x < p3.x - 68 and jumper.y == 259 \
            or jumper.x > p3.x + 68 and jumper.y == 259:
        if jumper.state == Jumper.RUNRIGHTDOWN:
            jumper.state = Jumper.STANDRIGHTDOWN
            game.jumping = 1
            jumper.state = Jumper.JUMPRIGHTDOWN

        if jumper.state == Jumper.RUNLEFTDOWN:
            jumper.state = Jumper.STANDLEFTDOWN
            game.jumping = 1
            jumper.state = Jumper.JUMPLEFTDOWN

    if jumper.x > 195 and jumper.x < 860:
        if jumper.state == Jumper.RUNRIGHT:
            jumper.state = Jumper.STANDRIGHT
            game.jumping = 1
            jumper.state = Jumper.JUMPRIGHT

        if jumper.state == Jumper.RUNLEFT:
            jumper.state = Jumper.STANDLEFT
            game.jumping = 1
            jumper.state = Jumper.JUMPLEFT

    if jumper.state == Jumper.JUMPRIGHTDOWN:
        if jumper.x < p3.x + 68:
            game.jump_y = 22
            game.gak = 70
        if jumper.x > p3.x + 68:
            game.jump_y = 15
            game.gak = 120

    if jumper.state == Jumper.JUMPLEFTDOWN:
        game.jump_y = 18
        game.gck = -310
    if game.gravity is False and game.jumping == 0:
        game.seta = 90
        game.gak = 270
        game.gck = 90

    if game.gravity and game.jumping == 0:
        game.seta = -90
        game.gak = 90
        game.gck = -270


# -----------------------------------------------------------------------------------

def upside(frame_time):
    if game.gravity and game.temp == 1:
        game.count += 2
        if jumper.y < 394:
            jumper.y += game.count
            jumper.life = 0

        if jumper.y >= 394:
            jumper.y = 394
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


# -----------------------------------------------------------------------------------

def height(frame_time):
    if game.gravity:
        if jumper.x < 185:
            game.height = 394 - game.y

        if jumper.x > 185:
            if jumper.x < p2.x - 92:
                game.height = 394 - game.y
                jumper.y += 0.9

        if jumper.x > p2.x - 92:
            if jumper.x < p2.x + 90:
                game.height = 329 - game.y

        if jumper.x > p3.x - 68:
            if jumper.x < p3.x + 68:
                if jumper.y >= p3.y - 3:
                    game.height = 259 - game.y

        if jumper.x > p3.x + 68:
            if jumper.x < monster_1.x - 15:
                game.height = 335 - game.y
                if game.seta == -90:
                    jumper.y += 6

        if jumper.x > monster_1.x - 15:
            if jumper.x < monster_1.x + 15:
                game.height = 319 - game.y

        if jumper.x > monster_1.x + 15:
            if jumper.x < monster_2.x - 15:
                game.height = 330 - game.y
                if game.seta == -90:
                    jumper.y += 6

        if jumper.x > monster_2.x - 15:
            if jumper.x < monster_2.x + 15:
                game.height = 330 - game.y

        if jumper.x > monster_2.x + 15:
            if jumper.x < gravity.x_3 - 10:
                game.height = 335 - game.y
                if game.seta == -90:
                    jumper.y += 6

        if jumper.x > gravity.x_3 - 10:
            if jumper.x < gravity.x_3 + 10:
                game.height = 359 - game.y

        if jumper.x > gravity.x_3 + 10:
            game.height = 335 - game.y
            if game.seta == -90:
                jumper.y += 6

    if jumper.x > 195:
        if jumper.x < 860:
            if jumper.state == Jumper.JUMPLEFT:
                game.gak = 290
                game.height = 125 - game.y
                if game.seta == 90:
                    jumper.y += 5
                    game.godown = True

    if jumper.x > p2.x + 90:
        if jumper.x < monster_1.x - 15:
            if jumper.y == 335:
                game.goup = True

    if game.godown:
        jumper.y -= 6

    if game.goup:
        jumper.y += 6


# -----------------------------------------------------------------------------------

def wall(frame_time):
    if jumper.x > 40:
        game.min_wall = 40

    if jumper.x <= 40:
        game.min_wall = 0

    if jumper.x < 950:
        game.max_wall = 50

    if jumper.x >= 950 and jumper.y == 183:
        game.max_wall = 0


# -----------------------------------------------------------------------------------

def text(frame_time):
    # text for player :)
    font.draw(440, 12, "FEEL  THE  GRAVITY", (255, 255, 255))

    if jumper.x > game.sign_x - 20:
        if jumper.x < game.sign_x + 20:
            if jumper.y == 394:
                font.draw(77, 340, "YOU CAN GET", (255, 255, 255))
                font.draw(75, 310, "UPSIDE DOWN", (255, 50, 50))


# -----------------------------------------------------------------------------------

def collision(frame_time):
    print(jumper.y, game.height)
    global gravity, monster1, monster2
    if collide(jumper, spike) or collide(jumper, spike2):
        delay(0.1)
        game.reset = True
        framework.push_state(level_7)
        if game.checkpoint:
            framework.push_state(level_7)
            jumper.x = flag.x
            jumper.y = flag.y + 1
            jumper.state = Jumper.STANDRIGHTDOWN
            game.gravity = True
            game.height = 130
            jumper.y = 259

    if collide(jumper, monster_1):
        monster1 = False
        game.seta = -90
        jumper.y -= 15
        if jumper.state == Jumper.RUNRIGHTDOWN or jumper.state == Jumper.STANDRIGHTDOWN:
            jumper.state = Jumper.STANDRIGHTDOWN
            game.jumping = 1
            jumper.state = Jumper.JUMPRIGHTDOWN

        if jumper.state == Jumper.RUNLEFTDOWN or jumper.state == Jumper.STANDLEFTDOWN:
            jumper.state = Jumper.STANDLEFTDOWN
            game.jumping = 1
            jumper.state = Jumper.JUMPLEFTDOWN

    if collide(jumper, monster_2):
        monster2 = False
        game.seta = -90
        jumper.y -= 15
        if jumper.state == Jumper.RUNRIGHTDOWN or jumper.state == Jumper.STANDRIGHTDOWN:
            jumper.state = Jumper.STANDRIGHTDOWN
            game.jumping = 1
            jumper.state = Jumper.JUMPRIGHTDOWN

        if jumper.state == Jumper.RUNLEFTDOWN or jumper.state == Jumper.STANDRIGHTDOWN:
            jumper.state = Jumper.STANDLEFTDOWN
            game.jumping = 1
            jumper.state = Jumper.JUMPLEFTDOWN

    if collide_1(jumper, gravity):
        if mg_1.frame < 6:
            mg_1.frame += 1
            mg_2.frame += 1
        mg_1.frame2 = 0
        mg_2.frame2 = 0
        game.gravity = True
        jumper.state = Jumper.CHANGEUP
        game.temp = 1
        game.move = 0
        game.change_motion = True

    if collide_2(jumper, gravity):
        mg_1.frame = 0
        mg_2.frame = 0
        if mg_1.frame2 < 6:
            mg_1.frame2 += 1
            mg_2.frame2 += 1
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

    if jumper.x >= flag.x - 20:
        if jumper.x <= flag.x + 20:
            if jumper.y == flag.y - 3:
                game.checkpoint = True


# -----------------------------------------------------------------------------------

def change_level(frame_time):
    if game.reset:
        blink.draw(game.back_x, game.back_y)
        game.temp += 1

    if game.temp > 2:
        game.reset = False

    if jumper.x <= game.min_x:
        framework.push_state(level_6)

    if jumper.x >= game.max_x:
        framework.push_state(level_8)


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

# -----------------------------------------------------------------------------------


