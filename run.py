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


def add_mines():
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
            add_mines()
    #copied from love sandwiches project
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")
        add_mines()


def main():
    add_mines()


main()