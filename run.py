import random

# Constant variables for readability
EMPTY = 0
MINE = 1
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
gird_display = [
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
            ask_mines()

    """copied from love sandwiches project"""
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
    for num in range(mines):
        x = random.randint(0,6) # x axis/horizontal
        y = random.randint(0,6) # y axis/vertical
        if grid[x][y] == 0:
            grid[x][y] = MINE  # MINE = 1


def show_grid():
    for row in range(0, 7):
        for col in range(0, 7):
        

def main():
    print("Welcome to a game of Minesweeper")
    ask_mines()


main()