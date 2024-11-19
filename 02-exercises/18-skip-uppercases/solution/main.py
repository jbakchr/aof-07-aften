text = input("Indtast din tekst: ")
index = 0

while index < len(text):
    char = text[index]
    if char.isupper():
        index += 1
        continue
    print(char, end="")
    index += 1
