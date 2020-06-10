import random

names = []

for _ in range(1, 10):
    names.append(input("Enter a name: ")
print("All names: ", names)

idx = random.radint(0, len(names))
print("Picked name: ", names[idx])

