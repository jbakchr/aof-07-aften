while True:
    user_input = input("Indtast en tekst (skriv 'stop' for at afslutte programmet): ")
    if user_input.lower() == "stop":
        print("M'kay .. farvel så!")
        break
    print(f"Dit input baglæns: {user_input[::-1]}")
