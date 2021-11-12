class DivStr(str):

    def proxy(self, item, f):
        
        def new_f(*args, **kwargs):
            return type(self)(f(*args, **kwargs))
        
        def rename(par_f):
            par_f.__name__ = item
            return par_f
        
        return rename(new_f)
    
    def __init__(self, s):
        self.s = s
        funcs = []                 
        for i, item in enumerate(dir(self)):
            f = getattr(self, item)
            if callable(f) and not item.startswith('__'):
                funcs.append((item, self.proxy(item, f)))
        for i, item in enumerate(funcs):
            setattr(self, item[0], item[1])
                                 
    def __floordiv__(self, arg):
        r = len(self.s) // arg
        if r == 0:
            return [''] * arg
        return [type(self)(self.s[i : i + r]) for i in range(0, len(self.s) - r + 1, r)]
    
    def __mod__(self, arg):
        r = len(self.s) // arg
        rem = len(self.s) - arg * r
        return type(self)(self.s[len(self.s) - rem : len(self.s)])
    
    def __getitem__(self, arg):
        return type(self)(super().__getitem__(arg))
    
    def __add__(self, other):
        return type(self)(super().__add__(other))
    
    def __mul__(self, const):
        return type(self)(super().__mul__(const))
    
    def __rmul__(self, const):
        return type(self)(super().__rmul__(const))