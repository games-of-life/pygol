from random import random

from abstract_grid import AbstractGrid, CellState


class VectorGrid(AbstractGrid):
    def __init__(self, width: int, height: int, prob: float):
        super().__init__(width, height)
        self._field = [
            CellState.DEAD if random() > prob else CellState.ALIVE
            for _ in range(width * height)
        ]

    def get_elem(self, i: int, j: int) -> CellState:
        return self._field[i * self.height + j]

    def set_elem(self, i: int, j: int, val: CellState) -> None:
        self._field[i * self.height + j] = val

    def _calc_neighbors(self, i: int, j: int) -> int:
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                n_x = i + dx
                n_y = j + dy
                if not (
                    (dx == 0 and dy == 0)
                    or (n_x < 0 or n_y < 0)
                    or (n_x >= self.width or n_y >= self.height)
                ) and CellState.ALIVE == self.get_elem(n_x, n_y):
                    count += 1
        return count

    def run_gol_step(self) -> None:
        field_copy = self._field.copy()
        for i in range(self.width):
            for j in range(self.height):
                neigh = self._calc_neighbors(i, j)

                if 3 == neigh or (
                    2 == neigh and CellState.ALIVE == self.get_elem(i, j)
                ):
                    field_copy[i * self.height + j] = CellState.ALIVE
                else:
                    field_copy[i * self.height + j] = CellState.DEAD
        self._field = field_copy
