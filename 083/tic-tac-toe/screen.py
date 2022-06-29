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
