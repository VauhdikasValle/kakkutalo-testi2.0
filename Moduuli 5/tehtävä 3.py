luku = int(input("Enter an integer: "))
alkuperäinen = luku
lista = []


while luku > 0:
    jaettu = alkuperäinen / luku

    luku = luku - 1

    lista.append(jaettu)

# print(lista)

kokonaiset = [luku for luku in lista if luku % 1 == 0]

if alkuperäinen > 1 and len(kokonaiset) < 3:
    print(f"{alkuperäinen} is a prime number.")
else:
    print(f"{alkuperäinen} is not a prime number.")
