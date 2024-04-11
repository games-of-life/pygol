from collections import Counter
from itertools import chain, product
from random import randint

from abstract_grid import AbstractGrid, CellState


class SetGrid(AbstractGrid):
    def __init__(self, width: int, height: int, prob: float):
        super().__init__(width, height)
        self._field = {
            (randint(0, width), randint(0, height))
            for _ in range(int(width * height * prob))
        }

    def get_elem(self, i: int, j: int) -> CellState:
        return CellState.ALIVE if (i, j) in self._field else CellState.DEAD

    def set_elem(self, i: int, j: int, val: CellState) -> None:
        match val:
            case CellState.ALIVE:
                self._field.add((i, j))
            case CellState.DEAD:
                self._field.remove((i, j))

    def _moore_neighborhood(self, i: int, j: int) -> map:
        offsets = product([-1, 0, 1], [-1, 0, 1])

        filtered_offsets = filter(lambda t: not (t[0] == 0 and t[1] == 0), offsets)

        return map(lambda x: (x[0] + i, x[1] + j), filtered_offsets)

    def run_gol_step(self) -> None:
        valuable_points = chain.from_iterable(
            map(lambda x: self._moore_neighborhood(x[0], x[1]), self._field)
        )

        in_bound_points = filter(
            lambda cur: not (
                cur[0] < 0
                or cur[1] < 0
                or cur[0] >= self.width
                or cur[1] >= self.height
            ),
            valuable_points,
        )

        frequencies = Counter(in_bound_points)

        points_to_keep = filter(
            lambda cur: 3 == cur[1]
            or (2 == cur[1] and CellState.ALIVE == self.get_elem(cur[0][0], cur[0][1])),
            frequencies.items(),
        )

        new_set = set({c[0] for c in points_to_keep})

        self._field = new_set
