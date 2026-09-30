for i in range(1, 11, 1):
    for x in range(0, i, 1):
        print(" ", end=" ")
    for y in range(11, i, -1):
        print(y, end=" ")
    print()