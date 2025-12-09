class Counter:
    def __init__(self, start=0):
        self.value = start
    def inc(self, n=None):
        if n == None:
            self.value += 1
        else:
            self.value += n
        return self.value
    
    def dec(self, n=None):
        if n == None:
            self.value -= 1
        else :
            self.value -= n
        if self.value < 0:
            self.value = 0
        return self.value 

class NonDecCounter(Counter):
    def __init__(self, start=0):
        super().__init__(start)
    
    def dec(self, n=None):
        pass

class LimitedCounter(Counter):
    def __init__(self, start=0,limit = 10):
        super().__init__(start)
        self.limit = limit
    
    def inc(self, n=None):
        if n == None:
            self.value += 1
        else:
            self.value += n
        if self.value > self.limit:
            self.value = self.limit 
        return self.value
    
c = Counter(5)
ndc = NonDecCounter(5)
lc = LimitedCounter(5, limit=10)

print("Counter:")
print(c.inc())       
print(c.inc(4))     
print(c.dec())       
print(c.dec(15))  
print(c.value)      

# Проверка NonDecCounter
print("NonDecCounter:")
print(ndc.inc())    
print(ndc.inc(3))   
print(ndc.dec())     
print(ndc.dec(10))   
print(ndc.value)     


print("LimitedCounter:")
print(lc.inc())      
print(lc.inc(3))     
print(lc.inc(5))     
print(lc.dec(2))    
print(lc.inc(5))     
print(lc.value)      