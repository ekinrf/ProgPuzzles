import random
import collections


class IDGDup:
    def __init__(self):
        random.seed()
        self.elem_to_idx = collections.defaultdict(set)
        self.elems = []
        self.size = 0

    def insert(self, elem):
        self.size += 1
        self.elems.append(elem)
        self.elem_to_idx[elem].add(self.size - 1)
        return len(self.elem_to_idx[elem]) != 1

    def remove(self, elem):
        if self.elem_to_idx[elem]:
            idx, last = self.elem_to_idx[elem].pop(), self.elems[self.size - 1]
            self.elems[idx] = last
            if self.elem_to_idx[last]:
                self.elem_to_idx[last].add(idx)
                self.elem_to_idx[last].remove(self.size - 1)
            self.elems.pop()
            self.size -= 1
            return True
        else:
            return False

    def get_random(self):
        if self.size:
            return self.elems[random.randint(0, self.size - 1)]
        else:
            raise KeyError


randomSet = IDGDup()

randomSet.insert(9)

randomSet.insert(9)

randomSet.insert(1)

randomSet.insert(1)

randomSet.insert(2)

randomSet.insert(1)

randomSet.remove(2)

randomSet.remove(1)

randomSet.remove(1)

randomSet.insert(9)

randomSet.remove(1)

print(randomSet.get_random())

# randomSet.remove(1)

# randomSet.insert(2)
# randomSet.insert(2)
# randomSet.insert(2)

print(randomSet.get_random())
