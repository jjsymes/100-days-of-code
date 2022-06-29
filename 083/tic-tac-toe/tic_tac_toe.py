import sys
import random
from time import sleep
from typing import Tuple
from controller import Controller
from utils import clear_screen


class Screen:
    def display(self, *args) -> None:
        self._clear_screen()
        for arg in args:
            print(arg)


    def append_to_screen(self, *args) -> None:
        for arg in args:
            print(arg)


    def _clear_screen(self) -> None:
        clear_screen()


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
    
    def get_ai_move(self, board) -> Tuple[int, int]:
        if self.difficulty == 1:
            return self._get_ai_move_easy(board)
        else:
            return self._get_ai_move_hard(board)

    def _get_ai_move_easy(self, board) -> Tuple[int, int]:
        empty_cells = []
        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                if cell is None:
                    empty_cells.append((y, x))
        return random.choice(empty_cells)


    def _get_ai_move_hard(self, board) -> Tuple[int, int]:
        empty_cells = []
        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                if cell is None:
                    empty_cells.append((y, x))

        if len(empty_cells) == 9:
            return random.choice([(0, 0), (0, 2), (2, 0), (2, 2)])
        else:
            choices = []
            for y, x in empty_cells:
                cell_lines = self._cell_lines(y, x)
                for line in cell_lines:
                    symbols = [board[y][x] for y, x in line]
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
                        if self._cell_in_corner(y, x):
                            choices.append(
                                {
                                    "cell": (y, x),
                                    "score": 10
                                }
                            )
                        elif self._cell_in_center(y, x):
                            choices.append(
                                {
                                    "cell": (y, x),
                                    "score": 5
                                }
                            )
                        elif self._cell_in_edge(y, x):
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

        choices = sorted(choices, key=lambda d: d['score'], reverse=True)
        return choices[0].get('cell')


    def _cell_in_corner(self, y, x) -> bool:
        return y == 0 and x == 0 or y == 2 and x == 0 or y == 0 and x == 2 or y == 2 and x == 2


    def _cell_in_center(self, y, x) -> bool:
        return y == 1 and x == 1


    def _cell_in_edge(self, y, x) -> bool:
        return y == 0 or y == 2 or x == 0 or x == 2


    def _cell_lines(self, y, x) -> list:
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


