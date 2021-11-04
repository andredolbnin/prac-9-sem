import random
import itertools

def randomes(s):
    i = itertools.cycle(itertools.chain.from_iterable(s))
    while True:
        a = next(i)
        b = next(i)
        yield random.randint(a, b)