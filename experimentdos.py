def count_big_drops(values: list[int]) -> int:
    """
    Schrijf hier precies vier doctests.
    """
    for i in len(values):
        if values[i] < values[i + 1] and values[i] < values[i + 1]