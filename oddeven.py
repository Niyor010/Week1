# Example Python program to check if a number is even or odd

# Function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        print("{} is an even number.".format(num))
    else:
        print("{} is an odd number.".format(num))

# Example usage
number = 7
check_even_odd(number)
