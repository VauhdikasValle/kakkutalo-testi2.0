month = int(input("Enter the number of a month (1-12): "))
print(f"You entered: {month}")

def get_season(kuukausi):
    if kuukausi == 12 or kuukausi == 1 or kuukausi == 2:
        return "The season is winter."
    elif kuukausi == 3 or kuukausi == 4 or kuukausi == 5:
        return "The season is spring."
    elif kuukausi == 6 or kuukausi == 7 or kuukausi == 8:
        return "The season is summer."
    elif kuukausi == 9 or kuukausi == 10 or kuukausi == 11:
        return "The season is autumn."
    else:
        return "Please enter a number between 1 and 12."

result = get_season(month)
print(result)