class TicTacToe:
    def __init__(self) -> None:
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.active_cell = (0, 0)
        self.controller = Controller()
        self.players = [
            Player("X"),
            Player("O")
        ]
        self.active_player = self.players[0]
        self.last_active_player = self.players[1]
        self.screen = Screen()
        self._reset_game()


    def play(self) -> None:
        self._game_start()
        self._play_round()


    def _play_round(self) -> None:
        self._reset_board()
        self.active_player = self.players[1 if self.last_active_player == self.players[0] else 0]
        round_in_progress = True
        while round_in_progress:
            self._play_turn()
            winner = self._check_winner()
            if winner is not None:
                self.last_active_player.score += 1
                self.active_cell = None
                self.active_player = None
                self.screen.display(
                    self._render_frame(),
                    f"Player {winner.symbol} wins!\n"
                )
                round_in_progress = False
            elif self._check_stalemate():
                self.active_player = None
                self.screen.display(
                    self._render_frame(),
                    "Stalemate!"
                )
                round_in_progress = False
        play_again = self._play_again_prompt()
        if play_again == True:
            self._play_round()
        else:
            self._quit()


    def _play_turn(self) -> None:
        self.screen.display(self._render_frame())
        if self.active_player.is_ai == True:
            self._ai_turn()
            self.screen.display(self._render_frame())
            if self.active_player.is_ai is True:
                sleep(1)
        else:
            input = self.controller.get_input()
            self._handle_input(input)

        self.screen.display(self._render_frame())


    def _game_start(self) -> None:
        self.screen.display(self._render_splash_screen())
        sleep(3)
        self.screen.display(self._render_instructions())
        self._wait_for_input()


    def _handle_input(self, input: str) -> None:
        if input == "up" or input == "down" or input == "left" or input == "right":
            self._move_active_cell(input)
        elif input == "quit":
            self._quit()
        elif input == "x":
            if self.active_player == self.players[1]:
                self._handle_enter_pressed()
        elif input == "o":
            if self.active_player == self.players[0]:
                self._handle_enter_pressed()
        elif input == "enter":
            self._handle_enter_pressed()
        elif input == "options":
            self._options_menu()
        else:
            pass


    def _play_again_prompt(self) -> bool:
        while True:
            self.screen.append_to_screen("Press any button to play again, or q to quit")
            input = self.controller.get_input()
            if input == "quit":
                return False
            if input == "options":
                self._options_menu()
                self.screen.display(self._render_frame())
            else:
                return True


    def _move_active_cell(self, direction: str) -> None:
        if direction == "up":
            self.active_cell = (max(self.active_cell[0] - 1, 0), self.active_cell[1])
        elif direction == "down":
            self.active_cell = (min(self.active_cell[0] + 1, len(self.board) - 1), self.active_cell[1])
        elif direction == "left":
            self.active_cell = (self.active_cell[0], max(self.active_cell[1] - 1, 0))
        elif direction == "right":
            self.active_cell = (self.active_cell[0], min(self.active_cell[1] + 1, len(self.board[0]) - 1))


    def _render_active_player(self) -> str:
        return f"Current player: {self.active_player.symbol}"


    def _render_board(self) -> str:
        return (f"""

    {self._render_cell_content((0, 0))}|{self._render_cell_content((0, 1))}|{self._render_cell_content((0, 2))}
    ---+---+---
    {self._render_cell_content((1, 0))}|{self._render_cell_content((1, 1))}|{self._render_cell_content((1, 2))}
    ---+---+---
    {self._render_cell_content((2, 0))}|{self._render_cell_content((2, 1))}|{self._render_cell_content((2, 2))}

        """)


    def _render_splash_screen(self) -> str:
        return (f"""
        -----------------------------------------------------
        |                                                   |
        |                                                   |
        |                    TIC|   |                       |
        |                    ---+---+---                    |
        |                       |TAC|                       |
        |                    ---+---+---                    |
        |                       |   |TOE                    |
        |                                                   |
        |                                                   |
        -----------------------------------------------------
        """)


    def _render_instructions(self) -> str:
        controller_mapping = self.controller.CONTROLLER_MAPPING.copy()
        controller_mapping["↑"] = controller_mapping.pop("[A")
        controller_mapping["↓"] = controller_mapping.pop("[B")
        controller_mapping["→"] = controller_mapping.pop("[C")
        controller_mapping["←"] = controller_mapping.pop("[D")
        controller_mapping["⎆"] = controller_mapping.pop("\n")
        controller_mapping.pop("\r")
        controller_mapping.pop("\r\n")
        keys = [key for key in controller_mapping if key.islower()]
        for key in keys:
            controller_mapping[key] = controller_mapping.pop(key.upper())
        controls_list = "\n".join(f"\t{k}: {v}" for k, v in controller_mapping.items())
        return (
        "Controls:\n"
        f"{controls_list}"
        "\n"
        )


    def _render_cell_content(self, cell: tuple) -> str:
        if cell == self.active_cell and self.active_player is not None and self.active_player.is_ai is False:
            padding_left = ">"
            padding_right = "<"
        else:
            padding_left = " "
            padding_right = " "
        symbol = self.board[cell[0]][cell[1]]
        if symbol is None:
            symbol = " "
        return f"{padding_left}{symbol}{padding_right}"

    def _render_frame(self) -> str:
        frame = self._render_scoreboard()
        frame += self._render_board() + "\n"
        if self.active_player is not None:
            frame += self._render_active_player() + "\n"
        return frame


    def _render_scoreboard(self) -> str:
        player_0_score = str(self.players[0].score)
        player_1_score = str(self.players[1].score)
        score_length = max(len(player_0_score), len(player_1_score))
        extra_padding = "-" * (score_length - 3)
        return (f"""
Score:
 --------------{extra_padding}
| Player {self.players[0].symbol} |{player_0_score.center(3 + len(extra_padding))}|
|----------|---{extra_padding}|
| Player {self.players[1].symbol} |{player_1_score.center(3 + len(extra_padding))}|
 --------------{extra_padding}
        """)


    def _wait_for_input(self) -> None:
        self.screen.append_to_screen("Press any key to continue...")
        self.controller.get_input()


    def _handle_enter_pressed(self) -> None:
        if self.board[self.active_cell[0]][self.active_cell[1]] is None:
            self.board[self.active_cell[0]][self.active_cell[1]] = self.active_player.symbol
            self.last_active_player = self.active_player
            self.active_player = self.players[1 if self.active_player == self.players[0] else 0]
            self.active_cell = self._first_empty_cell()


    def _check_winner(self):
        winner = None
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            winner = self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            winner = self.board[0][2]
        else:
           for i in range(3):
                if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not None:
                    winner = self.board[i][0]
                elif self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:
                    winner = self.board[0][i]

        if winner is not None:
            for player in self.players:
                if player.symbol == winner:
                    winner = player

        return winner


    def _check_stalemate(self) -> bool:
        if self._first_empty_cell() is None:
            return True
        else:
            return False


    def _first_empty_cell(self):
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell is None:
                    return (y, x)
        return None


    def _reset_game(self):
        self._reset_board()
        self.players = [
            Player("X"),
            Player("O")
        ]
        self.active_player = self.players[0]
        self.last_active_player = self.players[1]
    

    def _reset_board(self) -> None:
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.active_cell = (0, 0)


    def _options_menu(self):
        self.screen.display(
            "Options:",
            "1. Reset game",
            f"2. Player {self.players[0].symbol} toggle AI: {self.players[0].is_ai}",
            f"3. Player {self.players[0].symbol} AI difficulty: {self.players[0].difficulty}",
            f"4. Player {self.players[1].symbol} toggle AI: {self.players[1].is_ai}",
            f"5. Player {self.players[1].symbol} AI difficulty: {self.players[1].difficulty}",
            "6. Back",
            "7. Quit",
            "\n\n",
            "Choose an option: "
        )

        option = self.controller.get_input()
        if option == "1":
            self._reset_game()
        elif option == "2":
            self.players[0].is_ai = not self.players[0].is_ai
            self._options_menu()
        elif option == "3":
            self.players[0].change_difficulty()
            self._options_menu()
        elif option == "4":
            self.players[1].is_ai = not self.players[1].is_ai
            self._options_menu()
        elif option == "5":
            self.players[1].change_difficulty()
            self._options_menu()
        elif option == "7" or option == "quit":
            self._quit()
        else:
            pass

        self._render_frame()


    def _quit(self):
        sys.exit(0)


    def _ai_turn(self):
        self.active_cell = self.active_player.get_ai_move(self.board)
        self._handle_enter_pressed()