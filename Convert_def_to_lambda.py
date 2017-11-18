# Convert a def statement into a Lambda Expression (to better understand how Lambda Expressions work)

'''
* Lambda Expressions are a means to create anonymous functions (resusable code on-the-fly)
* Single-line expression, eliminates nesting
* Useful for simple tasks, not complex functions
'''

## First Example
def square(num):
    result = num**2
    print result 

square(2) #--> 4 (2*2)


#Step 1 Single-Line Conversion: single line (to think about this change)

def square(num): print num**2
square(3) #--> 9 (3*3)



#Step 2: Lambda Syntax
square = lambda num: num**2

print square(4)  #--> 16 (4*4)

#======================================================================================
## Second Example 

def cube(number):
  cubed_number = number**3
  print cubed_number

cube(2) #--> 8 (2*2*2)

#Step 1
def cube(number): number**3
cube(2)

#Step 2
cube = lambda number: number**3
print cube(2)

#======================================================================================
## Third Example

def sum(x,y):
    return x+y

print sum(10,12)


sum = lambda x,y: x+y
print sum(1,2)
