class Board:
    def __init(self):
        self.cells = [[None for _ in range(3)] for _ in range(3)]
        self.active_cell = (0, 0)


    def reset_board(self) -> None:
        self.cells = [[None for _ in range(3)] for _ in range(3)]
        self.active_cell = (0, 0)


    def _cell_in_corner(self, y, x) -> bool:
        return y == 0 and x == 0 or y == 2 and x == 0 or y == 0 and x == 2 or y == 2 and x == 2


    def _cell_in_center(self, y, x) -> bool:
        return y == 1 and x == 1


    def _cell_in_edge(self, y, x) -> bool:
        return y == 0 or y == 2 or x == 0 or x == 2


    def cell_lines(self, y, x) -> list:
        diagonal_cells = [[(0, 0), (1, 1), (2, 2)],[(2, 0), (1, 1), (0, 2)]]
        cell_lines = []
        cell_lines.extend(
            [
                [(y, 0), (y, 1), (y, 2)],
                [(0, x), (1, x), (2, x)],

            ]
        )
        if self._cell_in_corner(y, x):
            for line in diagonal_cells:
                if (y, x) in line:
                    cell_lines.append(line)
                    break

        elif self._cell_in_center(y, x):
            cell_lines.extend(diagonal_cells)
        return cell_lines


    def first_empty_cell(self):
        for y, row in enumerate(self.cells):
            for x, cell in enumerate(row):
                if cell is None:
                    return (y, x)
        return None

    def get_empty_cells(self) -> list:
        empty_cells = []
        for y, row in enumerate(self.cells):
            for x, cell in enumerate(row):
                if cell is None:
                    empty_cells.append((y, x))
        return empty_cells

    def get_filled_cells(self) -> list:
        filled_cells = []
        for y, row in enumerate(self.cells):
            for x, cell in enumerate(row):
                if cell is not None:
                    filled_cells.append((y, x))
        return filled_cells


    def move_active_cell(self, direction: str) -> None:
        if direction == "up":
            self.active_cell = (max(self.active_cell[0] - 1, 0), self.active_cell[1])
        elif direction == "down":
            self.active_cell = (min(self.active_cell[0] + 1, len(self.cells) - 1), self.active_cell[1])
        elif direction == "left":
            self.active_cell = (self.active_cell[0], max(self.active_cell[1] - 1, 0))
        elif direction == "right":
            self.active_cell = (self.active_cell[0], min(self.active_cell[1] + 1, len(self.cells[0]) - 1))
