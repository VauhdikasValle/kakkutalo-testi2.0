import random

N = int(input("Enter how many random points to generate: "))

circle = 0
point = 0
while point < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        circle += 1
    point += 1
pi_estimate = 4 * circle / N
print(f"Approximation of pi: {pi_estimate}")