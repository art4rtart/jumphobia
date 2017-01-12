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


class Saw:
    def __init__(self):
        self.x_1, self.y_1 = 445, 250
        self.x_2, self.y_2 = 445, 300
        self.x_3, self.y_3 = 445, 350
        self.x_4, self.y_4 = 640, 250
        self.x_5, self.y_5 = 640, 300
        self.x_6, self.y_6 = 640, 350
        self.x_7, self.y_7 = 835, 250
        self.x_8, self.y_8 = 835, 300
        self.x_9, self.y_9 = 835, 350

        self.image = load_image("saw.png")
        self.frame = 0
        self.temp = 0

    def update(self, frame_time):
        self.temp += 1

        if self.temp % 2 == 0:
            self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 55, 0, 55, 55, self.x_1, self.y_1)
        self.image.clip_draw(self.frame * 55, 0, 55, 55, self.x_2, self.y_2)
        self.image.clip_draw(self.frame * 55, 0, 55, 55, self.x_3, self.y_3)
        self.image.clip_draw(self.frame * 55, 0, 55, 55, self.x_4, self.y_4)
        self.image.clip_draw(self.frame * 55, 0, 55, 55, self.x_5, self.y_5)
        self.image.clip_draw(self.frame * 55, 0, 55, 55, self.x_6, self.y_6)
        self.image.clip_draw(self.frame * 55, 0, 55, 55, self.x_7, self.y_7)
        self.image.clip_draw(self.frame * 55, 0, 55, 55, self.x_8, self.y_8)
        self.image.clip_draw(self.frame * 55, 0, 55, 55, self.x_9, self.y_9)

    def draw_bb_1(self):
        draw_rectangle(*self.get_bb_1())

    def get_bb_1(self):
        return self.x_1 - 20, self.y_1 - 20, self.x_3 + 20, self.y_3 + 20

    def draw_bb_2(self):
        draw_rectangle(*self.get_bb_2())

    def get_bb_2(self):
        return self.x_4 - 20, self.y_4 - 20, self.x_6 + 20, self.y_6 + 20

    def draw_bb_3(self):
        draw_rectangle(*self.get_bb_3())

    def get_bb_3(self):
        return self.x_7 - 20, self.y_7 - 20, self.x_9 + 20, self.y_9 + 20



