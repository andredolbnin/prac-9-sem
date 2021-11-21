from collections import deque

class Lock:
    busy = {}
    sems = {}
    
    def __init__(self, par):
        self.par = par
        self._lock = None
        
        self.sem = None


    def __str__(self):
        return str(self.par)
        
    
    @property
    def lock(self):
        if self.sem not in Lock.busy:
            for k, v in Lock.sems.items():
                if self.par in v:
                    self._lock = self.sem
                    Lock.busy[self.sem] = self.par
        elif self.par == Lock.busy[self.sem]:
            pass
        else:
            self._lock = None
        #print(Lock.sems, Lock.busy)
        return self._lock
    
    
    @lock.setter
    def lock(self, value):
        tmp = Lock.busy.items()
        for k, v in tmp:
            if self.par == v:
                del Lock.busy[k]
                break
        for k, v in Lock.sems.items():
            if self.par in v:
                Lock.sems[k].remove(self.par)
                break
        self.sem = value
        try:
            Lock.sems[value].append(self.par)
        except:
            Lock.sems[value] = deque([self.par])
        #print(Lock.sems, Lock.busy)
        
        
    @lock.deleter
    def lock(self):
        tmp = Lock.busy.items()
        for k, v in tmp:
            if self.par == v:
                del Lock.busy[k]
                break
        for k, v in Lock.sems.items():
            if v:
                if self.par == v[0]:
                    Lock.sems[k].popleft()
            
        
    def __del__(self):
        tmp = Lock.busy.items()
        for k, v in tmp:
            if self.par == v:
                del Lock.busy[k]
                break
        for k, v in Lock.sems.items():
            if self.par in v:
                Lock.sems[k].remove(self.par)
                
                
    def locked(self):
        class locked_class(Lock):
            pass
        return locked_class