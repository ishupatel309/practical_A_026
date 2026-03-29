rows = 5

for i in range(rows, 0, -1):
    print(" " * (rows - i), end="")
    
    for j in range(i):
        print("*", end=" ")
    
    print()

# alphabet_pyramid.py

rows = 5

for i in range(1, rows + 1):
    # spaces
    print(" " * (rows - i), end="")

    # alphabets
    ch = ord('A')
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1

    print()