"""Lab 1: Expressions and Control Structures"""

# Coding Practice

def repeated(f, n, x):
    """Returns the result of composing f n times on x.

    >>> def square(x):
    ...     return x * x
    ...
    >>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    >>> repeated(square, 1, 4)  # square(4)
    16
    >>> repeated(square, 6, 2)  # big number
    18446744073709551616
    >>> def opposite(b):
    ...     return not b
    ...
    >>> repeated(opposite, 4, True)
    True
    >>> repeated(opposite, 5, True)
    False
    >>> repeated(opposite, 631, 1)
    False
    >>> repeated(opposite, 3, 0)
    True
    """
    "*** YOUR CODE HERE ***"
    y = f(x)
    while(n>1):
        y = f(y)
        n= n-1
    return y


def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    "*** YOUR CODE HERE ***"

    y = 1
    x = 10
    if n//10 == 0:
         return n
    while(y != 0):
        y = n//x
        x=x*10
    x=x//100
    s=0
    while(x>0):
        f = n//x
        n = n-(f*x)
        x = x//10
        s = s+f
    return s






def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    y = 1
    x = 10
    k=0

    if n//10 == 0:
        return False
    
    while(y != 0):
        y = n//x
        x=x*10
        k+=1
    x=x/100

    v=1
    f=1
    while(k>0):
        if v//x==8:
            return True
        else:
            f=1
        while(f!=8 and x>0):
            f = n//x
            n = n-(f*x)
            x = x//10
            k-=1
            v=n
    return False

    



