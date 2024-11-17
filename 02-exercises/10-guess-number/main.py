"""
I nedenstående er du givet noget kode som genererer et tilfældigt tal mellem 1 og 20.

Din opgave er at skrive et program der bedere brugeren om at gætte tallet, og giver feedback, hvis gættet er for højt eller for lavt. Programmet bør blive ved med at spørge, indtil brugeren gætter det rigtige tal.
"""

import random

target_number = random.randint(1, 20)
