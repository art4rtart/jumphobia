from pico2d import *
import framework
import gameTitle
import level_1

name = "TitleState"
kpu = None


def enter():
    open_canvas(1000, 500, sync=True)
    framework.push_state(level_1)
    global kpu
    kpu = load_image("kpu.png")


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



def update(frame_time):
    pass


def draw(frame_time):
    clear_canvas()

    kpu.draw(400, 300)

    update_canvas()



