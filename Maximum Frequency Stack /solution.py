from collections import deque
class FreqStack(object):
    def __init__(self):
        self.elements = deque()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.elements.append(val)
