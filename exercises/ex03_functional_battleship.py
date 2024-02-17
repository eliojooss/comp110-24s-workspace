"""EX03 - Functional_Battleship!"""

__author__ = "730484781"

# here I am just importing needed tools, and naming some variables
import random

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

run_row: bool = True
run_column: bool = True


# input guess is a function that will call for the user to put in a row or column guess
def input_guess(grid: int, row_column: str) -> int:
    """Allow for a guess input."""
    assert row_column == 'row' or row_column == 'column'
    run_row: bool = True
    run_column: bool = True
    
    if row_column == 'row':
        user_row: int = int(input("Guess a row: "))
        while run_row is True:

            if user_row > grid or user_row < 1:
                user_row = int(input(f"The grid is only {grid} by {grid}. Try Again: "))
            else:
                run_row = False
        return user_row
    else:
        user_column: int = int(input("Guess a column: "))
        while run_column is True:

            if user_column > grid or user_column < 1:
                user_column = int(input(f"The grid is only {grid} by {grid}. Try Again: "))
            else:
                run_column = False
        return user_column
    

# print grid will print out the game grid 
def print_grid(grid: int, row_guess: int, column_guess: int, correct_guess: bool) -> None:
    """Print the grid."""
    result_box: str = BLUE_BOX
    if correct_guess is True:
        result_box = RED_BOX
    else:
        result_box = WHITE_BOX

    row_counter: int = 1

    while row_counter <= grid:
        row_string: str = ("")
        column_counter: int = 1

        if row_guess == row_counter:
            while column_counter <= grid:
                if column_guess == column_counter:
                    row_string += result_box
                else: 
                    row_string += BLUE_BOX
                column_counter += 1
        else:
            while column_counter <= grid:
                row_string += BLUE_BOX
                column_counter += 1
        row_counter += 1
        print(row_string)


# function correct guess simply checks if the guesses are correct or not 
def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Check if guess is correct."""
    if secret_row == row_guess and secret_column == column_guess:
        return True
    else:
        return False


# this runs the main game loop that allows the user multiple terms, utilizing previous functions to simplify programming
def main(grid: int, secret_row: int, secret_column: int) -> None:
    """Main function."""
    turn: int = 1
    has_won: bool = False
    
    while turn <= 5 and has_won is False:
        print(f'=== Turn {turn}/5 ===')

        user_row = input_guess(grid, 'column') 
        user_column = input_guess(grid, 'row')
        print_grid(grid, user_row, user_column, correct_guess(user_row, user_column, secret_row, secret_column))
        if correct_guess(user_row, user_column, secret_row, secret_column) is True:
            print('Hit!')
            print(f'You won in {turn}/5 Turns!')
            has_won = True
        elif turn == 5:
            print('X/5 - Better luck next time!')
        else:
            print('Miss!')
        turn += 1


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))