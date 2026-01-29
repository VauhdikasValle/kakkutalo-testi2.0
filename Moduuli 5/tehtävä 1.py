# import random
#
# dice=input("How many dice to roll: ")
# dice = str(random.randint(1, 6))
#
# Sum of the dice=
#
# def neliosumma(eka, toka):
#     ns = eka**2 + toka**2
#     return ns


import random
nopat = int(input("How many dice to roll: "))
heitot = []

for i in range(nopat):
    nopat = random.randint(1, 6)
    heitot.append(nopat)


print(f"Sum of the dice: {sum(heitot):}")