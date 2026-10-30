rows = 7

for x in range(0, rows):
    for y in range(0, rows):
        if x+y == 3 or x+y == 9:
            print("*", end="")
        elif x+y == 5 and x != 5 and y != 5:
            print("*", end="")
        elif x+y == 7 and x != 6 and y != 6:
            print("*", end="")
        else:
            print(" ", end="")
    print()