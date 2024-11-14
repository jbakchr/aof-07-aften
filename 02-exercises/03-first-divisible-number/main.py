"""
I nedenstående ser du en liste af tilfældigt genererede tal.

Din opgave er at spørge brugeren om et tal, hvortil din kode skal tjekke, hvorvidt brugerens tal er ligeligt deleligt med ét af tallene i listen.

Skriv en for-løkke, der itererer gennem listen og stopper, når den støder på det første tal, der er deleligt med det tal, brugeren har indtastet.

Når/Hvis dette sker, så skal du printe en 'f-string' som fortæller, hvad dette første delelige tal er fra listen.
"""

numbers = [
    66,
    51,
    20,
    16,
    28,
    74,
    48,
    92,
    67,
    99,
    26,
    69,
    50,
    3,
    90,
    96,
    61,
    27,
    15,
    51,
]

divisor = int(input("Indtast et tal: "))

for num in numbers:
    if num % divisor == 0:
        print(f"Første delelige tal er: {num}")
        break
