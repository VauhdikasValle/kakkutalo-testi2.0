def gallons_to_liters(gallona_maara):
    litrat = gallona_maara * 3.785
    print(f"{gallona_maara} American gallons is {litrat:.2f} liters. ")


while True:
    galloona_maara = float(input("Enter a volume in American gallons (negative value to quit): "))
    if galloona_maara < 0:
        print("Program finished.")
        break
    gallons_to_liters(galloona_maara)