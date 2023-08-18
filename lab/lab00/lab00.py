def twenty_seventeen():
    """Come up with the most creative expression that evaluates to 2017,
    using only numbers and the +, *, and - operators.

    >>> twenty_seventeen()
    2017
    """
    from operator import add,sub,mul
    return add(mul(sub(250, 50), mul(2,5)), add(7,sub(12,2)))

