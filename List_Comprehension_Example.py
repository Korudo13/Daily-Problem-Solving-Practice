# Convert for loop examples into list comprenensions, and list comprension examples into for loops

'''
  # For Loop Example 1

  # for loop version
  lst = []

  for letter in 'word':
      lst.append(letter)

  print l
'''

# Conversion 1

lst = [letter for letter in 'word']
print lst


'''
# List Comprenesion Example 1

lst = [x**2 for x in range(0,11)]

print lst
'''


# Conversion 2

lst = []

for x in range(0,11):
    lst.append(x**2)

print lst


'''
# For Loop Example 2

lst = []

for number in range(11):
    if number %2 == 0:
        lst.append(number)

print lst
'''

# Conversion 3

lst = [number for number in range(11) if number %2 == 0]
print lst



'''
# List Comprenension Example 2

fahrenheit = [100.0, 87.0, 65.0, 32.0, 0, -20.0]

celsius  = [(temperature - 32) * 5 / 9 for temperature in fahrenheit]

print celsius
'''

# Conversion 4

fahrenheit = [100.0, 87.0, 65.0, 32.0, 0, -20.0]
celsius = []

for temperature in fahrenheit:
    celsius.append((temperature - 32) * 5 / 9)

print celsius

