# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Example usage
celsius_temperature = 25
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)

print("{}°C is equivalent to {}°F".format(celsius_temperature, fahrenheit_temperature))
