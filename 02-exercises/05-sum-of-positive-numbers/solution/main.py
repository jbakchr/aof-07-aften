numbers = [-5, 3, 7, -2, 9, -1, 6]
total = 0

for num in numbers:
    if num <= 0:
        continue
    total += num

print("Sum of positive numbers:", total)
