rows = 5

for x in range(rows):
    for y in range(rows + 1):
        if x + y == 3:
            print("* ", end="")
        elif x == 3 and y < 5:
            print("* ", end="")
        elif x == 0 and y > 2:
            print("* ", end="")
        elif y == 5 and x < 3:
            print(" *", end="")
        else:
            print(" ", end="")
    print()