from tree import BinaryTreeNode


def insert_bst(root: BinaryTreeNode, ins_node: BinaryTreeNode):
    if not root:
        return ins_node
    if ins_node.val == root.val:
        ori_left = root.left
        root.left = ins_node
        ins_node.left = ori_left
        return root
    elif ins_node.val > root.val:
        insert_bst(root.right, ins_node)
    else:
        insert_bst(root.left, ins_node)