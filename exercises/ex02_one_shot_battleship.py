"""EX02 - One Shot Battleship - The next step in Battleship """

__author__ = "730484781"

GRID: int = 4
SECRET_ROW: int = 3
SECRET_COLUMN: int = 2 

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

run_row: bool = True
run_column: bool = True

user_row: int = int(input("Guess a row: "))
while run_row == True:

    if user_row > GRID or user_row < 1:
        user_row: int = int(input(f"The grid is only {GRID} by {GRID}. Try Again: "))
    else:
        run_row = False

user_column: int = int(input("Guess a column: "))
while run_column == True:

    if user_column > GRID or user_column < 1:
        user_column: int = int(input(f"The grid is only {GRID} by {GRID}. Try Again: "))
    else:
        run_column = False

result_box = BLUE_BOX
if SECRET_ROW == user_row and SECRET_COLUMN == user_column:
    result_box = RED_BOX
else:
    result_box = WHITE_BOX

row_counter: int = 1

while row_counter <= GRID:
    row_string: str = ()
    column_counter: int = 1

    if user_row == row_counter:
        while column_counter <= GRID:
            if user_column == column_counter
                row_string += result_box
            else: 
                row_string += BLUE_BOX
            row_counter += 1

    




if SECRET_ROW == user_row and SECRET_COLUMN == user_column:
    print("Hit!")
else:
    print("Miss!")