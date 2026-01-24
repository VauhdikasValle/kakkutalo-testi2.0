luvut = []
while True:
    number=input("Enter a number (or press Enter to quit): ")

    if number == "":
        break

    else:
        luku = int(number)
        luvut.append(float(luku))


pienin = min(luvut)
suurin = max(luvut)

print("Smallest number:", pienin)
print("Largest number:",suurin)