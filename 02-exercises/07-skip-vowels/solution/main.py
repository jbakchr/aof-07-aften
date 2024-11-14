text = "Hello World"
vowels = "aeiouAEIOU"

for char in text:
    if char in vowels:  # Check if the character is a vowel
        continue  # Skip to the next iteration if true
    print(char, end=" ")
