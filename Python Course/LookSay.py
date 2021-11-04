import itertools

def LookSay():
    l = [1]
    yield 1
    while True:
        tmp = itertools.groupby(l)
        l = []
        for item in tmp:
            l.append(len(list(item[1])))
            yield l[-1]
            l.append(item[0])
            yield l[-1]