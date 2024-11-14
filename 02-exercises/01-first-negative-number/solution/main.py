numbers = [40, 10, 20, 60, 90, 80, -5, 30, 50]

for num in numbers:
    if num < 0:
        print(f"Det første negative tal {num} findes på index: {numbers.index(num)}")
        break
