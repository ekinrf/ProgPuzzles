from abc import ABCMeta, abstractmethod
from collections import defaultdict
import heapq


class CodeTree(metaclass=ABCMeta):
    def __init__(self):
        self._bit = ''
        self._weight = 0

    def __lt__(self, other):
        return self.weight < other.weight

    @property
    def bit(self):
        return self._bit

    @bit.setter
    def bit(self, bit):
        self._bit = bit

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, w):
        self._weight = w

    @abstractmethod
    def traverse(self, code, visit_fn):
        pass


class Fork(CodeTree):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.weight = left.weight + right.weight

    def __str__(self):
        return self.weight

    def traverse(self, code, visit_fn):
        self.left.traverse(code + str(self.bit), visit_fn)
        visit_fn(self, code + str(self.bit))
        self.right.traverse(code + str(self.bit), visit_fn)


class Leaf(CodeTree):
    def __init__(self, char, weight):
        super().__init__()
        self.char = char
        self.weight = weight

    def __str__(self):
        return self.weight, self.char

    def traverse(self, code, visit_fn):
        visit_fn(self, code + str(self.bit))


def huffman_code_tree(freq_table):
    def freq_table_to_leaves():
        return [Leaf(c, f) for (c, f) in freq_table.items()]

    leaves = freq_table_to_leaves()
    heapq.heapify(leaves)
    while len(leaves) > 1:
        left = heapq.heappop(leaves)
        left.bit = 0
        right = heapq.heappop(leaves)
        right.bit = 1
        heapq.heappush(leaves, Fork(left, right))
    return leaves[0]


def gen_freq_table(text):
    table = defaultdict(int)
    for c in text:
        table[c] += 1
    return table


def print_code(leaf_node, code):
    if hasattr(leaf_node, 'char'):
        print(leaf_node.char, code)

if __name__ == '__main__':
    table = gen_freq_table('this is an example of a huffman tree')
    code_tree = huffman_code_tree(table)
    code_tree.traverse('', print_code)