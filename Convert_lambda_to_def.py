# Convert a Lambda Expression into a def statement (function)

##Example 1: Check if a number is even

# Step 1: Take original lambda expression
even = lambda num: num % 2 == 0
print even(4)  # returns True
print even(5)  # returns False


# Step 2: Convert syntax to def statement
def even(num):
    return num % 2 == 0

print even(10)  # returns True
print even(11)  # returns False

#===================================================================

## Example 2: Grabs the first character of a string

first = lambda s: s[0]
print first('rope')

def first:
  
#===================================================================

## Example 3: Reverse a string
rev = lambda str: str[::-1]
print rev("rope")

def reversed(str):
    rev = str[::-1]
    return rev

print reversed("rope")


