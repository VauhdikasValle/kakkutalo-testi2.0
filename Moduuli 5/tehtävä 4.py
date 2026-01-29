town = input("Enter the name of a city: ")
list = [town]
maara = 1

for maara in range(4):
    town = input("Enter the name of a city: ")
    list.append(town)
    maara = maara + 1

print("\n")
print("The cities you entered: ")
for town_name in list:
    print(town_name)


