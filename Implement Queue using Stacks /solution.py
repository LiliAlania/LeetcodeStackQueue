class Stack:
    def __init__(self):
        self.container = []
    def push(self, x):
        self.container.append(x)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)
class MyQueue(object):
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()
