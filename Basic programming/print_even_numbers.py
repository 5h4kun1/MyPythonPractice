numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Iterate through each number in the list
for number in numbers:
    # Check if the number is even
    if number % 2 == 0:
        # Print the even number
        print(number, end=' ')


"""
# Prompt the user to enter a list of numbers
numbers = input("Enter a list of numbers, separated by commas: ")

# Convert the input string into a list of integers
numbers = [int(num) for num in numbers.split(",")]

# Iterate through each number in the list
for number in numbers:
    # Check if the number is even
    if number % 2 == 0:
        # Print the even number
        print(number, end=' ')
"""