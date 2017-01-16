# -----------------------------------------------------------------------------------
from pico2d import *
from math import *
import game
# -----------------------------------------------------------------------------------
name = "Jumper"
# -----------------------------------------------------------------------------------


class Jumper:
    PIXEL_PER_METER = (12.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.04
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    STANDRIGHT, STANDLEFT, RUNRIGHT, RUNLEFT, JUMPRIGHT, JUMPLEFT = 0, 1, 2, 3, 4, 5
    STANDLEFTDOWN, STANDRIGHTDOWN, RUNRIGHTDOWN, RUNLEFTDOWN, JUMPRIGHTDOWN, JUMPLEFTDOWN = 6, 7, 8, 9, 10, 11
    CHANGEUP, CHANGEDOWN = 12, 13

    def __init__(self):
        self.standright = load_image("resource/image/jumper/standRight.png")
        self.standleft = load_image("resource/image/jumper/standLeft.png")

        self.runright = load_image("resource/image/jumper/runRight.png")
        self.runleft = load_image("resource/image/jumper/runLeft.png")

        self.jumpright = load_image("resource/image/jumper/jumpRight.png")
        self.jumpleft = load_image("resource/image/jumper/jumpLeft.png")

        self.standrightdown = load_image("resource/image/jumper/standRightDown.png")
        self.standleftdown = load_image("resource/image/jumper/standLeftDown.png")

        self.changeup = load_image("resource/image/jumper/changeUp.png")
        self.changedown = load_image("resource/image/jumper/changeDown.png")

        self.runrightdown = load_image("resource/image/jumper/runRightDown.png")
        self.runleftdown = load_image("resource/image/jumper/runLeftDown.png")

        self.jumprightdown = load_image("resource/image/jumper/jumpRightDown.png")
        self.jumpleftdown = load_image("resource/image/jumper/jumpLeftDown.png")

        self.x, self.y = game.x, game.y
        self.state = Jumper.STANDRIGHT

        self.total_frames = 0
        self.frame = 0
        self.frame2 = 0

        self.life = 0

    def update(self, frame_time):
        distance = Jumper.RUN_SPEED_PPS * frame_time

        self.total_frames += 1.0
        self.frame = (self.frame + 1) % 8

        self.total_frames += Jumper.FRAMES_PER_ACTION * Jumper.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8

        if self.state == Jumper.STANDRIGHT or self.state == Jumper.STANDLEFT:
            pass

        if self.state == Jumper.STANDRIGHTDOWN or self.state == Jumper.STANDLEFTDOWN:
            pass

        if self.state == Jumper.RUNRIGHT or self.state == Jumper.RUNRIGHTDOWN:
            if self.x < game.max_x - game.max_wall:
                self.x += int(distance)

        if self.state == Jumper.RUNLEFT or self.state == Jumper.RUNLEFTDOWN:
            if self.x > game.min_x + game.min_wall:
                self.x -= int(distance)

        if self.state == Jumper.JUMPRIGHT:
            if self.x < game.max_x - game.max_wall - 10:
                self.x += int(game.jump_x * cos(game.seta * (3.14 / 180))) + game.flying

            self.y += int(game.jump_y * sin(game.seta * (3.14 / 180)))

            if game.seta >= -game.gck:
                game.seta -= 10

            if game.seta <= -game.gck:
                self.state = Jumper.STANDRIGHT
                game.seta = 90
                game.jumping = 0
                game.movement = 0
                game.flying = 0
                if self.life == 1:
                    self.y = game.y + game.height

        if self.state == Jumper.JUMPLEFT:
            if self.x > game.min_x + game.min_wall + 10:
                self.x += int(game.jump_x * cos(game.seta * (3.14 / 180))) + game.flying
            self.y += int(game.jump_y * sin(game.seta * (3.14 / 180)))

            if game.seta <= game.gak:
                game.seta += 10

            if game.seta >= game.gak:
                self.state = Jumper.STANDLEFT
                game.seta = 90
                game.jumping = 0
                game.movement = 0
                game.flying = 0

                if self.life == 1:
                    self.y = game.y + game.height

        # ----------------------------------------------------------------------------------------

        if self.state == Jumper.JUMPRIGHTDOWN:
            if self.x < game.max_x - game.max_wall - 10:
                self.x += int(game.jump_x * cos(game.seta * (3.14 / 180))) + game.flying
            self.y += int(game.jump_y * sin(game.seta * (3.14 / 180)))

            if game.seta <= game.gak:
                game.seta += 10

            if game.seta >= game.gak:
                self.state = Jumper.STANDRIGHTDOWN
                game.seta = -90
                game.jumping = 0
                game.movement = 0
                game.flying = 0

                if self.life == 1:
                    self.y = game.y + game.height

        if self.state == Jumper.JUMPLEFTDOWN:
            if self.x > game.min_x + game.min_wall + 10:
                self.x += int(game.jump_x * cos(game.seta * (3.14 / 180))) + game.flying
            self.y += int(game.jump_y * sin(game.seta * (3.14 / 180)))

            if game.seta >= game.gck:
                game.seta -= 10

            if game.seta <= game.gck:
                self.state = Jumper.STANDLEFTDOWN
                game.seta = -90
                game.jumping = 0
                game.movement = 0
                game.flying = 0

                if self.life == 1:
                    self.y = game.y + game.height

        # ----------------------------------------------------------------------------------------------

        if self.x < game.max_x - game.max_wall - 10:
            if game.movement == 1:
                game.flying += 1

        if self.x > game.min_x + game.min_wall + 10:
            if game.movement == 2:
                game.flying -= 1

    def draw(self):
        if self.state == Jumper.STANDRIGHT:
            self.standright.draw(self.x, self.y)

        if self.state == Jumper.STANDLEFT:
            self.standleft.draw(self.x, self.y)

        if self.state == Jumper.JUMPRIGHT:
            self.jumpright.draw(self.x, self.y)

        if self.state == Jumper.JUMPLEFT:
            self.jumpleft.draw(self.x, self.y)

        if self.state == Jumper.RUNRIGHT:
            self.runright.clip_draw(self.frame * 50, 0, 50, 35, self.x, self.y)

        if self.state == Jumper.RUNLEFT:
            self.runleft.clip_draw(self.frame * 50, 0, 50, 35, self.x, self.y)
        # --
        if self.state == Jumper.STANDRIGHTDOWN:
            self.standrightdown.draw(self.x, self.y)

        if self.state == Jumper.STANDLEFTDOWN:
            self.standleftdown.draw(self.x, self.y)

        if self.state == Jumper.JUMPRIGHTDOWN:
            self.jumprightdown.draw(self.x, self.y)

        if self.state == Jumper.JUMPLEFTDOWN:
            self.jumpleftdown.draw(self.x, self.y)

        if self.state == Jumper.RUNRIGHTDOWN:
            self.runrightdown.clip_draw(self.frame * 50, 0, 50, 35, self.x, self.y)

        if self.state == Jumper.RUNLEFTDOWN:
            self.runleftdown.clip_draw(self.frame * 50, 0, 50, 35, self.x, self.y)

        if self.state == Jumper.CHANGEUP:
            self.changeup.clip_draw(self.frame2 * 40, 0, 40, 43, self.x, self.y)

        if self.state == Jumper.CHANGEDOWN:
            self.changedown.clip_draw(self.frame2 * 40, 0, 40, 43, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 20, self.x + 10, self.y + 20






