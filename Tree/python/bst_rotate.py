from tree import BinaryTreeNode


def left_rotate(node: BinaryTreeNode):
    right = node.right
    if right:
        node.right = right.left
        right.left = node
        return right
    return node


def right_rotate(node: BinaryTreeNode):
    left = node.left
    if left:
        node.left = left.right
        left.right = node
        return left
    return node




