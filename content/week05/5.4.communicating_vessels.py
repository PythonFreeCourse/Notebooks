# could simply use zip but decided to make recursion in a functional programming style using map to strip iterables
def communicating_vessels(*iterables):
    if all(not itr for itr in
           iterables):  # returns if no more items in any of the iterables (in case of uneven iterables)
        return
    for itr in iterables:
        try:
            yield next(iter(itr))
        except StopIteration:
            continue
    yield from interleave(*(map(lambda it: it[1:], iterables)))

def main():
    for it in interleave('ab', [1,2,3], ('@','%')):
        print(it)

if __name__ == '__main__':
    main()
