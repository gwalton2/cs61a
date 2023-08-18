def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    "*** YOUR CODE HERE ***"
    if max(a,b)%min(a,b)==0:
        return max(a,b)

    x=2
    y=a
    while(y%b!=0):
        y=a*x
        x=x+1
    return y 


def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    x=10
    y = 1
    while(n//x!=0):
        x=x*10
        y=y+1
    x=x//10

    def has_digit(n,k,r,v):
        a=n//r
        if v==1 and a!=k:
            return 0
        while(a!=k and v>1):
            f=n-a*r
            r=r//10
            a=f//r
            n=f
            v=v-1
        if v==1 and a==k:
            return 1
        elif v==1:
            return 0
        else:
            return 1

    v=y
    a=n//x
    s=n 
    t = 0
    while(v>1):
        f=s-a*x
        x=x//10
        s=f
        v=v-1
        t = t + has_digit(s,a,x,v)
        total = y - t
        a=f//x
    return total

    


        

        

