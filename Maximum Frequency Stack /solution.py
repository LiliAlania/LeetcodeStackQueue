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
    def pop(self):
        """
        :rtype: int
        """
        el_dict = {}
        len_ = 0
        max_el = None
        for element in self.elements:
            len_ += 1
            if element not in el_dict.keys():
                el_dict[element] = [0, len_]
            else:
                el_dict[element] += [1, len_]
        max_fr = max(el_dict.values()[0])
        for el in el_dict.keys():
            if el_dict[el][0] == max_fr:
                if max_el:
                    if el_dict[el][1] < el_dict[max_el][0]:
                        max_el = el
                else:
                    max_el = el
        return self.element.pop(max_el)
