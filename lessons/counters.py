"""Practicing Counters"""

num_string: str = "123"

num_of_odds: int = 0
position = 0

while position < 3:
    if int(num_string[position]) % 2 == 1:
        num_of_odds += 1
    position += 1
print(num_of_odds)
