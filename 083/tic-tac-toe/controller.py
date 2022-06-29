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
        ',': 'options',
        '\n': 'enter',
        '\r': 'enter',
        '\r\n': 'enter',
    }


    def get_input(self):
        key = self._get_key()
        try:
            return self.CONTROLLER_MAPPING[key]
        except KeyError:
            return key


    def _get_key(self):
        first_char = getch()
        if first_char == '\x1b':
            return getch() + getch()
        elif first_char == b'\xe0':
            ch = getch()
            if ch == "H":
                return "[A"
            elif ch == "P":
                return "[B"
            elif ch == "M":
                return "[C"
            elif ch == "K":
                return "[D"
            else:
                return None
        elif type(first_char) == bytes:
            return None
        else:
            return first_char
