# Factorial
def factorial(number):
    fact = 1

    for i in range(number, 0, -1):
        fact = fact * i

    return fact


# Greeting
def greet_me(name):
    print("Hi " + name)


# Box
def box(size):
    for x in range(size):
        for y in range(size):

            if x == 0 or y == 0 or x == size - 1 or y == size - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print()


if __name__ == "__main__":

    number = int(input("Enter a factorial number: "))
    print(f"Factorial Number: {factorial(number)}")

    name = input("Enter your name: ")
    greet_me(name)

    size = int(input("Input your size of box: "))
    box(size)
