# Take a list of temperatures in Celsius and convert them to Farenheit using Python list comprehension

celsius = [0,10,20.1,34.5]

farenheit = [(temperature * (9.0/5.0) + 32) for temperature in celsius]

farenheit 
# outputs [32, 42, 52.1, 66.5]

# formula for celsius to farenheit: T(°F) = T(°C) × 9/5 + 32 
