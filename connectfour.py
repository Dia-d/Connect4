import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("1")
    stdscr.refresh()
    stdscr.getkey()


wrapper(main)