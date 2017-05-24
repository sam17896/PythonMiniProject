import random


number = random.randint(0, 100)

guessNumber = input("Guess the number?\n")

while str(number) != guessNumber:
    if str(number) > guessNumber:
        guessNumber = input("TOO LOW !! Guess again\n")
    else:
        guessNumber = input("TOO HIGH!! Guess again\n")

print("BINGO!! You got it right!! the number is " + str(number))

