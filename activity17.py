cars = ["BUGATTI CHIRON", "KOENIGSEGG JESKO", "HONDA CIVIC", "NISSAN GTR", "TOYOTA SUPRA", "MITSUBISHI LANCER"]

print(cars)

cars.append("FERRARI SF90")

print(cars)
print(cars[6])

cars.insert(1, "MCLAREN P1")

print(cars)
print(cars[1])

print(cars[2:6])

cars.remove("NISSAN GTR")

print(cars)

print(cars.pop(3))
print(cars)

print("NISSAN GTR" in cars)
print("BUGATTI CHIRON" in cars)