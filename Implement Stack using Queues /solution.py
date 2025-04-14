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
