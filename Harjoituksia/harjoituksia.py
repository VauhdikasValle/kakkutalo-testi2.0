# #
# # kerrat = int(input("Montako kertaa tervehditään: "))
# # tehdyt = 0
# # while tehdyt < kerrat:
# #     print("Hyvää huomenta")
# #     tehdyt = tehdyt + 1
#
# komento = input("Anna komento: ")
# while komento != "lopeta" and komento != "Lopeta" :
#         print("Suoritan toiminnon: " + komento)
#
#         komento = input("Anna komento: ")
# print("Toiminnot lopetettu.")

import random
noppa1 = 0
noppa2 = 0
heitot = 0
while (noppa1 != 6 or noppa2 != 6):
    noppa1 = random.randint(1, 6)
    noppa2 = random.randint(1, 6)
    heitot += 1
print(f"heitit {heitot:d} heittoa.")