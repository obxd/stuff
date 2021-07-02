import curses
import random

def c_main(stdscr):
    curses.use_default_colors() 
    x = random.randint(0,curses.COLS)
    y = random.randint(0,curses.LINES)
    x_dir = 1
    y_dir = 1
    while True:
        stdscr.clear()
        x = x + 1 * x_dir
        y = y + 1 * y_dir
        if x == curses.COLS or x == 0:
            x_dir = x_dir * -1
            x = x + 2 * x_dir
        if y == curses.LINES or y == 0:
            y_dir = y_dir * -1
            y = y + 2 * y_dir
        stdscr.addch(y, x, ord('a') + random.randint(0,25))
        stdscr.refresh()
        stdscr.timeout(30)
        if stdscr.getch()!= -1: break
    return 0

def main():
    return curses.wrapper(c_main)

if __name__ == "__main__":
    exit(main())

