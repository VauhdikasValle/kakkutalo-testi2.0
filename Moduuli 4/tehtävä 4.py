import random

oikea_luku = random.randint(1, 10)

while True:
    luku=int(input("Guess a number (1-10): "))

    if oikea_luku < luku:
        print("Too high")

    elif oikea_luku > luku:
        print("Too low")

    else:
        print("Correct")
        break

