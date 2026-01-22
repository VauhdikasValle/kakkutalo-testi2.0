gender = input("Enter biological gender (male/female): ")
hemoglobin = float(input("Enter hemoglobin value (g/l): "))

if gender.lower() == ("male"):
    if hemoglobin < 134:
     print("Your hemoglobin is low.")
    if 134 <= hemoglobin <= 167:
        print("Your hemoglobin is normal.")
    if hemoglobin > 167:
        print("Your hemoglobin is high.")

elif gender.lower() == ("female"):
    if hemoglobin < 117:
     print("Your hemoglobin is low.")
    if 117 <= hemoglobin <= 155 :
        print("Your hemoglobin is normal.")
    if hemoglobin > 155:
        print("Your hemoglobin is high.")
else:
    print("Invalid gender.")