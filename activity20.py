anime = []

ans = input("Do you watch anime? (YES/NO) --> ").lower()

while True:

    if ans == "yes":
        title = input("Enter an anime title --> ")
        anime.append(title)

        ans = input("Do you want to add another anime? (YES/NO) --> ").lower()

    else:
        print("Your anime list: ")
        print(anime)
        break