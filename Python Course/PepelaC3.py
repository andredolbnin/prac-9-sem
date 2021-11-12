b = ''
e = 'class Pepelac('
while True:
    inp = input()
    l = inp.split()
    
    if len(l[0]) > 1:
        for item in l[0]:
            e += f'{item},'
        e += '):\n'
        
        if len(l) == 3:
            for item in l[1]:
                e += f'    def {item}(self): pass\n'
      
            e += '\n\n'
        
            e += 'pep = Pepelac()\n'
            for item in l[2]:
                e += f'pep.{item}()\n'
        else:
            e += '    pass'
            
            e += '\n\n'
            e += 'pep = Pepelac()\n'
            for item in l[1]:
                e += f'pep.{item}\n'
        
        break
    
    b += f'class {l[0]}('
    if len(l) == 1: 
        b += '): pass\n'
        continue

    if l[1][0].isupper():
        for item in l[1]:
            b += f'{item},'
        b += '):\n'
        if len(l) == 3:
            for item in l[2]:
                b += f'    def {item}(self): pass\n'
        else:
            b += '    pass\n'
    else:
        b += '):\n'
        if len(l) == 2:
            for item in l[1]:
                b += f'    def {item}(self): pass\n'
                         
param = b + e

try:
    exec(param)
except (TypeError, AttributeError, NameError):
    print('Incorrect')
else:
    print('Correct')