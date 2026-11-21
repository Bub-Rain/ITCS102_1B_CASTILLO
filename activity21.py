route = ["Portofino", "Rapallo", "Zoagli", "Chiavari", "Lavagna"]
passengers = []
seats = 18
fare = 14
total = 0

while True:
    print("\n==========================")
    print("1. Sakay")
    print("2. Priority Seat")
    print("3. Para po!")
    print("4. Baba sa pinto")
    print("5. Baba sa harap")
    print("6. Seat check")
    print("7. Balikan")
    print("8. Exit")
    print("==========================")

    print("Passengers:", passengers)
    print("Seats:", len(passengers), "/", seats)

    choice = input("Enter choice: ")

    if choice == "1":
        if len(passengers) < seats:
            name = input("Name: ")
            passengers.append(name)
            total = total + fare
            print(name, "has boarded!")
        else:
            print("Puno na!")

    elif choice == "2":
        if len(passengers) < seats:
            name = input("Name: ")
            passengers.insert(0, name)
            total = total + (fare * 0.93)
            print(name, "got a priority seat!")
        else:
            print("Puno na!")

    elif choice == "3":
        name = input("Who is getting off? ")
        if name in passengers:
            passengers.remove(name)
            print(name, "has left. Ingat!")
        else:
            print("Passenger not found.")

    elif choice == "4":
        if len(passengers) > 0:
            print(passengers.pop(), "got off.")
        else:
            print("No passengers.")

    elif choice == "5":
        if len(passengers) > 0:
            print(passengers.pop(0), "got off.")
        else:
            print("No passengers.")

    elif choice == "6":
        print("Current passengers:")
        for i in range(len(passengers)):
            print(i + 1, passengers[i])

    elif choice == "7":
        route.reverse()
        print("New route:", route)

    elif choice == "8":
        print("Total fare:", total)
        break

    else:
        print("Invalid choice!")