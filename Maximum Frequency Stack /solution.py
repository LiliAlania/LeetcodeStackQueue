from collections import deque, defaultdict
class FreqStack(object):
    def __init__(self):
        self.elements = deque()
        self.freq = defaultdict(int)
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.elements.append(val)
        self.freq[val] += 1
    def pop(self):
        """
        :rtype: int
        """
        max_freq = max(self.freq.values())
        for i in range(len(self.elements) - 1, -1, -1):
            val = self.elements[i]
            if self.freq[val] == max_freq:
                del self.elements[i]
                self.freq[val] -= 1
                if self.freq[val] == 0:
                    del self.freq[val]
                return val
