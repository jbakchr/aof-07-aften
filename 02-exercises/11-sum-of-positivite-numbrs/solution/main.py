total_sum = 0
number = 0

while number >= 0:
    number = int(input("Indtast et tal (negative tal stopper programmet): "))
    if number >= 0:
        total_sum += number

print("Sum of positive numbers:", total_sum)
