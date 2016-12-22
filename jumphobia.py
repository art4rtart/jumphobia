# -----------------------------------------------------------------------------------
from pico2d import *
import framework

# -----------------------------------------------------------------------------------
name = "Jumphobia"
# -----------------------------------------------------------------------------------


def create_world():
    pass


def enter():
    framework.reset_time()


def exit():
    pass


def pause():
    pass


def resume():
    pass


# -----------------------------------------------------------------------------------

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()


def update(frame_time):
    update_canvas()


def draw(frame_time):
    pass

# -----------------------------------------------------------------------------------



