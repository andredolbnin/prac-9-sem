from functools import wraps

def counter(f):
    d = {} 
    d['count'] = 0
    
    @wraps(f)
    def new_f(*args, **kwargs):
        d['count'] += 1 
        return f(*args, *kwargs)
    
    def counter():
        return d['count']
    
    new_f.counter = counter
    
    return new_f