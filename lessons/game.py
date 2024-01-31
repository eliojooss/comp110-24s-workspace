"""Number guessing game."""
from random import randint

SECRET: int = randint(1,10)
correct: bool = False

while not correct: #same as saying while correct == False
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"You got it right! {guess} is the secret number!")
        correct = True
    else:
        if guess > 10:
            print("Your guess is to High!")
        if guess < 1:
            print("Your guess is to low!")
        print("Try again!")