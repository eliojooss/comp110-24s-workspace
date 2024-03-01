def odd_even(list: list[int]) -> list[int]:
    new_list: list[int] = []
    for i in range(0, len(list)):
        if i % 2 == 0:
            if list[i] % 2 == 1:
                new_list.append(list[i])
    return new_list

def short_words(list: list[str]) -> list[str]:
    return_list: list[str] = []
    for i in list:
        if len(i) < 5:
            return_list.append(i)
        else:
            print(f"{i} is too long!")
    return return_list

def double(x: int) -> int:
    return x * 2

def double_display(y: int):
    print(y * 2)

double_display(2)
    