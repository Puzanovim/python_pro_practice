# generators save memory

def squares(numbers: list):
    for i in numbers:
        yield i ** 2


print(list(squares([1, 2, 3, 4, 5, 6, 7, 8, 9])))
