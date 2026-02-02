# nimet = ("juha" , "matti" , "kloiri")
# print(nimet[1])
#
# hedelmat = "appelsiini", "omena"
# (eka, toka) = hedelmat
# print(hedelmat[0])

import random

def heitä():
    eka, toka = random.randint(1, 6), random.randint(1, 6)
    return eka, toka

def heitä2():
    eka, toka = random.randint(1, 6), random.randint(1, 6)
    return eka, toka
#
# noppa1, noppa2 = heitä()
# print(f"Nopista tuli {noppa1} ja {noppa2}.")
# noppa1, noppa2 = heitä2()
# print(f"Nopista tuli {noppa1} ja {noppa2}.")

autot = [
    # Ensimmäinen auto (sanakirja)
    {
        "merkki": "Toyota",
        "malli": "Corolla",
        "vuosimalli": 2018
    },
    # Toinen auto (sanakirja)
    {
        "merkki": "Ford",
        "malli": "Focus",
        "vuosimalli": 2020
    },
    # Kolmas auto (sanakirja)
    {
        "merkki": "VW",
        "malli": "ID.3",
        "vuosimalli": 2023
    }
]


