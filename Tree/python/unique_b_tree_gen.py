# https://leetcode.com/problems/unique-binary-search-trees-ii/
from itertools import product

from tree import BinaryTreeNode


# pick a k as the root
# then 1...k-1 is the left tree
# k + 1 ... n is the right tree
def gen_trees(n: int):

    def _gen_trees(s, e):
        ret = []
        if s > e:
            ret.append(None)
        for idx in range(s, e + 1):
            left_trees = _gen_trees(s, idx - 1)
            right_trees = _gen_trees(idx + 1, e)

            for l, r in product(left_trees, right_trees):
                root = BinaryTreeNode(idx)
                root.left = l
                root.right = r
                ret.append(root)
        return ret
    return _gen_trees(1, n)


