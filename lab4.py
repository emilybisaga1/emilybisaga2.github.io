def sum_of_digits(n):
    '''
    Calculates the sum of each of the digits in the input number n.
    HINT: use a while loop
        >>> sum_of_digits(5)
        5
        >>> sum_of_digits(15)
        6
        >>> sum_of_digits(51)
        6
        >>> sum_of_digits(1234567890)
        45
    '''
    if n < 10:
        return n
    new=n
    sumd=0
    while new > 0:
        sumd=(new%10)+sumd
        new=(new//10)
    return sumd

def min_of_digits(n):
    '''
    Calculates the smallest digit in the input number n
    HINT: use a while loop
        >>> min_of_digits(1)
        1
        >>> min_of_digits(57)
        5
        >>> min_of_digits(75)
        5
        >>> min_of_digits(571)
        1
        >>> min_of_digits(1234567890)
        0
        >>> min_of_digits(9999999949999)
        4
    '''
    if n < 10:
        return n
    smallest=n%10
    current=n//10
    while current > 0:
        new= current%10
        if new < smallest:
            smallest=new
        current=current//10    
    return smallest

def box(n):
    '''
    prints an nxn box of *
    HINT: use nested for loops
        >>> box(0)
        >>> box(1)
        *
        >>> box(2)
        **
        **
        >>> box(5)
        *****
        *****
        *****
        *****
        *****
        >>> box(15)
        ***************
        ***************
        ***************
        ***************
        ***************
        ***************
        ***************
        ***************
        ***************
        ***************
        ***************
        ***************
        ***************
        ***************
        ***************
    '''
    if n <= 0:
        return
    for i in range(n):
        print('*'*n)


def checkers(n):
    '''
    prints a "checkers board," which is an nxn box where every other element is a space
    HINT: use nested for loops
        >>> checkers(0)
        >>> checkers(1)
        *
        >>> checkers(2)
        * 
         *
        >>> checkers(5)
        * * *
         * * 
        * * *
         * * 
        * * *
        >>> checkers(15)
        * * * * * * * *
         * * * * * * * 
        * * * * * * * *
         * * * * * * * 
        * * * * * * * *
         * * * * * * * 
        * * * * * * * *
         * * * * * * * 
        * * * * * * * *
         * * * * * * * 
        * * * * * * * *
         * * * * * * * 
        * * * * * * * *
         * * * * * * * 
        * * * * * * * *
    '''
    if n<=0:
        return
    for i in range(int(n/2)):
        if n%2==0:
            print('* '*int(n/2))
            print(' *'*int(n/2))
        if n%2!=0:
            print(('* '*int(n/2)) + '*')
            print((' *'*int(n/2)) + ' ')
    if n%2!=0:
        print(('* '*int(n/2)) + '*')


def outline(n):
    '''
    prints the outline of a box, leaving the middle empty
    HINT: use nested for loops
        >>> outline(0)
        >>> outline(1)
        *
        >>> outline(2)
        **
        **
        >>> outline(5)
        *****
        *   *
        *   *
        *   *
        *****
        >>> outline(15)
        ***************
        *             *
        *             *
        *             *
        *             *
        *             *
        *             *
        *             *
        *             *
        *             *
        *             *
        *             *
        *             *
        *             *
        ***************
    '''
    if n<=0:
        return
    if n==1:
        print('*')
    if n==2:
        print('**')
        print('**')
    if n > 2:
        print('*' * n)
        for i in range(int(n-2)):
            print('*' + ' ' * (int(n-2))+ '*')
        print('*' * n)
    
# DO NOT MODIFY BELOW THIS LINE
import doctest
doctest.testmod(verbose=True)
