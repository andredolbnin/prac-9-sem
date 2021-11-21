def sizer(c):
    class new_c(c):
        def __init__(self, *args, **kwargs):
            try:
                super().__init__(*args, **kwargs)
            except:
                pass
            
            if hasattr(self, '__len__'):
                self.size = len(self)
            elif hasattr(self, '__abs__'):
                self.size = abs(self)
            else:
                self.size = 0
                
    return new_c