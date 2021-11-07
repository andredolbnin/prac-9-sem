from math import sqrt


class Triangle:
    
    def __init__(self, a, b, c):
        self.set_values(a, b, c)
        self.bool = False
        if a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0:
            self.bool = True
    
    
    def set_values(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        
        
    def __bool__(self):
        return self.bool
       
     
    def __abs__(self):
        if self:
            cos_t = (self.a ** 2 + self.b ** 2 - self.c ** 2 ) / (2 * self.a * self.b)
            sin_t = sqrt(1 - cos_t ** 2)
            return 0.5 * self.a * self.b * sin_t
        return 0
        
    
    def __eq__(self, other):
        tri1 = sorted([self.a, self.b, self.c])
        tri2 = sorted([other.a, other.b, other.c])
        if tri1 == tri2:
            return True
        return False
    
    
    def __lt__(self, other):
        if abs(self) < abs(other):
            return True
        return False
    
    
    def __le__(self, other):
        if self < other or abs(self) == abs(other):
            return True
        return False
    
    
    def __gt__(self, other):
        if abs(self) > abs(other):
            return True
        return False
    
    
    def __ge__(self, other):
        if self > other or abs(self) == abs(other):
            return True
        return False
    
    
    def __str__(self):
        return f'{self.a}:{self.b}:{self.c}'