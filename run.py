import random

# Constant variables for readability
EMPTY = 0
MINE = 9
UNKNOWN = -1

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
    not between 5 and 20 the user will be asked again 
    and Raises ValueError if strings cannot be converted into int.
    """
    num_mines = int(input("Choose how many mines you want. choose a number between 5 and 20: \n"))

    try:
        if num_mines > 20 or num_mines < 5:
            print("Please choose a number between 5 and 20")
            return False

    # copied from lovesandwiches project
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")
        return False

    return add_mines(num_mines)


def add_mines(mines):
    """
    Randomly places user input (between 5 and 20)
    number of mines to the grid. also checks if the
    space is not already occupied by a mine.
    """
    for num in range(mines + 1):
        x = random.randint(0, 6)  # x axis/horizontal
        y = random.randint(0, 6)  # y axis/vertical
        if grid[x][y] == 0:
            grid[x][y] = MINE  # MINE = 9


def show_grid():
    """
    Shows the grid if something is not yet shown the user sees a - symbol
    copied from
    https://www.youtube.com/watch?v=XTT8mXwIGpQ
    https://github.com/wynand1004/Projects/blob/master/Minesweeper/minesweeper.py
    """
    symbols = {-2: "F", -1: "-"}
    for row in range(0, 7):
        for col in range(0, 7):
            value = grid_display[row][col]
            if value in symbols:
                symbol = symbols[value]
            else:
                symbol = str(value)
            print(f"{symbol} ", end='')
        print("")


def ask_coordinates():
    
    row = input("Press f to set a flag or guess a row between 1 and 7: ")
    row = row.lower()
    if row == "f":
        # flag funtion
        print("setting a flag")
    else:
        row = int(row)
        print(row)

    try:
        if row > 7 or row < 1:
            print("Please choose a number between 1 and 7")
            return False

    # copied from lovesandwiches project
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")
        return False
    
    return true

    column = int(input("guess a column between 1 and 7: "))

    try:
        if column > 7 or column < 1:
            print("Please choose a number between 1 and 7")
            return False

    # copied from lovesandwiches project
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")
        return False
    
    return true
    


def main():
    # runs the functions
    ask_mines()
    show_grid()
    ask_coordinates()


main()