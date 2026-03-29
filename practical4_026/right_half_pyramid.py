



# -------- Part 1: Star Pyramid --------
rows = 6

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# -------- Part 2: Number Pattern (ONLY 2 ROWS) --------
num = 1

# first row
for i in range(5):
    print(num, end=" ")
    num += 1
print()

# second row
for i in range(4):
    print(num, end=" ")
    num += 1
print()

# -------- Part 3: Restart from 1 --------
num = 1
rows = 3

for i in range(rows, 0, -1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()