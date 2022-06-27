import sys
from time import sleep
from controller import Controller
from utils import clear_screen


class TicTacToe:
    def __init__(self) -> None:
        self.board = [[None, None, None] for _ in range(3)]
        self.active_cell = (0, 0)
        self.controller = Controller()
        self.players = ["O", "X"]
        self.current_player = self.players[0]


    def play(self) -> None:
        clear_screen()
        print(self._render_splash_screen())
        sleep(3)
        clear_screen()
        print(self._render_instructions())
        self._wait_for_input()
        while True:
            clear_screen()
            print(self._render_frame())
            k = self.controller.get_input()
            self._handle_input(k)
            clear_screen()
            print(self._render_frame())
            winner = self._check_winner()
            if winner is not None:
                self.active_cell = None
                clear_screen()
                print(self._render_frame())
                print(f"Player {winner} wins!")
                sys.exit(0)
            elif self._check_stalemate():
                clear_screen()
                self.active_cell = None
                print(self._render_frame())
                print("Stalemate!")
                sys.exit(0)

    def _handle_input(self, input: str) -> None:
        if input == "up" or input == "down" or input == "left" or input == "right":
            self._move_active_cell(input)
        elif input == "quit":
            sys.exit(0)
        elif input == "x":
            if self.current_player == self.players[1]:
                self._handle_enter_pressed()
        elif input == "o":
            if self.current_player == self.players[0]:
                self._handle_enter_pressed()
        elif input == "enter":
            self._handle_enter_pressed()
        else:
            print("Invalid input")


    def _move_active_cell(self, direction: str) -> None:
        if direction == "up":
            self.active_cell = (max(self.active_cell[0] - 1, 0), self.active_cell[1])
        elif direction == "down":
            self.active_cell = (min(self.active_cell[0] + 1, len(self.board) - 1), self.active_cell[1])
        elif direction == "left":
            self.active_cell = (self.active_cell[0], max(self.active_cell[1] - 1, 0))
        elif direction == "right":
            self.active_cell = (self.active_cell[0], min(self.active_cell[1] + 1, len(self.board[0]) - 1))


    def _render_current_player(self) -> str:
        return f"Current player: {self.current_player}"


    def _render_board(self) -> str:
        return (f"""
         ---+---+---
        |{self._render_cell_content((0, 0))}|{self._render_cell_content((0, 1))}|{self._render_cell_content((0, 2))}|
         ---+---+---
        |{self._render_cell_content((1, 0))}|{self._render_cell_content((1, 1))}|{self._render_cell_content((1, 2))}|
         ---+---+---
        |{self._render_cell_content((2, 0))}|{self._render_cell_content((2, 1))}|{self._render_cell_content((2, 2))}|
         ---+---+---
        """)


    def _render_splash_screen(self) -> str:
        return (f"""
        -----------------------------------------------------
        |                                                   |
        |                    ---+---+---                    |
        |                   |TIC|   |   |                   |
        |                    ---+---+---                    |
        |                   |   |TAC|   |                   |
        |                    ---+---+---                    |
        |                   |   |   |TOE|                   |
        |                    ---+---+---                    |
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
        if cell == self.active_cell:
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
        frame = self._render_board() + "\n" + self._render_current_player()
        return frame


    def _wait_for_input(self) -> None:
        print("Press any key to continue...")
        self.controller.get_input()


    def _handle_enter_pressed(self) -> None:
        if self.board[self.active_cell[0]][self.active_cell[1]] is None:
            self.board[self.active_cell[0]][self.active_cell[1]] = self.current_player
            self.current_player = self.players[1 if self.current_player == self.players[0] else 0]


    def _check_winner(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return self.board[0][2]
        else:
           for i in range(3):
                if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not None:
                    return self.board[i][0]
                elif self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:
                    return self.board[0][i]
        return None


    def _check_stalemate(self) -> bool:
        for row in self.board:
            for cell in row:
                if cell is None:
                    return False
        return True
