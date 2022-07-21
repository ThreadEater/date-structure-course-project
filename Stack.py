class Stack:
    def __init__(self):
        self.data = []
        
    def push(self, val):
        self.data.append(val)

    def pop(self):
        assert not self.empty()
        ret = self.data[-1]
        del self.data[-1]
        return ret
    
    def peek(self):
        assert not self.empty()
        return self.data[-1]

    def empty(self):
        return len(self.data) == 0

    def __bool__(self):
        return not self.empty()