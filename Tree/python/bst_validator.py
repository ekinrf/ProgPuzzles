from tree import BinaryTreeNode


def traverse_and_validate(cur, prev):  # , visit_stack):
    if not cur:
        return True, prev
    # visit_stack.append(cur)
    if cur.left:
        valid, prev = traverse_and_validate(cur.left, prev)  # , visit_stack):
        if not valid:
            return False, None

    # node = visit_stack.pop()
    if prev and not cur.val > prev.val:
        return False, None

    if cur.right:
        return traverse_and_validate(cur.right, cur)  # , visit_stack)
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


def validate_bst_1(root: BinaryTreeNode):
    # validate a tree 'node' that all the elems are bigger than min and smaller than max
    def _validate_bst(node: BinaryTreeNode, min_node: BinaryTreeNode, max_node: BinaryTreeNode):
        if node:
            left_valid = False if min_node and min_node.val > node.val else True
            right_valid = False if max_node and max_node.val < node.val else True
            if left_valid and right_valid:
                return _validate_bst(node.left, min_node, node) \
                       and _validate_bst(node.right, node, max_node)
            else:
                return False
        else:
            return True

    return _validate_bst(root.left, None, root) & _validate_bst(root.right, root, None) # _valdate_bst(root, None, None)
