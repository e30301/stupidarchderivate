import curses
import subprocess

# Define menu options
menu = ["cfdisk", "make file systems", "Abort"]

def run_command(command):
    """Run an OS command and display the output"""
    subprocess.run(command, shell=True)
    input("\nPress Enter to return to menu...")

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    current_row = 0

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        for idx, row in enumerate(menu):
            x = w//2 - len(row)//2
            y = h//2 - len(menu)//2 + idx
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if menu[current_row] == "Abort":
                break
            elif menu[current_row] == "cfdisk":
                curses.endwin()
                run_command("python3 test.py")
            elif menu[current_row] == "make file systems":
                curses.endwin()
                run_command("pwd")

        # Re-enter curses after running command
        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(lambda stdscr: (
        curses.start_color(),
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE),
        main(stdscr)
    ))
