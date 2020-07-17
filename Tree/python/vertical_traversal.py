import heapq
from collections import deque

from tree import BinaryTreeNode


# left is x - 1, y - 1, right is x + 1, y - 1
# we reverse y to make heap sort it so y becomes y + 1
def vertical_traversal(root: BinaryTreeNode):
    node_values = []
    to_visit = deque([])
    to_visit.append((root, 0, 0))
    while to_visit:
        node, x, y = to_visit.pop()
        heapq.heappush(node_values, (x, y, node.val))
        if node.left:
            to_visit.append((node.left, x - 1, y + 1))
        if node.right:
            to_visit.append((node.right, x + 1, y + 1))
    res = []
    prev_x = None
    while node_values:
        x, y, val = heapq.heappop(node_values)
        if prev_x == x:
            res[-1].append(val)
        else:
            res.append([val])
        prev_x = x
    return res

