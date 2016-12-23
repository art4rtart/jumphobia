from pico2d import *
import framework
import gameMain

name = "gameTitle"

back = None

def enter():
    pass


def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global select_status
    global game_mode

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()


def update(frame_time):
    framework.push_state(gameMain)
    update_canvas()


def draw(frame_time):
    update_canvas()



