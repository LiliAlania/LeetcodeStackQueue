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
