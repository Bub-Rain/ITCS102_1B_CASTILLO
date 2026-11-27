
from activity23 import factorial, greet_me, box
import os

while True:

    print("SELECT AN OPTION:")
    print("[1] Factorial")
    print("[2] Greet Me")
    print("[3] Box")
    print("[4] Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        os.system("cls")

        number = int(input("Enter a factorial number: "))
        result = factorial(number)

        print("OUTPUT: ----->")
        print("Factorial Number:", result)

    elif choice == "2":
        os.system("cls")

        name = input("Enter your name: ")

        print("OUTPUT: ----->")
        greet_me(name)

    elif choice == "3":
        os.system("cls")

        size = int(input("Input your size of box: "))

        print("OUTPUT: ----->")
        box(size)

    elif choice == "4":
        os.system("cls")
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")
