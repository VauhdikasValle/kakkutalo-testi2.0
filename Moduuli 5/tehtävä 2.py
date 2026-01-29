luvut = []
while True:
    number=input("Enter a number: ")

    if number == "":
        break

    else:
        luku = int(number)
        luvut.append(float(luku))

luvut.sort(reverse=True)
five_numbers = luvut[:5]
pienin = min(luvut)
suurin = max(luvut)

print(f"The greatest numbers in descending order: ")
for num in five_numbers:
    print(num)
