from tree import BinaryTreeNode


# one pass solution
def get_all_elem(root1: BinaryTreeNode, root2: BinaryTreeNode):
    stack1 = []
    stack2 = []

    cur_node1 = root1
    cur_node2 = root2

    res = []

    while cur_node1 or cur_node2 or stack1 or stack2:
        while cur_node1:
            stack1.append(cur_node1)
            cur_node1 = cur_node1.left

        while cur_node2:
            stack2.append(cur_node2)
            cur_node2 = cur_node2.left

        if not stack2 or (stack1 and stack1[-1].val < stack2[-1].val):
            visiting_node = stack1.pop()
            res.append(visiting_node.val)
            cur_node1 = visiting_node.right
        else:
            visiting_node = stack2.pop()
            res.append(visiting_node.val)
            cur_node2 = visiting_node.right

    return res
