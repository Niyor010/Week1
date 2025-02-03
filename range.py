# Function to check if a number is in a given range
def is_in_range(num, start, end):
    if start <= num <= end:
        return True
    else:
        return False

# Example usage
number = 10
range_start = 5
range_end = 15

if is_in_range(number, range_start, range_end):
    print("{} is in the range [{}, {}].".format(number, range_start, range_end))
else:
    print("{} is not in the range [{}, {}].".format(number, range_start, range_end))
