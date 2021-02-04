class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxIndeces = []
        self.length = 0

    def push(self, val):
        self.stack.append(val)
        self.length+=1
        if (self.length ==1 or val>self.stack[self.maxIndeces[-1]]):
            self.maxIndeces.append(self.length-1)

    def pop(self):
        if (self.length):
            popped =  self.stack.pop()
            self.length-=1
            if (self.length==self.maxIndeces[-1]):
                self.maxIndeces.pop()
            return popped
        else:
            raise Exception("Cannot pop an empty stack")

    def max(self):
        if (self.maxIndeces):
            return self.stack[self.maxIndeces[-1]]

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)


print (s.stack[-1])
s.pop()

print (s.stack[-1])
s.pop()

print (s.stack[-1])
s.pop()

print (s.stack[-1])
s.pop()

print (s.max())
s.pop

# 2
