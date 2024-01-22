"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730484781"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

user_input1: str = input("pick a secret boat location between 1 and 4: ")
user_number1: int = int(user_input1)

if user_number1 < 1:
    print("Error!", user_number1, "too low!")
    exit()
if user_number1 > 4:
    print("Error!", user_number1, "too high!")
    exit()

user_guess1: str = input("guess a number between 1 and 4: ")
user_guessint1: int = int(user_guess1)
if user_guessint1 < 1:
    print("Error!", user_number1, "too low!")
    exit()
if user_guessint1 > 4:
    print("Error!", user_number1, "too high!")
    exit()

final_display: str = (BLUE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
user_guess_color: str = (BLUE_BOX)

if user_guessint1 == user_number1:
    user_guess_color = (RED_BOX)
    if user_guessint1 == 1:
        final_display = (user_guess_color + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    if user_guessint1 == 2:
        final_display = (BLUE_BOX + user_guess_color + BLUE_BOX + BLUE_BOX)
    if user_guessint1 == 3:
        final_display = (BLUE_BOX + BLUE_BOX + user_guess_color + BLUE_BOX)
    if user_guessint1 == 4:
        final_display = (BLUE_BOX + BLUE_BOX + BLUE_BOX + user_guess_color)
    print(final_display)
    print("Correct! You hit the ship.")    
else:
    user_guess_color = (WHITE_BOX)
    if user_guessint1 == 1:
        final_display = (user_guess_color + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    if user_guessint1 == 2:
        final_display = (BLUE_BOX + user_guess_color + BLUE_BOX + BLUE_BOX)
    if user_guessint1 == 3:
        final_display = (BLUE_BOX + BLUE_BOX + user_guess_color + BLUE_BOX)
    if user_guessint1 == 4:
        final_display = (BLUE_BOX + BLUE_BOX + BLUE_BOX + user_guess_color)
    print(final_display)
    print("Incorrect! You missed the ship.")