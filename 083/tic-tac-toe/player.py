import random
from board import Board
from typing import Tuple


class Player:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.score = 0
        self.is_ai = False
        self.difficulty = 2

    def change_difficulty(self, difficulty: int=None) -> None:
        if difficulty is not None and difficulty in range(1, 3):
            self.difficulty = difficulty
        else:
            self.difficulty = self.difficulty + 1 if self.difficulty < 2 else 1
    
    def get_ai_move(self, board: Board) -> Tuple[int, int]:
        if self.difficulty == 1:
            return self._get_ai_move_easy(board)
        else:
            return self._get_ai_move_hard(board)

    def _get_ai_move_easy(self, board: Board) -> Tuple[int, int]:
        empty_cells = []
        for y, row in enumerate(board.cells):
            for x, cell in enumerate(row):
                if cell is None:
                    empty_cells.append((y, x))
        return random.choice(empty_cells)


    def _get_ai_move_hard(self, board: Board) -> Tuple[int, int]:
        empty_cells = board.get_empty_cells()

        if len(empty_cells) == 9:
            return random.choice([(0, 0), (0, 2), (2, 0), (2, 2), (1, 1)])
        elif len(empty_cells) == 8 and board._cell_in_corner(board.get_filled_cells()[0][0], board.get_filled_cells()[0][1]):
                opponent_cell = board.get_filled_cells()[0]
                if opponent_cell[0] == 0:
                    y = 2
                else:
                    y = 0
                if opponent_cell[1] == 0:
                    x = 2
                else:
                    x = 0
                return (y, x)
        else:
            choices = []
            for y, x in empty_cells:
                cell_lines = board.cell_lines(y, x)
                for line in cell_lines:
                    symbols = [board.cells[y_coord][x_coord] for y_coord, x_coord in line]
                    player_symbol_count = symbols.count(self.symbol)
                    no_symbol_count = symbols.count(None)
                    opponent_symbol_count = 3 - player_symbol_count - no_symbol_count
                    if player_symbol_count == 2 and no_symbol_count == 1:
                        choices.append(
                            {
                                "cell": (y, x),
                                "score": 12
                            }
                        )
                    elif opponent_symbol_count == 2 and no_symbol_count == 1:
                        choices.append(
                            {
                                "cell": (y, x),
                                "score": 11
                            }
                        )
                    elif player_symbol_count == 1 and opponent_symbol_count == 0:
                        if board._cell_in_corner(y, x):
                            choices.append(
                                {
                                    "cell": (y, x),
                                    "score": 10
                                }
                            )
                        elif board._cell_in_center(y, x):
                            choices.append(
                                {
                                    "cell": (y, x),
                                    "score": 5
                                }
                            )
                        elif board._cell_in_edge(y, x):
                            choices.append(
                                {
                                    "cell": (y, x),
                                    "score": 2
                                }
                            )
                        else:
                            choices.append(
                                {
                                    "cell": (y, x),
                                    "score": 1
                                }
                            )
                    else:
                        choices.append(
                            {
                                "cell": (y, x),
                                "score": 0
                            }
                        )

        return max(choices, key=lambda x:x['score'])["cell"]
