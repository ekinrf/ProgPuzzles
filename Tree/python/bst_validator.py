from collections import deque


class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


def traverse_and_validate(cur, prev): #, visit_stack):
    if not cur:
        return True, prev
    # visit_stack.append(cur)
    if cur.left:
        valid, prev = traverse_and_validate(cur.left, prev) #, visit_stack):
        if not valid:
            return False, None

    # node = visit_stack.pop()
    if prev and not cur.val > prev.val:
        return False, None

    if cur.right:
        return traverse_and_validate(cur.right, cur)#, visit_stack)
    else:
        return True, cur


def validate_bst(root):
    valid, biggest = traverse_and_validate(root, None)
    return valid


def bottom_right(root):
    if root.right:
        return bottom_right(root.right)
    else:
        return root


def bottom_left(root):
    if root.left:
        return bottom_left(root.left)
    else:
        return root


def validate_bst_rec(root):
    if root is None:
        return True
    if validate_bst_rec(root.left) and validate_bst_rec(root.right):
        if root.left and bottom_right(root.left).val >= root.val:
            return False
        if root.right and bottom_left(root.right).val <= root.val:
            return False
        return True
    else:
        return False