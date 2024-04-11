import pyray as pr
from __init__ import CellState, SetGrid, VectorGrid

WIDTH = 800
HEIGHT = 600

BOX_DIMENSION = 10

pr.init_window(WIDTH, HEIGHT, "Game of life")
# pr.set_target_fps(30)

BOX_WIDTH = WIDTH // BOX_DIMENSION
BOX_HEIGHT = HEIGHT // BOX_DIMENSION

grid = SetGrid(BOX_WIDTH, BOX_HEIGHT, 0.5)

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)

    for i in range(BOX_WIDTH):
        for j in range(BOX_HEIGHT):
            pr.draw_rectangle(
                BOX_DIMENSION * i,
                BOX_DIMENSION * j,
                BOX_DIMENSION - 1,
                BOX_DIMENSION - 1,
                pr.WHITE if CellState.ALIVE == grid.get_elem(i, j) else pr.BLACK,
            )
    pr.draw_fps(10, 10)

    pr.end_drawing()

    grid.run_gol_step()

    # break

pr.close_window()
