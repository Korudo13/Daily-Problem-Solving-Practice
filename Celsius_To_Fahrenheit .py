# Take a list of temperatures in Celsius and convert them to Fahrenheit using Python list comprehension

celsius = [0,10,20.1,34.5]

fahrenheit = [(temperature * (9.0/5.0) + 32) for temperature in celsius]

fahrenheit
# outputs [32, 42, 52.1, 66.5]

# formula for Celsius to Fahrenheit: T(°F) = T(°C) × 9/5 + 32 
