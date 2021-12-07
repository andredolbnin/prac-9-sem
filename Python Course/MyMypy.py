from functools import wraps
from inspect import getfullargspec

class checked(type):

    def proxy(self, func): 
        
        @wraps(func)
        def new_func(*args, **kwargs):
            desc = getfullargspec(func)
            l1 = len(args)
            
            for i, item in enumerate(desc.args):
                l1 -= 1
                if item == 'self':
                    continue
                if item in desc.annotations:
                    if not isinstance(args[i], desc.annotations[item]):
                        raise TypeError(f'Type mismatch: {item}')
                if l1 == 0:
                    break

            
            check = False
            for k, v in kwargs.items():
                if k in desc.kwonlyargs:
                    check = True  
            l2 = len(desc.kwonlyargs)
            for k, v in kwargs.items():
                if k in desc.kwonlyargs:
                    if k in desc.annotations:
                        if not isinstance(v, desc.annotations[item]):
                            raise TypeError(f'Type mismatch: {k}')
                    l2 -= 1
                    if l2 == 0:
                        break
                elif l2 != 0 and check:
                    if desc.varkw in desc.annotations:
                        if not isinstance(v, desc.annotations[desc.varkw]):
                            raise TypeError(f'Type mismatch: {k}')
                            
                
            if l1 > 0:
                tmp1 = args[len(args) - l1 :]
                for i, item in enumerate(tmp1):
                    if item == 'self':
                        continue
                    if desc.varargs in desc.annotations:
                        if not isinstance(tmp1[i], desc.annotations[desc.varargs]):
                            raise TypeError(f'Type mismatch: {desc.varargs}')
                            
                            
            for k, v in kwargs.items():
                if k not in desc.kwonlyargs:
                    if desc.varkw in desc.annotations:
                        if not isinstance(v, desc.annotations[desc.varkw]):
                            raise TypeError(f'Type mismatch: {k}')
                            
                            
            if 'return' in desc.annotations:
                if not isinstance(func(*args, **kwargs), desc.annotations['return']):
                    raise TypeError('Type mismatch: return')
                    
            return func(*args, **kwargs)
        
        return new_func
        
    
    def __init__(self, name, parents, ns):
        l = [(k, v) for k, v in ns.items() if not k.startswith('__')]
        funcs = []
        for f in l:
            func = getattr(self, f[0])
            funcs.append((f[0], self.proxy(func)))
        for f in funcs:
            setattr(self, f[0], f[1])
        
        return super().__init__(name, parents, ns)