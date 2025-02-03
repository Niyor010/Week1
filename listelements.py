# Function to return a list with unique elements
def get_unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

# Example usage
original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_list = get_unique_elements(original_list)

print("Original list:", original_list)
print("List with unique elements:", unique_list)
