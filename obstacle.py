# -----------------------------------------------------------------------------------
from pico2d import *
import game
# -----------------------------------------------------------------------------------
name = "Obstacle"
# -----------------------------------------------------------------------------------


class Spike:
    def __init__(self):
        self.x, self.y = 520, 80

    def update(self, frame_time):
        pass

    def draw(self):
        pass

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 300, self.y - 10, self.x + 300, self.y + 10






