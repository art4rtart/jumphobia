# -----------------------------------------------------------------------------------
from pico2d import *
from math import *
import gameMain
# -----------------------------------------------------------------------------------
name = "Jumper"
# -----------------------------------------------------------------------------------

tempy = 157
seta = 90

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

    def __init__(self):
        self.standright = load_image("standRight.png")
        self.standleft = load_image("standLeft.png")

        self.runright = load_image("runRight.png")
        self.runleft = load_image("runLeft.png")

        self.jumpright = load_image("jumpRight.png")
        self.jumpleft = load_image("jumpLeft.png")

        self.x, self.y = 50, 157
        self.state = Jumper.STANDRIGHT

        self.total_frames = 0
        self.frame = 0

        self.dir = 1


    def update(self, frame_time):
        global seta

        distance = Jumper.RUN_SPEED_PPS * frame_time

        self.total_frames += 1.0
        self.frame = (self.frame + 1) % 8

        self.total_frames += Jumper.FRAMES_PER_ACTION * Jumper.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8

        if self.state == Jumper.STANDRIGHT or self.state == Jumper.STANDLEFT:
            pass

        if self.state == Jumper.RUNRIGHT:
            self.x += distance

        if self.state == Jumper.RUNLEFT:
            self.x -= distance

        if self.state == Jumper.JUMPRIGHT:
            self.x += 8 * cos(seta * (3.14 / 180))
            self.y += 15 * sin(seta * (3.14 / 180))

            if seta >= -90:
                seta -= 10

            if seta <= -90:
                self.state = Jumper.STANDRIGHT
                seta = 90
                self.y = tempy
                gameMain.jumping = 0

        if self.state == Jumper.JUMPLEFT:
            self.x += 8 * cos(seta * (3.14 / 180))
            self.y += 15 * sin(seta * (3.14 / 180))

            if seta <= 270:
                seta += 10

            if seta >= 270:
                self.state = Jumper.STANDLEFT
                seta = 90
                self.y = tempy
                gameMain.jumping = 0

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



