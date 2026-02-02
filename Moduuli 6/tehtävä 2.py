import random

def roll_dice(tahkot):
    noppa = random.randint(1,tahkot)
    print(noppa)
    return noppa
maks = int(input("Anna nopan maksimiarvo: "))

heitto = 0
while heitto != maks:
    heitto = roll_dice(maks)