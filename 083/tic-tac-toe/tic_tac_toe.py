import sys
from time import sleep
from controller import Controller
from board import Board
from player import Player
from screen import Screen


class TicTacToe:
    def __init__(self) -> None:
        self.board = Board()
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
        self.board.reset_board()
        self.active_player = self.players[1 if self.last_active_player == self.players[0] else 0]
        round_in_progress = True
        while round_in_progress:
            self._play_turn()
            winner = self._check_winner()
            if winner is not None:
                self.last_active_player.score += 1
                self.board.active_cell = None
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
        turn_in_progress = True
        current_player = self.active_player
        while turn_in_progress:
            self.screen.display(self._render_frame())
            if self.active_player.is_ai == True:
                self._ai_turn()
                self.screen.display(self._render_frame())
                if self.active_player.is_ai is True:
                    sleep(1)
            else:
                input = self.controller.get_input()
                self._handle_input(input)
            if current_player != self.active_player:
                turn_in_progress = False

        self.screen.display(self._render_frame())


    def _game_start(self) -> None:
        self.screen.display(self._render_splash_screen())
        sleep(3)
        self.screen.display(self._render_instructions())
        self._wait_for_input()


    def _handle_input(self, input: str) -> None:
        if input == "up" or input == "down" or input == "left" or input == "right":
            self.board.move_active_cell(input)
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
        if cell == self.board.active_cell and self.active_player is not None and self.active_player.is_ai is False:
            padding_left = ">"
            padding_right = "<"
        else:
            padding_left = " "
            padding_right = " "
        symbol = self.board.cells[cell[0]][cell[1]]
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
        active_cell = self.board.active_cell
        if self.board.cells[active_cell[0]][active_cell[1]] is None:
            self.board.cells[active_cell[0]][active_cell[1]] = self.active_player.symbol
            self._switch_active_player()


    def _switch_active_player(self) -> None:
            self.last_active_player = self.active_player
            self.active_player = self.players[1 if self.active_player == self.players[0] else 0]
            self.board.active_cell = self.board.first_empty_cell()


    def _check_winner(self):
        winner = None
        if self.board.cells[0][0] == self.board.cells[1][1] == self.board.cells[2][2] and self.board.cells[0][0] is not None:
            winner = self.board.cells[0][0]
        elif self.board.cells[0][2] == self.board.cells[1][1] == self.board.cells[2][0] and self.board.cells[0][2] is not None:
            winner = self.board.cells[0][2]
        else:
           for i in range(3):
                if self.board.cells[i][0] == self.board.cells[i][1] == self.board.cells[i][2] and self.board.cells[i][0] is not None:
                    winner = self.board.cells[i][0]
                elif self.board.cells[0][i] == self.board.cells[1][i] == self.board.cells[2][i] and self.board.cells[0][i] is not None:
                    winner = self.board.cells[0][i]

        if winner is not None:
            for player in self.players:
                if player.symbol == winner:
                    winner = player

        return winner


    def _check_stalemate(self) -> bool:
        if self.board.first_empty_cell() is None:
            return True
        else:
            return False


    def _reset_game(self):
        self.board.reset_board()
        self.players = [
            Player("X"),
            Player("O")
        ]
        self.active_player = self.players[0]
        self.last_active_player = self.players[1]


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
        self.board.active_cell = self.active_player.get_ai_move(self.board)
        self._handle_enter_pressed()
