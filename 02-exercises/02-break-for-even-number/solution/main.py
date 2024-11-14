numbers = [3, 13, 5, 9, 17, 8, 21, 7]
contains_evens = False

for num in numbers:
    if num % 2 == 0:
        contains_evens = True
        break

if contains_evens:
    print("Listen indeholder et lige tal")
else:
    print("Listen indeholder IKKE et lige tal")
