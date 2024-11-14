numbers = [
    66,
    51,
    20,
    16,
    28,
    74,
    48,
    92,
    67,
    99,
    26,
    69,
    50,
    3,
    90,
    96,
    61,
    27,
    15,
    51,
]

divisor = int(input("Indtast et tal: "))

for num in numbers:
    if num % divisor == 0:
        print(f"Første delelige tal er: {num}")
        break
