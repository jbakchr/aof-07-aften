import random

target_number = random.randint(1, 20)
guess = None

while guess != target_number:
    guess = int(input("Gæt tallet (mellem 1 og 20): "))
    if guess < target_number:
        print("For lavt gæt!")
    elif guess > target_number:
        print("For højt gæt!")

print("Tillykke! Du har gættet det rigtige tal:", target_number)
