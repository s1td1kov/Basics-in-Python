for x in range(10):
    for y in range(10):
        if x != 0 and y != 0:
            if 2 * x * y == 10 * x + y:
                print(10 * x + y, end=' ')
