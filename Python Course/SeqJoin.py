import itertools

def special_iterator(s):
    iters = []
    for word in s:
        iters.append(itertools.chain(word))
    fs = []
    for k, i in enumerate(iters):
        fs.append((k, next(i)))
    fs.sort(key = lambda x: x[1])
    ind = fs[0][0]
    yield fs.pop(0)[1]
    while True:
        el = next(iters[ind], None)
        if el == None:
            if not fs:
                return None
            fs.sort(key = lambda x: x[1])
            ind = fs[0][0]
            yield fs.pop(0)[1]
        else:
            fs.append((ind, el))
            fs.sort(key = lambda x: x[1])
            ind = fs[0][0]
            yield fs.pop(0)[1]
        
def joinseq(*s):
    i = special_iterator(s)
    while True:
        r = next(i, None)
        if r == None:
            break
        yield r