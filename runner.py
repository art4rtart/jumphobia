# -----------------------------------------------------------------------------------
from pico2d import *
# -----------------------------------------------------------------------------------
name = "Runner"
# -----------------------------------------------------------------------------------


class Runner:
    PIXEL_PER_METER = (5.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.04
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    STANDRIGHT, STANDLEFT, RUNRIGHT, RUNLEFT = 0, 1, 2, 3

    def __init__(self):
        self.standright = load_image("standRight.png")
        self.standleft = load_image("standLeft.png")
        self.runright = load_image("runRight.png")
        self.runleft = load_image("runLeft.png")

        self.x, self.y = 400, 200
        self.state = Runner.STANDRIGHT

        self.total_frames = 0
        self.frame = 0

    def update(self, frame_time):
        distance = Runner.RUN_SPEED_PPS * frame_time

        self.total_frames += 1.0
        self.frame = (self.frame + 1) % 8

        self.total_frames += Runner.FRAMES_PER_ACTION * Runner.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8

        if self.state == Runner.STANDRIGHT or self.state == Runner.STANDLEFT:
            pass

        if self.state == Runner.RUNRIGHT:
            self.x += distance

        if self.state == Runner.RUNLEFT:
            self.x -= distance

    def draw(self):
        if self.state == Runner.STANDRIGHT:
            self.standright.draw(self.x, self.y)

        if self.state == Runner.STANDLEFT:
            self.standleft.draw(self.x, self.y)

        if self.state == Runner.RUNRIGHT:
            self.runright.clip_draw(self.frame * 56, 0, 56, 54, self.x, self.y)

        if self.state == Runner.RUNLEFT:
            self.runleft.clip_draw(self.frame * 56, 0, 56, 54, self.x, self.y)



