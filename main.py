import random

min = 1
max = 6

while(True):
    value = random.randint(min, max)
    print("die rolled " + str(value))
    print()
    response = input("You want to roll again?\n")
    if response == 'Y' or response == 'y':
        continue
    else:
        break

