rows = int(input("Input how many rows do you want: "))
counter = 1

for x in range(1, rows+1):
    for y in range(1, x+1):
        print(counter, end=" ")
        counter += 1
    print()