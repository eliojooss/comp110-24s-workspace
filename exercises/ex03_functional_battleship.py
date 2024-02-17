"""EX03 - Functional_Battleship!"""

__author__ = "730484781"

run_row: bool = True
run_column: bool = True

def input_guess(grid: int, row_column: str) -> int:
    assert row_column == 'row' or row_column == 'column'
    run_row: bool = True
    run_column: bool = True
    
    if row_column == 'row':
        user_row: int = int(input("Guess a row: "))
        while run_row == True:

            if user_row > grid or user_row < 1:
                user_row = int(input(f"The grid is only {grid} by {grid}. Try Again: "))
            else:
                run_row = False
        return user_row
    elif row_column == 'column':
        user_column: int = int(input("Guess a column: "))
        while run_column == True:

            if user_column > grid or user_column < 1:
                user_column = int(input(f"The grid is only {grid} by {grid}. Try Again: "))
            else:
                run_column = False
        return user_column
    

    

