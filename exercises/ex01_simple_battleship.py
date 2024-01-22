"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730484781"

user_input1: str = input("pick a secret boat location between 1 and 4: ")

user_number1: int = int(user_input1)
if user_number1 < 1:
    print("Error!",user_number1,"too low!")
if user_number1 > 4:
    print("Error!",user_number1,"too high!")

user_input2: str = input("pick a secret boat location between 1 and 4: ")

user_number2: int = int(user_input2)
if user_number2 < 1:
    print("Error!",user_number2,"too low!")
if user_number2 > 4:
    print("Error!",user_number2,"too high!")

user_guess1: str = input("guess a number between 1 and 4: ")

user_guessint1: int = int(user_guess1)
if user_guessint1 == user_number2:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")

user_guess2: str = input("guess a number between 1 and 4: ")

user_guessint2: int = int(user_guess2)
if user_guessint2 == user_number1:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")