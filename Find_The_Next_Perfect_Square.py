'''
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the find_next_square method that finds the next integral perfect square after the one passed as a parameter.
Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.

Examples:

find_next_square(121) --> returns 144
find_next_square(625) --> returns 676
find_next_square(114) --> returns -1 since 114 is not a perfect
'''

def find_next_square(sq):
    #if sq (like 144) is an integral perfect square, take the square root + 1, then square that result
    if sq**0.5 % 1 == 0:
        result = ((sq **0.5) + 1) ** 2
        print result

    else:
        print(-1)

find_next_square(144) # --> returns 144
find_next_square(100) # --> returns 121
find_next_square(13) # --> returns -1

