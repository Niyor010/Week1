# Example Python program to greet a user by their name

# Function to greet the user
def greet_user(name):
    print("Hello, {}! Welcome!".format(name))

# Prompt the user to enter their name
user_name = input("Enter your name: ")

# Call the function to greet the user
greet_user(user_name)
