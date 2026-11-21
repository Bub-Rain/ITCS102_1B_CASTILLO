rimuru = {"Name": "Rimuru Tempest", "Skill": "Predator, Gluttony, Beelzebuth"}
milim = {"Name": "Milim Nava", "Skill": "Drago Nova, Dragon Eye, Magicule Breeder"}
benimaru = {"Name": "Benimaru", "Skill": "Hellflare, Black Flame, Swordsmanship"}

meliodas = {"Name": "Meliodas", "Skill": "Full Counter, Demon Mark, Hellblaze"}
escanor = {"Name": "Escanor", "Skill": "Sunshine, Cruel Sun, Divine Sword"}
ban = {"Name": "Ban", "Skill": "Snatch, Hunter Fest, Immortality"}

subaru = {"Name": "Natsuki Subaru", "Skill": "Return by Death, Invisible Providence"}
emilia = {"Name": "Emilia", "Skill": "Ice Magic, Spirit Arts, Absolute Zero"}
rem = {"Name": "Rem", "Skill": "Water Magic, Healing, Morning Star"}

kaneki = {"Name": "Ken Kaneki", "Skill": "Kagune, Regeneration, Kakuja"}
touka = {"Name": "Touka Kirishima", "Skill": "Ukaku Kagune, High Speed"}
juuzou = {"Name": "Juuzou Suzuya", "Skill": "Quinque, High Agility"}

Tensura = [rimuru, milim, benimaru]
SevenDS = [meliodas, escanor, ban]
ReZero = [subaru, emilia, rem]
TokyoGhoul = [kaneki, touka, juuzou]

Anime = {
    "1. Tensura": Tensura,
    "2. Seven Deadly Sins": SevenDS,
    "3. Re:Zero": ReZero,
    "4. Tokyo Ghoul": TokyoGhoul
}

print("====== ANIME LIBRARY ======")
for name in Anime:
    print(name)

while True:
    ask = input("\nChoose an anime (1-4) or 5 to exit: ")

    if ask == "1":
        selected = Tensura
    elif ask == "2":
        selected = SevenDS
    elif ask == "3":
        selected = ReZero
    elif ask == "4":
        selected = TokyoGhoul
    elif ask == "5":
        print("Exiting library...")
        break
    else:
        print("Invalid choice!")
        continue

    for hero in selected:
        print("\nName:", hero["Name"])
        print("Skills:", hero["Skill"])