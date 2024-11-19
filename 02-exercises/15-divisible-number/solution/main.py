start = int(input("Indtast et starttal: "))
divisor = int(input("Indtast divisor: "))

current = start
while True:
    if current % divisor == 0:
        print(f"Det første tal som kan divideres med {divisor} er: {current}")
        break
    current += 1
