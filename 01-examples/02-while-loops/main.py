"""
Eksempler på brugen af 'while loops'
"""

# Eksempel 1 - while loop med betinget variabel
num1 = 1
while num1 <= 5:
    print(f"Eksempel 1: {num1}")
    num1 += 1


# Eksempel 2 - while loop med 'break' statement
num2 = 1
while num2 <= 5:
    if num2 == 3:
        break
    print(f"Eksempel 2: {num2}")
    num2 += 1


# Eksempel 3 - while loop med 'continue' statement
num3 = 6
while num3 > 1:
    num3 -= 1
    if num3 == 3:
        continue
    print(f"Eksempel 3: {num3}")


# Example 4 - while loop med 'else' statement
num4 = 5
while num4 >= 1:
    print(f"Eksempel 4: {num4}")
    num4 -= 1
else:
    print("While loop fra eksempel 4 færdigt!")


# Eksempel 5 - nested while loops
print("Multiplication Table:")

outer_range = 5

i = 1

while i <= outer_range:

    j = 1

    while j <= outer_range:
        print(f"{i} x {j} = {i * j}", end="\t")
        j += 1

    print()
    i += 1
