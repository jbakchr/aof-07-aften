while True:
    user_input = input("Dit input (brug 'exit' for at stoppe): ")
    if user_input.lower() == "exit":
        print("Farvel!")
        break
    else:
        print(f"Du skrev: {user_input}")
