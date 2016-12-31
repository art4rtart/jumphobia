# -----------------------------------------------------------------------------------
from pico2d import *
import game
# -----------------------------------------------------------------------------------
name = "Obstacle"
# -----------------------------------------------------------------------------------


class Spike:
    def __init__(self):
        self.x, self.y = 0, 0

    def update(self, frame_time):
        pass

    def draw(self):
        pass

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 300, self.y - 10, self.x + 300, self.y + 10


class Flag:
    def __init__(self):
        self.x, self.y = 0, 0
        self.red = load_image('red.png')
        self.green = load_image('green.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.red.draw(self.x, self.y)
        self.green.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20






