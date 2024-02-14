"""Demonstrate Basic List Syntax"""

grocery_list: list[str] = list() # <- list constructor

# could also do the command below, both of these just make an empty list

grocery_list: list[str] = [] # <- literal

print(grocery_list)

# add item to a list

grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")

print(grocery_list)

# Create an already populated list
grocery_list2: list[str] = ["bananas", "milk", "bread"]

print(grocery_list2)

#modifying by index
print(grocery_list)
grocery_list[1] = 'almond milk'
print(grocery_list)

# to remove an item, notice you use parenthases, instead of brackets

grocery_list.pop(1)
print(grocery_list)

# writing functions with lists

def display(list: list) -> list:
    print(list)

display(grocery_list)

def create(str1: str, str2: str) -> list[str]:
    created_list: list[str] = [str1,str2]
    return created_list

print(create('word', 'word2'))
