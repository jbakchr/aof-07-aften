start = 1
end = 10

for i in range(start, end + 1):
    for j in range(start, end + 1):
        print(f"{i * j}", end="\t")
    print()
