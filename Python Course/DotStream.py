def segment_generator(a, b, count):
    for i in range(count):
        yield a + i * (b - a) / (count - 1)
        
        
def slice_segment_generator(a, b, count, s, f):
    for i in range(s, f):
        yield a + i * (b - a) / (count - 1)
        
        
def extrapolate_generator(a, b, first, second, third):
    cur = first 
    while (cur < 0):
        yield a + cur * (b - a) / (third - 1)
        cur += 1
        
    if second <= third:
        it = segment_generator(a, b, third)
        while (cur < second):
            yield next(it)
            cur += 1    
            
    else:
        it = segment_generator(a, b, third)
        while (cur < third):
            yield next(it)
            cur += 1
        while (cur < second):
            yield a + cur * (b - a) / (third - 1)
            cur += 1
    

class Dots:
    
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    
    def __getitem__(self, arg):
        #d[n]
        if isinstance(arg, int):
            return segment_generator(self.a, self.b, arg)
            
        if isinstance(arg, slice):
            first = arg.start
            second = arg.stop
            third = arg.step
            
            #d[i:n]
            if not third:
                return self.a + first * (self.b - self.a) / (second - 1)
            
            #d[i:j:n]
            else:
                if not first:
                    first = 0
                if not second:
                    second = third
                    
                if 0 <= first <= second <= third:
                    return slice_segment_generator(self.a, self.b, third, first, second)
                
                else:
                    return extrapolate_generator(self.a, self.b, first, second, third)