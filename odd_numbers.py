# Odd numbers between 1 to 100

odd_numbers = []

for i in range(1, 101):
    if i % 2 != 0:
        odd_numbers.append(i)

# Display list
print("Odd Numbers:", odd_numbers)

# Minimum odd number
print("Minimum Odd Number:", min(odd_numbers))

# Maximum odd number
print("Maximum Odd Number:", max(odd_numbers))

# Sum of odd numbers
print("Sum of Odd Numbers:", sum(odd_numbers))