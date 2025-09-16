from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90

MoveType = True
angle = 360
r = 235
cx = 405
cy = 325
angle_step = 5

def Move():
    global x, y, MoveType, angle

    if MoveType:
        if y == 90 and x < 784:
            x = x + 2
        elif x >= 784 and y < 560:
            y = y + 2
        elif y >= 560 and x > 16:
            x = x - 2
        elif x <= 16 and y > 90:
            y = y - 2

        if x == 400 and y == 90:
            MoveType = False
            angle = 360

    else:
        if angle <= 90:
            MoveType = True
            x, y = 400, 90
            angle = 360
        else:
            radian = math.radians(angle)
            x = int(cx + r * math.cos(radian))
            y = int(cy + r * math.sin(radian))
            angle = angle - angle_step

while True:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)

    Move()
    delay(0.01)
