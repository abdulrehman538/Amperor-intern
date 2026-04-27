class Stack:

    def __init__(self):
        self.stack = []  

    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if len(self.stack) == 0:
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if len(self.stack) == 0:
            return "Stack is empty"
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
class Queue:
    
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return "Queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if len(self.queue) == 0:
            return "Queue is empty"
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
    


d = Stack()
d.push(1)       
d.push(2)
d.push(3)
print(d.is_empty())
print(d.size())
print(d.peek())
print(d.pop())
print(d.pop())
print(d.is_empty())

q = Queue()
q.enqueue(1)            
q.enqueue(2)
q.enqueue(3)
print(q.is_empty())
print(q.size())
print(q.peek())
print(q.dequeue())
print(q.dequeue())
print(q.is_empty())
