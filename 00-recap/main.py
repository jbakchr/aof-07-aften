"""
Recap fra 6. aften
"""

# Eksempel 1 - om datastrukturen 'dict'
person = {
    "name": "Jonas",
    "city": "Hillerød",
    "age": 41,
    "family": [
        {"type": "dad", "name": "Bent", "age": 70},
        {"type": "mom", "name": "Susanne", "age": 66},
        {"type": "kid", "name": "Milton", "age": 14},
        {"type": "kid", "name": "Edgar", "age": 10},
    ],
}
x = "name"
name = person[x]
age = person.get("age")

person["is_awesome"] = True
person.update({"likes": ["Bad Omens", "The Prodigy", "Pink Floyd", "Python"]})

for key, value in person.items():
    if key == "family":
        for family_member in value:
            print(f"Eksempel 1: {family_member["name"]}")


# Eksempel 2 - om kontrolstrukturerne 'if', 'elif' og 'else'
x = 20
y = 10
z = 15

if x > y:
    print("Eksempel 2: x er større end y")


if x > y and x > z:
    print("Eksempel 2: x er større end y og z")


if x < y:
    print(
        "Eksempel 2: x er ikke mindre end y, så denne kodeblok bliver ikke eksekveret"
    )
elif x > y:
    print("Eksempel 2: x er større end y, så denne kodeblok bliver eksekveret")


if x < y:
    print(
        "Eksempel 2: x er ikke mindre end y, så denne kodeblok bliver ikke eksekveret"
    )
elif x < z:
    print(
        "Eksempel 2: x er større end y, så denne kodeblok bliver heller ikke eksekveret"
    )
else:
    print(
        "Eksempel 2: Da hverken 'if' eller 'elif' er sande, så eksekveres denne kodeblok"
    )
