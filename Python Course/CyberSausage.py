from fractions import Fraction
from itertools import cycle


class Sausage:
    
    def __init__(self, meat = 'pork!', vol = '1'):
        self.meat = meat
        self.vol = Fraction(vol)
        self.h = 3
        self.w = 12
        self.len = self.w * self.vol
        
        
    def __str__(self):
        if self.vol < Fraction('1/12'):
            s = '/|\n'
            for i in range(self.h):
                s += '||\n'
            s += '\|'
            return s
        
        full_count = self.len // self.w
        rem = self.len % self.w
        
        tmp = ''
        c = cycle(self.meat)
        for _ in range(12):
            tmp += next(c)
            
        tmp_last = ''
        c = cycle(self.meat)
        for _ in range(int(rem)):
            tmp_last += next(c)

        s = ''
        for j in range(full_count):
            s += '/'
            s += '-' * self.w
            s += '\\'
        if rem:
            s += '/'
            s += '-' * int(rem)
            s += '|\n'
        else:
            s += '\n'

        for i in range(3):
            for j in range(full_count):
                s += f'|{tmp}|'
            if tmp_last:
                s += f'|{tmp_last}|\n'
            else:
                s += '\n'
    
        for j in range(full_count):
            s += '\\'
            s += '-' * self.w
            s += '/'
        if rem:
            s += '\\'
            s += '-' * int(rem)
            s += '|'
            
        return s
    
    
    def __add__(self, other):
        return Sausage(self.meat, self.vol + other.vol)
    
    
    def __sub__(self, other):
        d = self.vol - other.vol
        if d < 0:
            d = 0
        return Sausage(self.meat, d)
    
    
    def __mul__(self, other):
        return Sausage(self.meat, self.vol * other)
    
    
    def __rmul__(self, other):
        return Sausage(self.meat, self.vol * other)
    
    
    def __truediv__(self, other):
        return Sausage(self.meat, self.vol / other)
    
    
    def __abs__(self):
        return self.vol
    
    
    def __bool__(self):
        if self.vol == 0:
            return False
        return True