"""Demonstrate bheavior of conditionals."""

user_input: str = input("pick a number: ")
print(type(user_input))
user_number: int = int(user_input)
print(type(user_number))

# if user_number is less than 10, print "small"
if user_number < 10:
    print("small")
else: #user_number >= 10
     print("big")

# if user_number is even, print "even"

if user_number % 2 == 0:
     print("even")
else:
     print("even")

print(user_number)