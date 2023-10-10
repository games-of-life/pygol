from abc import ABC, abstractmethod
from enum import Enum


class CellState(Enum):
    DEAD = 0
    ALIVE = 1


class AbstractGrid(ABC):
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @abstractmethod
    def get_elem(self, i: int, j: int) -> CellState:
        pass

    @abstractmethod
    def set_elem(self, i: int, j: int, val: CellState) -> None:
        pass

    @abstractmethod
    def run_gol_step(self) -> None:
        pass
