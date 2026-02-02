import random

def roll_dice():
    noppa = random.randint(1,6)
    print(noppa)
    return noppa

heitto = 1
while heitto != 6:
    heitto = roll_dice()

