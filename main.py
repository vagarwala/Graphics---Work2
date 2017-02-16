from display import *
from draw import *

screen = new_screen()

x = 0

while (x <= 5000):
    draw_line(0, 500 - x, x, 0, screen, [0, 0, 0] )
    draw_line(500, x, 500 - x, 500, screen, [0, 100, 0])
    draw_line(x, 0, 500, x, screen, [100, 0, 0])
    draw_line(0, x, x, 500, screen, [0, 0, 100])
    x += 10