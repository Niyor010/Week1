# Function to find the largest item in a list
def find_largest_item(input_list):
    if len(input_list) == 0:
        return None  # Return None if the list is empty
    largest = input_list[0]
    for item in input_list:
        if item > largest:
            largest = item
    return largest

# Example usage
example_list = [3, 8, 2, 20, 5, 12]
largest_item = find_largest_item(example_list)

print("The largest item in the list is:", largest_item)
