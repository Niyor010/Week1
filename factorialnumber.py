# Function to calculate the factorial of a number
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Example usage
number = 5
result = factorial(number)

print("The factorial of {} is: {}".format(number, result))
