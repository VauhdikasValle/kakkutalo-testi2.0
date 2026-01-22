# # eka = 1
# # while eka <= 9:
# #     toka = 1
# #     while toka <= 1:
# #         print(f"{eka} kertaa {toka} on {eka*toka:d}")
# #         toka = toka + 1
# #     eka = eka + 1
#
# import random
# toistot = 0
# heitot_yhteensä = 0
# while toistot < 100000:
#
#     #heitetään niin kauan kunnes saadaan 2 kuutosta
#     noppa1 = noppa2 = heitot = 0
#     while (noppa1!=6 or noppa2!=6):
#         noppa1 = random.randint(1,6)
#         noppa2 = random.randint(1,6)
#         heitot = heitot + 1
#
#     #print(f"Tarvittiin {heitot:d} heittoa.")
#     #kasvatetaan kierroslaskuria ja lasketaan heittojen kokonaismäärä
#     toistot = toistot + 1
#     heitot_yhteensä = heitot_yhteensä + heitot
#
#     #lasketaan keskiarvo ja tulostus
# heitot_keskimäärin = heitot_yhteensä/toistot
# print(f"Heitot keskimäärin: {heitot_keskimäärin:6.2f}")

luku = 1
while luku<5:
    print (luku)

# Tänne ei koskaan päästä:
print("Valmista tuli.")