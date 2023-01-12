"""
Some useful fibonacci functions
"""


def calculate_fibonacci(how_many: int) -> list:
    """
    Calculates the first x numbers in the fibonacci sequence and returns them as
    a list
    :param how_many: how many numbers of the sequence to calculate (returns
    empty list if <= 0 or > 30)
    :returns: list of fibonacci numbers
    """
    if how_many <= 0:
        return []
    if how_many == 1:
        return [0]
    if how_many > 30:
        return []
    res = [0, 1]
    while len(res) < how_many:
        res.append(res[-1] + res[-2])
    return res
    