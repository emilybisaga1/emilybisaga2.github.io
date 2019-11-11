def max_num_4(a,b,c,d):
    '''
    this function returns the maximum of a, b, c, and d
        >>> max_num_4(1,2,3,4)
        4
        >>> max_num_4(2,3,4,1)
        4
        >>> max_num_4(3,4,1,2)
        4
        >>> max_num_4(4,1,2,3)
        4
        >>> max_num_4(10,1,2,3)
        10
    '''
    maxnum= d
    if a > maxnum:
        maxnum=a
    if b > maxnum:
        maxnum=b
    if c > maxnum:
        maxnum=c
    return maxnum
    

    # DO NOT MODIFY BELOW THIS LINE
import doctest
doctest.testmod(verbose=True)
