# -----------------------------------------------------------------------------------
from pico2d import *
import game
# -----------------------------------------------------------------------------------
name = "OBSTACLE"
# -----------------------------------------------------------------------------------


class Spike:
    def __init__(self):
        self.x, self.y = 0, 0
        self.box_x, self.box_y = 0, 0

    def update(self, frame_time):
        pass

    def draw(self):
        pass

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - self.box_x, self.y - self.box_y, self.x + self.box_x, self.y + self.box_y


class Spike2:
    def __init__(self):
        self.x, self.y = 0, 0
        self.box_x, self.box_y = 0, 0

    def update(self, frame_time):
        pass

    def draw(self):
        pass

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - self.box_x, self.y - self.box_y, self.x + self.box_x, self.y + self.box_y


class Flag:
    def __init__(self):
        self.x, self.y = 0, 0
        self.red = load_image('red.png')
        self.green = load_image('green.png')

    def update(self, frame_time):
        pass

    def draw(self):
        if game.checkpoint:
            self.green.draw(self.x, self.y)
        else:
            self.red.draw(self.x - 22, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20


class Monster:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image("monster.png")

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15






