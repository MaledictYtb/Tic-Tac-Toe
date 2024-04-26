from kandinsky import *
from ion import KEY_LEFT, KEY_DOWN, KEY_UP, KEY_RIGHT, keydown
from time import sleep


def draw_map():
    fill_rect(0, 0, 320, 222, color(255, 255, 255))
    #Draw the grid
    fill_rect(107, 0, 1, 222, color(0, 0, 0))
    fill_rect(214, 0, 1, 222, color(0, 0, 0))
    fill_rect(0, 73, 320, 1, color(0, 0, 0))
    fill_rect(0, 148, 320, 1, color(0, 0, 0))

    #Draw X and O from map
    abs_coords = [54, 161, 268]
    ord_coords = [37, 110, 185]
    for i in range(3):
        for j in range(3):
            if map[i][j]:  # check if the element is not None
                draw_string(map[i][j], abs_coords[j]-5, ord_coords[i]-5, color(255, 0, 0))


def draw_cursor(ordonne, abscisse):
    draw_map()
    abs_coords = [54, 161, 268]
    ord_coors = [37, 110, 185]

    fill_rect(abs_coords[abscisse] - 5, ord_coors[ordonne] - 5, 10, 10, color(255, 0, 0))

cursor_position = (1, 1)
map =  [[None, None, None],
        [None, None, None],
        [None, None, None]]


draw_map()
draw_cursor(1, 1)

while True :
    if keydown(KEY_UP):
        if cursor_position[0] == 0:
            break
        cursor_position = (cursor_position[0] - 1 , cursor_position[1])
        draw_cursor(cursor_position[0], cursor_position[1])

    elif keydown(KEY_DOWN):
        if cursor_position[0] == 2:
            break
        cursor_position = (cursor_position[0] + 1 , cursor_position[1])
        draw_cursor(cursor_position[0], cursor_position[1])

    elif keydown(KEY_LEFT):
        if cursor_position[1] == 0:
            break
        cursor_position = (cursor_position[0], cursor_position[1] - 1)
        draw_cursor(cursor_position[0], cursor_position[1])

    elif keydown(KEY_RIGHT):
        if cursor_position[1] == 2:
            break
        cursor_position = (cursor_position[0], cursor_position[1] + 1 )
        draw_cursor(cursor_position[0], cursor_position[1])
    sleep(0.1)