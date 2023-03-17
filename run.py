import random

# Constant variables for readability
EMPTY = 0
MINE = 9
UNKNOWN = -1
FLAG = -2

cell_opened = 0
game_running = True

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
    global num_mines
    
    while True:  
        try:
            num_mines = int(input("Choose how many" 
                                  "mines you want. choose a"
                                  " number between 5 and 15: \n"))     

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


def show_solution():
    """
    Shows the user the grid with the solution/location of the mines
    """
    symbols = {9: "*"}
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
    or otherwise but a row. Because user experience asks between 1 and 7 
    and puts -1 to the input after that checks if the input
    is between 0 and 6. Passes row to ask_column function. 
    """
    while True:
        try:
            row = input("Press f to set a flag"
                        " or guess a row between 1 and 7: ")
            row = row.lower()
            if row == "f":
                # flag funtion
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
            ask_column(row)
            break


def ask_column(row):
    """
    Because of user experience flag and row gets asked at the same time,
    if a flag was put in the grid at the end of the game it asked the column.
    so in this way there is a solution to this bug. 
    Function askes the column and passes the row and column
    to the cell_activated function
    """
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
    Checks what the user input hit.
    if it hit a flag quick_remove function gets called.
    if it hit a mine game_over function gets called.
    if it hit neither the check_around function gets called.
    """
    global cell_opened

    if grid_display[row][column] == FLAG:
        print("There is a flag here!")
        quick_remove(row, column)
    elif grid[row][column] == MINE:
        print("Gameover! You hit a mine!!!")
        game_over()
    else:
        cell_opened += 1
        check_win(cell_opened)
        if game_running:
            check_around(row, column)


def check_around(row, col):
    """
    Checks around the users input if there is a mine the count
    goes up by 1 at the end returns the count. row-1 means left
    of the input row+1 is right. col-1 is above the input col+1
    is below the input, in this way we check all 8 boxes around the
    input and the box itself but we already know there is no mine here.
    if statement for out of bounds.
    reference used: https://www.youtube.com/watch?v=lla6QlAF4HQ
    """
    count = 0
    for x in range(row-1, row+2):
        for y in range(col-1, col+2):
            if x >= 0 and x < 7 and y >= 0 and y < 7:
                if grid[x][y] == MINE:
                    count += 1

        grid_display[row][col] = count
        # if count == 0:
        #     if_zero(row, col)
    
    show_grid()
    ask_coordinates()


# def if_zero(row, col):

#     count = 0
#     for i in range(row-1, row+2):
#         for j in range(col-1, col+2):
#             if i >= 0 and i < 7 and j >= 0 and j < 7:
#                 if grid[i][j] == MINE:
#                     count += 1

#                 grid_display[row][col] = count
#                 if_zero(i, j)


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
            col_flag = int(input("The column where you \
                want to put a flag (1-7): "))-1
                
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


def check_win(cell_opened):
    """
    checks if the user has won the game. the grid is 7 by 7
    so if the num of mines and times played hits 49 without
    hitting a mine the player must have winned
    """
    global num_mines
    
    if num_mines + cell_opened == 49:
        print("You Won!")
        game_over()


def game_over():
    """
    When the user hits a mine this function activates asking
    the user if they want to play a new game or not.
    """
    global grid
    global grid_display
    global game_running

    show_solution()
    while True:
        try:
            play_again = input("Do you want to play again? y/n: ")
            play_again = play_again.lower()

            if play_again == 'y':
                grid = [
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]
                ]

                grid_display = [
                        [-1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1],
                ]
                main()
                break
            elif play_again == 'n':
                print("Game Over!")
                game_running = False
                break
                
        # copied from lovesandwiches project
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.")
            continue


def main():
    # runs the functions
    ask_mines()
    show_grid()
    show_solution()
    ask_coordinates()


main()