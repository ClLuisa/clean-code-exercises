# The `RasterGrid` represents a structured, rectangular grid in 2d space.
# Each cell of the grid is identified by its column/row index pair:
#
#  ________ ________ ________
# |        |        |        |
# | (0, 1) | (1, 1) | (2, 2) |
# |________|________|________|
# |        |        |        |
# | (0, 0) | (1, 0) | (2, 0) |
# |________|________|________|
#
#
# One can construct a `RasterGrid` by specifying the lower left and upper right
# corners of a domain and the number of cells one wants to use in x- and y-directions.
# Then, `RasterGrid` allows to iterate over all cells and retrieve the center point
# of that cell.
#
# This class can be significantly cleaned up, though. Give it a try, and if you need
# help you may look into the file `raster_grid_hints.py`.
# Make sure to make small changes, verifying that the test still passes, and put
# each small change into a separate commit.
from typing import Tuple
from math import isclose
from dataclasses import dataclass


class RasterGrid:
    @dataclass
    class Cell:
        ix: int
        iy: int

    @dataclass
    class Point:
        x: float
        y: float

    def __init__(self,
                 lower_left_point: Point,
                 upper_right_point: Point,
                 nx: int,
                 ny: int) -> None:
        self._x0 = lower_left_point.x
        self._y0 = lower_left_point.y
        self._x1 = upper_right_point.x
        self._y1 = upper_right_point.y
        self._nx = nx
        self._ny = ny
        self._dx = (self._x1 - self._x0) / self._nx
        self._dy = (self._y1 - self._y0) / self._ny
    
    @property
    def number_of_cells(self) -> int:
        return self._nx*self._ny

    @property
    def cells(self):
        return [self.Cell(i, j) for i in range(self._nx) for j in range(self._ny)]

    def get_center(self, cell: Cell) -> Point:
        return self.Point(
            self._x0 + (cell.ix + 0.5)*self._dx,
            self._y0 + (cell.iy + 0.5)*self._dy
        )

def test_number_of_cells():
    p0 = RasterGrid.Point(0.0, 0.0)
    p1 = RasterGrid.Point(10.0, 10.0)
    assert RasterGrid(p0, p1, 10, 10).number_of_cells == 100
    assert RasterGrid(p0, p1, 10, 20).number_of_cells == 200
    assert RasterGrid(p0, p1, 20, 10).number_of_cells == 200
    assert RasterGrid(p0, p1, 20, 20).number_of_cells == 400


def test_cell_center():
    grid = RasterGrid(RasterGrid.Point(0.0, 0.0), RasterGrid.Point(2.0, 2.0), 2, 2)
    expected_centers = [
        RasterGrid.Point(0.5, 0.5),
        RasterGrid.Point(1.5, 0.5),
        RasterGrid.Point(0.5, 1.5),
        RasterGrid.Point(1.5, 1.5)
    ]

    for cell in grid.cells:
        for center in expected_centers:
            if isclose(grid.get_center(cell).x, center.x) and isclose(grid.get_center(cell).y, center.y):
                expected_centers.remove(center)

    assert len(expected_centers) == 0


if __name__ == "__main__":
    test_number_of_cells()
    test_cell_center()
    print("All tests passed")
