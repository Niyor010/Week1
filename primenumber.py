# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage
number = 29
if is_prime(number):
    print("{} is a prime number.".format(number))
else:
    print("{} is not a prime number.".format(number))
