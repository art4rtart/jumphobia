# -----------------------------------------------------------------------------------
from pico2d import *
import framework
# -----------------------------------------------------------------------------------
name = "Runner"
# -----------------------------------------------------------------------------------


class Runner:
    def __init__(self):
        self.x, self.y = 400, 200
        self.state = 0

        self.right = load_image("runRight.png")
        self.left = load_image("runLeft.png")

        self.right_frame = 0
        self.left_frame = 0

    def update(self, frame_time):
        if self.state == 1:
            self.x += 1
            if self.right_frame < 6:
                self.right_frame += 1

            if self.right_frame > 5:
                self.right_frame = 0

        if self.state == 2:
            self.x -= 1
            if self.left_frame < 6:
                self.left_frame += 1

            if self.left_frame > 5:
                self.left_frame = 0

        if self.state == 0:
            pass

    def draw(self):
        print(self.right_frame)
        if self.state == 0:
            self.right.clip_draw(self.right_frame * 55, 0, 55, 75, self.x, self.y)

        if self.state == 1:
            self.right.clip_draw(self.right_frame * 55, 0, 55, 75, self.x, self.y)

        if self.state == 2:
            self.left.clip_draw(self.left_frame * 55, 0, 55, 75, self.x, self.y)

