import random

# Constant variables for readability
EMPTY = 0
MINE = 9
UNKNOWN = -1
FLAG = 1

# variables
setting_flag = False  # inactive

# Solution grid that the user can not see
grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

# Grid that gets displayed to the user
grid_display = [
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1],
]


def ask_mines():
    """
    converts all strings into integers gives the user an option
    to choose the amount of mines. if the amount of mines is 
    not between 5 and 15 the user will be asked again and 
    raises ValueError if strings cannot be converted into int.
    """
    while True:    
        try:
            num_mines = int(input("Choose how many mines you want. choose a number between 5 and 15: \n"))     

        # copied from lovesandwiches project
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.")
            continue

        if num_mines > 15 or num_mines < 5:
            print("Please choose a number between 5 and 15")
            continue
        else:
            # num_mines successfully parsed, and we're happy with its value.
            add_mines(num_mines)
            break


def add_mines(mines):
    """
    Randomly places user input (between 5 and 15)
    number of mines to the grid. also checks if the
    space is not already occupied by a mine.
    """
    counter = 0
    while counter < mines:
        x = random.randint(0, 6)  # x axis/horizontal
        y = random.randint(0, 6)  # y axis/vertical
        if grid[x][y] == 0:
            grid[x][y] = MINE  # MINE = 9
            counter = counter + 1
 

def show_grid():
    """
    Shows the grid if something is not yet shown the user sees a - symbol
    copied from
    https://www.youtube.com/watch?v=XTT8mXwIGpQ
    https://github.com/wynand1004/Projects/blob/master/Minesweeper/minesweeper.py
    """
    symbols = {1: "F", -1: "-"}
    for row in range(0, 7):
        for col in range(0, 7):
            value = grid_display[row][col]
            if value in symbols:
                symbol = symbols[value]
            else:
                symbol = str(value)
            print(f"{symbol} ", end='')
        print("")



def show_sol():
    symbols = {1: "F", -1: "-"}
    for row in range(0, 7):
        for col in range(0, 7):
            value = grid[row][col]
            if value in symbols:
                symbol = symbols[value]
            else:
                symbol = str(value)
            print(f"{symbol} ", end='')
        print("")


def ask_coordinates():
    """
    Ask the user if they want to put a flag goes to set_flag function
    or otherwise but a row and a column. Because user experience asks
    between 1 and 7 and puts -1 to the input after that checks if the input
    is between 0 and 6. Passes row and column to cell_activated function. 
    """
    global setting_flag
    while True:
        try:
            row = input("Press f to set a flag or guess a row between 1 and 7: ")
            row = row.lower()
            if row == "f":
                # flag funtion
                setting_flag = True
                set_flag()
                break
            else:
                row = int(row)-1

            if row > 6 or row < 0:
                print("Please choose a number between 1 and 7")
                continue
                    
        # copied from lovesandwiches project
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.")
            continue

        else:
            # row successfully parsed, and we're happy with its value.
            break

    if setting_flag is False:    
        while True:
            try:
                column = int(input("guess a column between 1 and 7: "))-1
                
                if column > 6 or column < 0:
                    print("Please choose a number between 1 and 7")
                    continue
                    
            # copied from lovesandwiches project
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.")
                continue

            else:
                # column successfully parsed, and we're happy with its value.
                break

    cell_activated(row, column)


def cell_activated(row, column):
    """
    Checks if the user row and column input hit a flag or a mine.
    if it hit a flag quick_remove function gets called.
    if it hit a mine game_over function gets called.
    """
    if grid_display[row][column] == FLAG:
        print("There is a flag here!")
        quick_remove(row, column)
    elif grid[row][column] == MINE:
        print("Gameover! You hit a mine!!!")
    else:
        grid_display[row][column] = check_around(row, column)
        show_grid()
        ask_coordinates()


def check_around(row, col):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            count = 0
            for a in (-1, 1, 1):
                for b in (-1, 1, 1):
                    if (0 <= row+a < len(grid) and 
                        0 <= col+b < len(grid[0]) and 
                        grid[row+a][col+b] == MINE): 
                        count = count + 1
            return count

def set_flag():
    """
    Gives the user a option to set a flag where they think there is a mine,
    The grid displays a F that stands for flag for better user experience.
    The user gets asked which row and column they want to place the flag.
    If there is a flag the user will go to the quick-remove function.
    """
    print("setting a flag! ")
    while True:
        try:
            row = int(input("The row where you want to put a flag (1-7): "))-1

            if row > 6 or row < 0:
                print("Please choose a number between 1 and 7")
                continue

        # copied from lovesandwiches project
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.")
            continue

        else:
            # row successfully parsed, and we're happy with its value.
            break

    while True:
        try:
            col_flag = int(input("The column where you want to put a flag (1-7): "))-1
                
            if col_flag > 6 or col_flag < 0:
                print("Please choose a number between 1 and 7")
                continue
                    
        # copied from lovesandwiches project
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.")
            continue

        else:
            # column successfully parsed, and we're happy with its value.
            break

    if grid_display[row][col_flag] == UNKNOWN:
        grid_display[row][col_flag] = FLAG
    elif grid_display[row][col_flag] == FLAG:
        print("There is a flag here!")
        quick_remove(row, col_flag)
    else:
        print("You can't put a flag here")
    
    global setting_flag
    setting_flag = False
    show_grid()
    ask_coordinates()


def quick_remove(row, column):
    """
    gives the user the option to remove a flag they hit. also gives 
    the user not to remove a flag and just goes further with the game.
    """
    while True:
        try:
            remove_flag = input("Do you want to remove the flag? y/n: ")
            remove_flag.lower()

            if remove_flag == 'y':
                grid_display[row][column] = UNKNOWN
                break
            elif remove_flag == 'n':
                break
                
        # copied from lovesandwiches project
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.")
            continue

    show_grid()    
    ask_coordinates()


def main():
    # runs the functions
    ask_mines()
    show_grid()
    show_sol()
    ask_coordinates()


main()