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


class Brick:
    def __init__(self):
        self.x_1, self.y_1 = 750, 200
        self.x_2, self.y_2 = 600, 250
        self.x_3, self.y_3 = 450, 300
        self.dir_1, self.dir_2, self.dir_3 = 1, 1, 1
        self.move_1, self.move_2, self.move_3 = 1, 1, 1
        self.brick_1 = load_image('brick.png')
        self.brick_2 = load_image('brick.png')
        self.brick_3 = load_image('brick.png')

    def update(self, frame_time):
        self.move_1 = 2 * self.dir_1
        self.move_2 = 2 * self.dir_2
        self.move_3 = 2 * self.dir_3

        self.x_1 -= self.move_1
        self.x_2 -= self.move_2
        self.x_3 -= self.move_3

        if self.x_1 >= 750:
            self.dir_1 *= -1

        elif self.x_1 <= 650:
            self.dir_1 *= -1

        if self.x_2 >= 650:
            self.dir_2 *= -1

        elif self.x_2 <= 550:
            self.dir_2 *= -1

        if self.x_3 >= 450:
            self.dir_3 *= -1

        elif self.x_3 <= 350:
            self.dir_3 *= -1

    def draw(self):
        self.brick_1.draw(self.x_1, self.y_1)
        self.brick_2.draw(self.x_2, self.y_2)
        self.brick_3.draw(self.x_3, self.y_3)

    def draw_bb_1(self):
        draw_rectangle(*self.get_bb_1())

    def draw_bb_2(self):
        draw_rectangle(*self.get_bb_2())

    def draw_bb_3(self):
        draw_rectangle(*self.get_bb_3())

    def get_bb_1(self):
        return self.x_1 - 50, self.y_1 - 10, self.x_1 + 50, self.y_1 + 10

    def get_bb_2(self):
        return self.x_2 - 50, self.y_2 - 10, self.x_2 + 50, self.y_2 + 10

    def get_bb_3(self):
        return self.x_3 - 50, self.y_3 - 10, self.x_3 + 50, self.y_3 + 10
