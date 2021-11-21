from functools import wraps

def cast(t):
    def decorator(f):
        @wraps(f)
        def new_f(*args):
            try:
                return t(f(*args))
            except:
                return f(*args)
        return new_f
    return decorator