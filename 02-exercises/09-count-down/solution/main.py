from time import sleep

number = int(input("Indtast et starttal: "))

while number >= 0:
    print(number)
    sleep(1)
    number -= 1
