def my_range(*args):
    start = 0
    stop = 1
    step = 1
    match len(args):
        case 1:
            stop = args[0]
        case 2:
            start = args[0]
            stop = args[1]
        case 3:
            start = args[0]
            stop = args[1]
            step = args[2]

    current = start
    while current < stop:
        yield current
        current += step


print(list(my_range(9)))
print(list(my_range(1, 5)))
print(list(my_range(0, 10, 2)))
to_9 = my_range(9)
while next(to_9):
    print(next(to_9))
