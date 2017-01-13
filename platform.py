# -----------------------------------------------------------------------------------
from pico2d import *
import game
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
        self.x_1, self.y_1 = 750, 160
        self.x_2, self.y_2 = 600, 220
        self.x_3, self.y_3 = 350, 280
        self.dir_1, self.dir_2, self.dir_3 = 1, 1, 1
        self.move_1, self.move_2, self.move_3 = 1, 1, 1
        self.brick_1 = load_image('brick.png')
        self.brick_2 = load_image('brick.png')
        self.brick_3 = load_image('brick.png')

    def update(self, frame_time):
        self.move_1 = 2 * self.dir_1
        self.move_2 = 3 * self.dir_2
        self.move_3 = 4 * self.dir_3

        self.x_1 -= self.move_1
        self.x_2 -= self.move_2
        self.x_3 -= self.move_3

        if self.x_1 >= 750:
            self.dir_1 *= -1

        elif self.x_1 <= 650:
            self.dir_1 *= -1

        if self.x_2 >= 600:
            self.dir_2 *= -1

        elif self.x_2 <= 450:
            self.dir_2 *= -1

        if self.x_3 >= 350:
            self.dir_3 *= -1

        elif self.x_3 <= 250:
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


class Triangle:
    def __init__(self):
        self.x_1, self.y_1 = 595, 255
        self.x_2, self.y_2 = 560, 255
        self.x_3, self.y_3 = 525, 255
        self.x_4, self.y_4 = 490, 255
        self.x_5, self.y_5 = 455, 255

        self.image_1 = load_image('triangle.png')
        self.image_2 = load_image('triangle.png')
        self.image_3 = load_image('triangle.png')
        self.image_4 = load_image('triangle.png')

        self.opacify_1, self.opacify_2, self.opacify_3, self.opacify_4 = 1, 1, 1, 1

    def update(self, frame_time):
        if game.t1:
            if self.opacify_1 > 0:
                self.opacify_1 -= 0.05

        if game.t2:
            if self.opacify_2 > 0:
                self.opacify_2 -= 0.05

        if game.t3:
            if self.opacify_3 > 0:
                self.opacify_3 -= 0.05

        if game.t4:
            if self.opacify_4 > 0:
                self.opacify_4 -= 0.05

    def draw(self):
        self.image_1.draw(self.x_1, self.y_1)
        self.image_2.draw(self.x_2, self.y_2)
        self.image_3.draw(self.x_3, self.y_3)
        self.image_4.draw(self.x_4, self.y_4)
        self.image_1.opacify(self.opacify_1)
        self.image_2.opacify(self.opacify_2)
        self.image_3.opacify(self.opacify_3)
        self.image_4.opacify(self.opacify_4)

    def draw_bb_1(self):
        draw_rectangle(*self.get_bb_1())

    def draw_bb_2(self):
        draw_rectangle(*self.get_bb_2())

    def draw_bb_3(self):
        draw_rectangle(*self.get_bb_3())

    def draw_bb_4(self):
        draw_rectangle(*self.get_bb_4())

    def get_bb_1(self):
        return self.x_1 - 19, self.y_1 + 18, self.x_1 + 17, self.y_1 + 20

    def get_bb_2(self):
        return self.x_2 - 19, self.y_2 + 18, self.x_2 + 17, self.y_2 + 20

    def get_bb_3(self):
        return self.x_3 - 19, self.y_3 + 18, self.x_3 + 17, self.y_3 + 20

    def get_bb_4(self):
        return self.x_4 - 19, self.y_4 + 18, self.x_4 + 17, self.y_4 + 20


class Jump:
    def __init__(self):
        self.x_1, self.y_1 = 445, 250
        self.x_2, self.y_2 = 445, 300
        self.x_3, self.y_3 = 445, 350

        self.image = load_image("jumping.png")
        self.frame = 0
        self.temp = 0

    def update(self, frame_time):
        self.temp += 1

        if self.temp % 2 == 0:
            self.frame = (self.frame + 1) % 3

    def draw(self):
        self.image.clip_draw(self.frame * 55, 0, 55, 55, self.x_1, self.y_1)
        self.image.clip_draw(self.frame * 55, 0, 55, 55, self.x_2, self.y_2)
        self.image.clip_draw(self.frame * 55, 0, 55, 55, self.x_3, self.y_3)

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

