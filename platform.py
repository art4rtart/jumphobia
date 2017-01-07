# -----------------------------------------------------------------------------------
from pico2d import *
# import game
# -----------------------------------------------------------------------------------
name = "PLATFORM"
# -----------------------------------------------------------------------------------


class P1:
    def __init__(self):
        self.x, self.y = 420, 270
        self.image = load_image('p1.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 115, self.y - 3, self.x + 113, self.y + 3


class P2:
    def __init__(self):
        self.x, self.y = 270, 210
        self.image = load_image('p2.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 92, self.y - 3, self.x + 90, self.y + 3


class P3:
    def __init__(self):
        self.x, self.y = 600, 180
        self.image = load_image('p3.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 68, self.y - 3, self.x + 68, self.y + 3


class P4:
    def __init__(self):
        self.x, self.y = 680, 330
        self.image = load_image('p4.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 43, self.y - 3, self.x + 41, self.y + 3


class P5:
    def __init__(self):
        self.x, self.y = 500, 200
        self.image = load_image('p5.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 3, self.x + 20, self.y + 3
