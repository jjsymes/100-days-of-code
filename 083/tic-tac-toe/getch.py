import sys


if sys.platform == 'win32':
    import msvcrt
    def getch():
        ch = msvcrt.getch()
        try:
            ch = ch.decode("UTF-8")
        except UnicodeDecodeError:
            pass
        return ch
else:
    import sys, tty, termios
    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
