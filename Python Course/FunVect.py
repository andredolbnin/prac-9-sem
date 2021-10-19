def superposition(funmod, funsec):
    
    results = []
    
    def mod(x):
        return funmod(x)
    
    for i in range(len(funsec)):
        def result(x, j = i):
            return mod(funsec[j](x))
        results.append(result)
    
    return results