import framework
from pico2d import *
import gameTitle

name = "gameCredit"

def enter():
    open_canvas(800, 800, sync=True)

def exit():
    pass

def update(frame_time):
    framework.push_state(gameTitle)
    update_canvas()


def draw(frame_time):
    pass


def handle_events(frame_time): pass


def pause(): pass


def resume(): pass




