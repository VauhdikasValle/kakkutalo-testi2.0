import random

code1 = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

print(f"3-digit code: {code1}")

code2 = str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6))

print(f"4-digit code: {code2}")