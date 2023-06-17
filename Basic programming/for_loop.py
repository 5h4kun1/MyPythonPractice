# Take input of 10 numbers from the user and save them as a list
number_list = []
for i in range(10):
    number = int(input("Enter number {}: ".format(i + 1)))
    number_list.append(number)
# String formatting allows dynamic insertion of values into strings, improving readability and flexibility.

# Create a function to add two numbers and return the result
def add_numbers(num1, num2):
    return num1 + num2

# Create a function to add all numbers in a list and print the result
def add_list_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    print("Sum of all numbers:", total)

# Example usage:
result = add_numbers(5, 3)
print("Result of adding two numbers:", result)

add_list_numbers(number_list)

