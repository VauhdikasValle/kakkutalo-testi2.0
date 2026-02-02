import math

diameter = int(input("Enter the diameter of the first pizza (cm): "))
price = float(input("Enter the price of the first pizza (euros): "))
second_diameter = int(input("Enter the diameter of the second pizza (cm): "))
second_price = float(input("Enter the price of the second pizza (euros): "))

def calculate_unit_price(diameter, price):
    radius_m = (diameter / 100) / 2
    area_m2 = math.pi * (radius_m ** 2)
    unit_price = price / area_m2
    return unit_price

Unit_price_of_the_first_pizza = calculate_unit_price(diameter, price)

print(f"Unit price of the first pizza: {Unit_price_of_the_first_pizza:.2f} euros/m²")

Unit_price_of_the_second_pizza = calculate_unit_price(second_diameter, second_price)

print(f"Unit price of the second pizza: {Unit_price_of_the_second_pizza:.2f} euros/m²")

if Unit_price_of_the_first_pizza < Unit_price_of_the_second_pizza:
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")