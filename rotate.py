
def rotate(lst: list[object]) -> None:
    """
    Verschuift alle elementen één plaats naar links.
    Het eerste element komt achteraan.

    >>> n1 = [1, 2, 3]
    >>> rotate(n1)
    >>> n1
    [2, 3, 1]

    >>> n2 = [10, 20, 30, 40]
    >>> rotate(n2)
    >>> n2
    [20, 30, 40, 10]

    >>> n3 = ["a", "b", "c"]
    >>> rotate(n3)
    >>> n3
    ['b', 'c', 'a']

    >>> n4 = []
    >>> rotate(n4)
    >>> n4
    []

    >>> n5 = [5]
    >>> rotate(n5)
    >>> n5
    [5]

    >>> n6 = [1, 1, 2]
    >>> rotate(n6)
    >>> n6
    [1, 2, 1]
    """
    if len(lst) <= 1:
        return

    eerste = lst[0]

    for index in range(len(lst) - 1):
        lst[index] = lst[index + 1]

    lst[-1] = eerste
