correct_password = "python123"
user_password = ""

while user_password != correct_password:
    user_password = input("Indtast password: ")
    if user_password != correct_password:
        print("Forkert password, prøv igen.")

print("Whoaa .. gættede passwordet, og kan nu kalde dig selv en 'ægte' hacker!")
