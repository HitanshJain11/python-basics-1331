# Take a number from the user
n = int(input("Enter a number: "))

# Initialize factorial value
fact = 1

# Calculate factorial using a loop
for i in range(1, n + 1):
    fact = fact * i

# Display the factorial
print("Factorial =", fact)
