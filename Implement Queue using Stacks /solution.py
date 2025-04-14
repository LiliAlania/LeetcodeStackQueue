from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
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
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.push(x)
    def pop(self):
        """
        :rtype: int
        """
        self._move_in_to_out()
        return self.stack_out.pop()
    def peek(self):
        """
        :rtype: int
        """
        self._move_in_to_out()
        return self.stack_out.peek()
    def empty(self):
        """
        :rtype: bool
        """
        return self.stack_in.is_empty() and self.stack_out.is_empty()
    def _move_in_to_out(self):
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
