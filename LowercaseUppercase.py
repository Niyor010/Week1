# Function to count uppercase and lowercase letters in a string
def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

# Example usage
input_string = "Hello, World!"
upper_count, lower_count = count_upper_lower(input_string)

print("The number of uppercase letters is:", upper_count)
print("The number of lowercase letters is:", lower_count)
