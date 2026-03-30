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

# Even Numbers between 1 to 100

even_numbers = []

for num in range(1, 101):
    if num % 2 == 0:
        even_numbers.append(num)

print("Even numbers from 1 to 100:")
print(even_numbers)

print("Minimum even number:", min(even_numbers))
print("Maximum even number:", max(even_numbers))
print("Total sum of even numbers:", sum(even_numbers))

