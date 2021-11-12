class Tester():
    
    def __init__(self, fun):
        self.fun = fun
        
    def __call__(self, suite, allowed = []):
        res = 0
        for tup in suite:
            try:
                self.fun(*tup)
            except tuple(allowed):
                if not tuple(allowed):
                    return 1
                res = -1
            except:
                return 1
        
        return res