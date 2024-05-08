def cup_of_join(*lists, sep = None):
    if sep is None:
        return [item for lst in lists for item in lst]
    else:
        return [item for lst in lists for item in (lst + [sep])]

def main():
    print(cup_of_join([1,2,3],['a','b'],[True, False]))
    print(cup_of_join([1, 2, 3], ['a', 'b'], [True, False], sep = '-'))

if __name__ == '__main__':
    main()