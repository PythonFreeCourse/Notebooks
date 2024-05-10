from itertools import zip_longest

def interleave(*iterables):
    '''
    Interleave the elements of the given iterables.
    :param iterables: one or more iterables
    :return: an iterator that yields elements from the given iterables interleaved
    '''
    for iter in zip_longest(*iterables, fillvalue=None):
        for item in iter:
            if item is not None:  
                yield item


def test():
    result = list(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    assert result == ['a', 1, '!', 'b', 2, '@', 'c', 3, '#']

    result = list(interleave('abc', [1, 2, 3, 4], ('!', '@', '#')))
    assert result == ['a', 1, '!', 'b', 2, '@', 'c', 3, '#', 4]

    result = list(interleave('abc', [1, 2, 3], ('!', '@', '#'), [4, 5, 6]))
    assert result == ['a', 1, '!', 4, 'b', 2, '@', 5, 'c', 3, '#', 6]

    result = list(interleave('abc', [1, 2, 3], ('!', '@', '#'), [4, 5]))
    assert result == ['a', 1, '!', 4, 'b', 2, '@', 5, 'c', 3, '#']

    result = list(interleave('abc', [1, 2, 3], ('!', '@', '#'), [4, 5, 6, 7]))
    assert result == ['a', 1, '!', 4, 'b', 2, '@', 5, 'c', 3, '#', 6, 7]

    result = list(interleave('abc', [1, 2, 3], ('!', '@', '#'), [4, 5, 6, 7], [8, 9, 10]))
    assert result == ['a', 1, '!', 4, 8, 'b', 2, '@', 5, 9, 'c', 3, '#', 6, 10, 7]

    print('All tests passed')

if __name__ == '__main__':
    test()
    result = list(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    print(result)
