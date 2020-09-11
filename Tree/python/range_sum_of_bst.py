from tree import BinaryTreeNode


def range_sum_bst(root: BinaryTreeNode, l: int, r: int):
    def visit_and_sum(node: BinaryTreeNode):
        if not node:
            return 0
        if node.val < l:
            return visit_and_sum(node.right)
        elif l <= node.val <= r:
            return node.val + visit_and_sum(node.left) + visit_and_sum(node.right)
        elif node.val > r:
            return visit_and_sum(node.left)

    return visit_and_sum(root)