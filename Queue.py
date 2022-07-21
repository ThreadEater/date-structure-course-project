class Queue:
    def __init__(self, limit=10):
        self.data = [None] * limit
        self.head = -1
        self.tail = -1

    def full(self):
        if (self.head+1)%len(self.data)==self.tail:
            return True
        else:
            return False
        
    def enqueue(self, val): # O(1)
        if self.empty():
            self.head=0
            self.tail=0
            self.data[0]=val
        else:
            if (self.head+1)%len(self.data)==self.tail:
                raise RuntimeError()
            else:
                self.head= (self.head + 1) % len(self.data)
                self.data[self.head] = val
                
    def peek(self):
        return self.data[self.head]
                
    def dequeue(self): # O(1)
        if self.empty():
            raise RuntimeError()
        ret = self.data[self.tail]
        self.data[self.tail] = None
        self.tail = (self.tail + 1) % len(self.data)
        if (self.head+1)%len(self.data)==self.tail:
            self.tail=self.head=-1
        return ret
    
    def resize(self, newsize):
        assert(len(self.data) < newsize)
        newq=Queue(newsize)
        for i in self:
            newq.enqueue(i)
        self.data=newq.data
        self.head=newq.head
        self.tail=newq.tail
        
    def empty(self):
        if self.head==self.tail==-1:
            return True
        return False
    
    def __bool__(self):
        return not self.empty()
    
    def __str__(self):
        if not(self):
            return ''
        return ', '.join(str(x) for x in self)
    
    def __repr__(self):
        return str(self)
    
    def __iter__(self):
        head=(self.head+len(self.data))%len(self.data)
        tail=(self.tail+len(self.data))%len(self.data)
        i=tail
        while (i!=head):
            yield self.data[i]
            i=(i+1)%len(self.data)
        else:
            yield (self.data[head])