from typing import List


def cup_of_join(*lists: list, sep: str = '-') -> list:
    # I added this func just because the assignment required a function named cup_of_join and a func named join...
    return join(*lists, sep=sep)


def join(*lists: list, sep: str = '-') -> list:
    '''
    Joins the lists with the separator
    :param lists: list, lists to join
    :param sep: str, separator
    :return: list, joined list
    '''
    if not isinstance(sep, str):
        raise TypeError('The separator must be a string')
    if not all(isinstance(lst, List) for lst in lists):
        raise TypeError('All the arguments must be lists')
    if not lists:
        return None

    result = list(lists[0])

    for lst in lists[1:]:
        result.append(sep)
        result.extend(lst)

    return result


def test_join():
    assert cup_of_join([1, 2], [8], [9, 5, 6], sep='@') == [1, 2, '@', 8, '@', 9, 5, 6]
    assert cup_of_join([1, 2], [8], [9, 5, 6]) == [1, 2, '-', 8, '-', 9, 5, 6]
    assert cup_of_join([1]) == [1]
    assert cup_of_join() == None

    try:
        cup_of_join([1, 2], [8], [9, 5, 6], sep=1)
    except TypeError:
        pass
    else:
        assert False

    try:
        cup_of_join([1, 2], {3}, sep='@')
    except TypeError:
        pass
    else:
        assert False

    print('All test cases passed')


if __name__ == '__main__':
    test_join()
    