def soma(x, y):
    #doctest
    '''
    Soma x + y
    >>> soma(10,20)
    30
    >>> soma('10',20)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float

    '''
    #assertion
    assert isinstance(x, (float, int)), 'x precisa ser int ou float'
    assert isinstance(y, (float, int)), 'y precisa ser int ou float'
    return x + y

def subtrai(x,y):
    '''
    Subtrai x - y
    >>> subtrai(10,5)
    5
    >>> subtrai("10",5)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float
    '''
    assert isinstance(x, (float, int)), 'x precisa ser int ou float'
    assert isinstance(y, (float, int)), 'y precisa ser int ou float'
    return x - y

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

