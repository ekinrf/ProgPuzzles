from collections import deque
import turtle

class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def height(self):
        left_h = right_h = 0
        if self.left:
            left_h = self.left.height() + 1
        if self.right:
            right_h = self.right.height() + 1
        return max(1, left_h, right_h)

    def visualise(self):
        height = self.height()
        t = turtle.Turtle()
        t.write(self.val, align="center")
        t.goto(45, -20)
        t.hideturtle()
        turtle.done()


def bfs_list_to_binary_tree(nodes):
    if nodes and nodes[0]:
        queue = deque()
        root = BinaryTreeNode(nodes[0])
        queue.append(root)
        idx = 1
        while idx < len(nodes):
            node = queue.popleft()
            children_visited = 0
            while children_visited < 2 and idx < len(nodes):
                if nodes[idx] is not None:
                    child = BinaryTreeNode(nodes[idx])
                    queue.append(child)
                    if not children_visited:
                        node.left = child
                    else:
                        node.right = child
                children_visited += 1
                idx += 1
        return root
    else:
        return None


def list_to_btree(nodes):
    tree_nodes = [None if val is None else BinaryTreeNode(val) for val in nodes]
    children = tree_nodes[::-1]
    root = children.pop()
    for node in tree_nodes:
        if node:
            if children:
                node.left = children.pop()
            if children:
                node.right = children.pop()

    return root


def btree_to_list(root):
    nodes = [root]
    for node in nodes:
        if node:
            nodes.append(node.left)
            nodes.append(node.right)

    return [None if node is None else node.val for node in nodes]


if __name__ == '__main__':
    c = list_to_btree([4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5,
                       None, 9, None, None, -1, -4, None, None, None, -2])
    print(c.height())
    print(btree_to_list(c))
    c.visualise()