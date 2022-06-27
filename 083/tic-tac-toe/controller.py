from getch import getch

class Controller:
    CONTROLLER_MAPPING = {
        '[A': 'up',
        '[B': 'down',
        '[C': 'right',
        '[D': 'left',
        'w': 'up',
        's': 'down',
        'd': 'right',
        'a': 'left',
        'x': 'x',
        'o': 'o',
        'q': 'quit',
        'W': 'up',
        'S': 'down',
        'D': 'right',
        'A': 'left',
        'X': 'x',
        'O': 'o',
        'Q': 'quit',
        '\n': 'enter',
        '\r': 'enter',
        '\r\n': 'enter',
    }


    def get_input(self):
        key = self._get_key()
        try:
            return self.CONTROLLER_MAPPING[key]
        except KeyError:
            return None


    def _get_key(self):
        first_char = getch()
        if first_char == '\x1b':
            return getch() + getch()
        else:
            return first_char
