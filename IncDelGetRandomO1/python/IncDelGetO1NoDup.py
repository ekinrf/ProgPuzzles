import random


class IDGNoDup:

    def __init__(self):
        random.seed()
        self.dict = {}
        self.array = []
        self.size = 0

    def insert(self, elem):
        if elem not in self.dict:
            self.dict[elem] = self.size
            self.array.append(elem)
            self.size += 1
            return True
        else:
            return False

    def remove(self, elem):
        if elem in self.dict:
            pos, last = self.dict[elem], self.array[self.size - 1]
            # del(self.dict[elem]) cannot del here, imagine elem == last...
            self.array[pos], self.dict[last] = last, pos
            self.array.pop()
            del(self.dict[elem])
            self.size -= 1
            return True
        else:
            return False

    def get_random(self):
        if self.size:
            r = random.randint(0, self.size - 1)
            return self.array[r]
        else:
            raise LookupError()


randomSet = IDGNoDup()

randomSet.insert(1)

randomSet.remove(2)

randomSet.insert(2)

print(randomSet.get_random())

randomSet.remove(1)

randomSet.insert(2)

print(randomSet.get_random())