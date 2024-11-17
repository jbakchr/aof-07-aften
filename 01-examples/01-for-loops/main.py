"""
Eksempler på brugen af 'range' og 'for' loops
"""

# Eksempel 1 - Range loop med start, stop og 'step' værdi (som vi kender)
for i in range(1, 11, 4):
    print(f"Eksempel 1: Num is: {i}")


# Eksempel 2.1 - Klassisk 'for loop'
fruits = ["apple", "banana", "cherry", "grapes", "oranges"]

for fruit in fruits:
    print(f"Eksempel 2.1: {fruit}")


# Eksempel 2.2 - 'for loop' med 'break'
for fruit in fruits:
    if fruit == "cherry":
        break
    print(f"Eksempel 2.2: {fruit}")


# Eksempel 2.3 - 'for loop' med 'continue'
for fruit in fruits:
    if fruit == "cherry":
        continue
    print(f"Eksempel 2.3: {fruit}")


# Eksempel 2.4 - 'for loop' med 'else'
for fruit in fruits:
    print(f"Eksempel 2.4: {fruit}")
else:
    print("Eksempel 2.4: 'Else' eksekveres til sidst ..")


# Eksempel 2.5 - 'for loop' med 'pass' (dette loop gør ingenting ..)
for fruit in fruits:
    pass


# Eksempel 2.6 - 'nested' for loops (dvs. et loop i et loop)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"Eksempel 2.6: {i} {j}")
