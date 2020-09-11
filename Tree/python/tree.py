from collections import deque


class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left: BinaryTreeNode = None
        self.right: BinaryTreeNode = None

    def height(self):
        left_h = right_h = 0
        if self.left:
            left_h = self.left.height() + 1
        if self.right:
            right_h = self.right.height() + 1
        return max(1, left_h, right_h)

    def visualise(self):
        import turtle

        def jump_to(x, y):
            t.penup()
            t.goto(x, y)
            t.pendown()

        def draw(node, x, y, dx):
            if node:
                t.goto(x, y)
                jump_to(x, y - 20)
                t.write(node.val, align='center', font=('Arial', 12, 'normal'))
                draw(node.left, x - dx, y - 40, dx / 2)
                jump_to(x, y - 20)
                draw(node.right, x + dx, y - 40, dx / 2)

        h = self.height()
        t = turtle.Turtle()
        jump_to(0, 40 * h)
        draw(self, 0, 40 * h, h * 40)

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


def serialize(root) -> str:
    nodes = deque([root])
    res = []
    while nodes:
        node = nodes.popleft()
        res.append(node)
        if node:
            nodes.append(node.left)
            nodes.append(node.right)
    return ' '.join([n.val if n else None for n in res])


def deserialize(data: str):
    nodes = deque(BinaryTreeNode(node_str) if node_str != 'None' else None for node_str in data.split(' '))
    root = nodes.popleft()
    children_queue = deque([root])
    while nodes:
        node = children_queue.popleft()
        if nodes: # add left
            node.left = nodes.popleft()
            if node.left:
                children_queue.append(node.left)
        if nodes:
            node.right = nodes.popleft()
            if node.right:
                children_queue.append(node.right)
    return root



def print_bt_root_to_leaf_path(root):
    def _print_rec(node, path):
        path.append(node.val)
        if not node:
            return
        elif node.left or node.right:
            if node.left:
                _print_rec(node.left, path)
                path.pop()
            if node.right:
                _print_rec(node.right, path)
                # path.pop()
        else:
            print(path)

    _print_rec(root, [])


if __name__ == '__main__':
    c = list_to_btree([4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5,
                       None, 9, None, None, -1, -4, None, None, None, -2])
    print(c.height())
    print(btree_to_list(c))
    c.visualise()

    print_bt_root_to_leaf_path(c)
