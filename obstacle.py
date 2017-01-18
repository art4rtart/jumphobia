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
        self.red = load_image('resource/image/objects/red.png')
        self.green = load_image('resource/image/objects/green.png')
        self.redup = load_image('resource/image/objects/redUp.png')
        self.greenup = load_image('resource/image/objects/greenUp.png')

    def update(self, frame_time):
        pass

    def draw(self):
        if game.gravity_stage:
            if game.checkpoint:
                self.greenup.draw(self.x, self.y)
            else:
                self.redup.draw(self.x + 22, self.y)

        else:
            if game.checkpoint:
                self.green.draw(self.x, self.y)
            else:
                self.red.draw(self.x - 22, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20


class Saw:
    def __init__(self):
        self.x_1, self.y_1 = 445, 190
        self.x_2, self.y_2 = 445, 240
        self.x_3, self.y_3 = 445, 290
        self.x_4, self.y_4 = 640, 190
        self.x_5, self.y_5 = 640, 240
        self.x_6, self.y_6 = 640, 290
        self.x_7, self.y_7 = 835, 190
        self.x_8, self.y_8 = 835, 240
        self.x_9, self.y_9 = 835, 290
        self.x_10, self.y_10 = 445, 410
        self.x_11, self.y_11 = 640, 410
        self.x_12, self.y_12 = 835, 410

        self.image = load_image("resource/image/objects/saw.png")
        self.frame = 0
        self.temp = 0

        self.dir = 1

    def update(self, frame_time):
        self.temp += 1
        self.y_10 -= 2 * self.dir
        self.y_11 += 2 * self.dir
        self.y_12 -= 2 * self.dir

        if self.temp % 2 == 0:
            self.frame = (self.frame + 1) % 6

        if self.y_10 > 455:
            self.dir *= -1

        elif self.y_10 < 365:
            self.dir *= -1

    def draw(self):
        self.image.clip_draw(self.frame * 45, 0, 45, 45, self.x_1, self.y_1)
        self.image.clip_draw(self.frame * 45, 0, 45, 45, self.x_2, self.y_2)
        self.image.clip_draw(self.frame * 45, 0, 45, 45, self.x_3, self.y_3)
        self.image.clip_draw(self.frame * 45, 0, 45, 45, self.x_4, self.y_4)
        self.image.clip_draw(self.frame * 45, 0, 45, 45, self.x_5, self.y_5)
        self.image.clip_draw(self.frame * 45, 0, 45, 45, self.x_6, self.y_6)
        self.image.clip_draw(self.frame * 45, 0, 45, 45, self.x_7, self.y_7)
        self.image.clip_draw(self.frame * 45, 0, 45, 45, self.x_8, self.y_8)
        self.image.clip_draw(self.frame * 45, 0, 45, 45, self.x_9, self.y_9)
        self.image.clip_draw(self.frame * 45, 0, 45, 45, self.x_10, self.y_10)
        self.image.clip_draw(self.frame * 45, 0, 45, 45, self.x_11, self.y_11)
        self.image.clip_draw(self.frame * 45, 0, 45, 45, self.x_12, self.y_12)

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

    def draw_bb_4(self):
        draw_rectangle(*self.get_bb_4())

    def get_bb_4(self):
        return self.x_10 - 20, self.y_10 - 20, self.x_10 + 20, self.y_10 + 20

    def draw_bb_5(self):
        draw_rectangle(*self.get_bb_5())

    def get_bb_5(self):
        return self.x_11 - 20, self.y_11 - 20, self.x_11 + 20, self.y_11 + 20

    def draw_bb_6(self):
        draw_rectangle(*self.get_bb_6())

    def get_bb_6(self):
        return self.x_12 - 20, self.y_12 - 20, self.x_12 + 20, self.y_12 + 20


class Monster:
    def __init__(self):
        self.x, self.y = 0, 0
        self.dir = 1
        self.image = load_image("resource/image/objects/monster.png")
        self.opacify = 1

    def update(self, frame_time):
        self.x += 2 * self.dir

        if self.x < 100:
            self.dir *= -1

        if self.x > 250:
            self.dir *= -1

        if game.monster is False:
            if self.opacify > 0:
                self.opacify -= 0.05

    def draw(self):
        self.image.draw(self.x, self.y)
        self.image.opacify(self.opacify)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15


class MonsterGravity:
    def __init__(self):
        self.x, self.y = 0, 0
        self.init = load_image('resource/image/objects/monster.png')
        self.up = load_image('resource/image/objects/monsterUp.png')
        self.down = load_image('resource/image/objects/monsterDown.png')
        self.frame = 0
        self.frame2 = 0
        self.count = 0

    def update(self, frame_time):
        pass

    def draw(self):
        if game.gravity is True:
            self.up.clip_draw(self.frame * 36, 0, 36, 37, self.x, self.y)
            self.count += 1

        else:
            if self.count == 0:
                self.init.draw(self.x + 4, self.y)
            else:
                self.down.clip_draw(self.frame2 * 37, 0, 37, 37, self.x + 1, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15



