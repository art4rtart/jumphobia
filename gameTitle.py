from pico2d import *
import framework
import gameMain

name = "TitleState"
title = None


def enter():
    global title
    title = load_image("title.png")


def exit():
    global image
    image = None
    del(image)


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                framework.quit()
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                framework.push_state(gameMain)


def update(frame_time):
    pass


def draw(frame_time):
    clear_canvas()

    title.draw(400, 300)

    update_canvas()



