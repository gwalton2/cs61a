# Q2
def if_this_not_that(i_list, this):
    """Define a function which takes a list of integers `i_list` and an integer
    `this`. For each element in `i_list`, print the element if it is larger
    than `this`; otherwise, print the word "that".

    >>> original_list = [1, 2, 3, 4, 5]
    >>> if_this_not_that(original_list, 3)
    that
    that
    that
    4
    5
    """
    "*** YOUR CODE HERE ***"
    for i in range(len(i_list)):
        element=i_list[i]
        if element>this:
            print(element)
        else:
            print('that')

# Q4
def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """
    "*** YOUR CODE HERE ***"
    return [ [i,fn(i)] for i in seq if fn(i)>=lower and fn(i)<=upper]

# Q5
def link_to_list(linked_lst):
    """Return a list that contains the values inside of linked_lst

    >>> link_to_list(empty)
    []
    >>> lst1 = link(1, link(2, link(3, empty)))
    >>> link_to_list(lst1)
    [1, 2, 3]
    """
    "*** YOUR CODE HERE ***"
    def element(lst):
        if lst==empty:
            return []
        if len(lst)==1 and type(lst[0]) is int:
            return [lst[0]]
        elif len(lst)==1:
            return element(lst[0])
        elif type(lst[0]) is int:
            return [lst[0]]+element(lst[1:])
        else:
            return element(lst[0])+element(lst[1:])
    return element(linked_lst)


# Q6
def interleave(s0, s1):
    """Interleave linked lists s0 and s1 to produce a new linked
    list.

    >>> evens = link(2, link(4, link(6, link(8, empty))))
    >>> odds = link(1, link(3, empty))
    >>> print_link(interleave(odds, evens))
    1 2 3 4 6 8
    >>> print_link(interleave(evens, odds))
    2 1 4 3 6 8
    >>> print_link(interleave(odds, odds))
    1 1 3 3
    """
    "*** YOUR CODE HERE ***"
    lst1=link_to_list(s0)
    lst2=link_to_list(s1)
    length=max(len(lst1),len(lst2))
    total=[]
    for i in range(length):
        if i<len(lst1) and i<len(lst2):
            total=total+[lst1[i],lst2[i]]
        elif i<len(lst1):
            total=total+[lst1[i]]
        else:
            total=total+[lst2[i]]
    def makelist(lst):
        if len(lst)==1:
            return [lst[0],empty]
        return list((lst[0],makelist(lst[1:])))
    return makelist(total)

# Linked List definition
empty = 'empty'


def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))


def link(first, rest=empty):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]


def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), 'first only applies to linked lists.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]


def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), 'rest only applies to linked lists.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]

def isempty(s):
    """Returns True iff s is the empty list."""
    return s is empty

def print_link(s):
    """Print elements of a linked list s.

    >>> s = link(1, link(2, link(3, empty)))
    >>> print_link(s)
    1 2 3
    """
    line = ''
    while s != empty:
        if line:
            line += ' '
        line += str(first(s))
        s = rest(s)
    print(line)