while True:
    print("\nMenu:")
    print("1. Læg 2 tal sammen")
    print("2. Gang 2 tal")
    print("3. Exit")
    choice = input("Indtast dit valg (1/2/3): ")

    if choice == "1":
        num1 = float(input("Indtast første tal: "))
        num2 = float(input("Indtast andet tal: "))
        print(f"Summen er: {num1 + num2}")
    elif choice == "2":
        num1 = float(input("Indtast første tal: "))
        num2 = float(input("Indtast andet tal: "))
        print(f"Produktet er: {num1 * num2}")
    elif choice == "3":
        print("Stopper programmet...")
        break
    else:
        print("Ugyldig indtastning. Prøv igen.")
