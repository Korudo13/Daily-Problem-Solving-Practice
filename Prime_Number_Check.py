#Create a function that checks to see if a number is prime or not

# Method 1
def is_prime_manual(num):
    """
    This function checks for prime numbers.
    INPUT: int
    OUTPUT: A print statement whether or not a number is prime.
    """
    for i in range(2,num):
        if num % i == 0:
            print 'Not Prime'
            break

    else:
        print 'The number is Prime!'

is_prime_manual(12) # --> 'Not Prime'
is_prime_manual(13) # --> 'The number is Prime!'


# Method 2
import math

def is_prime_math(num):

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print 'Not Prime'
            return False
            break

    else:
        print 'The number is Prime!'
        return True

is_prime_math(12) # --> 'Not Prime' (False)
is_prime_math(13) # --> 'The number is Prime!' (True)
