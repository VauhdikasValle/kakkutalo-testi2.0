airports = {}
icao = {}
while True:

    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choise = int(input("Enter your choice: "))

    if choise == 1:
        icao = input("Enter_the_ICAO_code: ")
        name = input("Enter the airport name: ")
        airports[icao] = name
        print(f"Airport {name} Airport with ICAO code {icao} has been added.")

    if choise == 2:
        koodi = input("Enter_the_ICAO_code: ")
        print("Enter_the_ICAO_code")
        if koodi in airports:
            print(f"The airport is {airports[koodi]}")
        else:
                print("Airport not found.")


    if (choise == 3):
        print("Thank you for using the Airport Data Management system. Goodbye!")
        break
