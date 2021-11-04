import itertools

def chainslice(a, b, *s):
    return itertools.islice(itertools.chain.from_iterable(s), a, b)