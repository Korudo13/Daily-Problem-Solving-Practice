#Create a function that checks to see if a number is prime or not

def is_prime(num):
    """
    This function checks for prime numbers.
    INPUT: int
    OUTPUT: A print statement whether or not a number is prime.
    """
    for n in range(2,num):
        if num % n == 0:
            print 'Not Prime'
            break

    else:
        print 'The number is Prime!'

is_prime(12) # --> 'Not Prime'
is_prime(13) # --> 'The number is Prime!'
