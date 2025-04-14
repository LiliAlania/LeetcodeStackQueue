class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1
    def popleft(self):
        if self.is_empty():
            raise IndexError("pop_front from empty deque")
        value = self.front.value
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None
        self._size -= 1
        return value
class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
    def pop(self):
        """
        :rtype: int
        """
        return self.q1.popleft()
    def top(self):
        """
        :rtype: int
        """
        return self.q1[0]
    def empty(self):
        """
        :rtype: bool
        """
        return not self.q1
