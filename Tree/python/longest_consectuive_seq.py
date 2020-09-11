from tree import BinaryTreeNode, list_to_btree


# top down approach, but b/c we start from root and back tracking, so still O(n) without memo
def longest_consecutive_seq(root: BinaryTreeNode):
    def longest_from_node(node: BinaryTreeNode, cur_max):
        subtree_seq = 0
        if node.left:
            cur_max, from_left = longest_from_node(node.left, cur_max)
            if node.val == node.left.val - 1:
                subtree_seq = from_left
        if node.right:
            cur_max, from_right = longest_from_node(node.right, cur_max)
            if node.val == node.right.val - 1:
                subtree_seq = max(subtree_seq, from_right)

        cur_max = max(cur_max, subtree_seq + 1)
        return cur_max, subtree_seq + 1

    max_seq, _ = longest_from_node(root, 0)
    return max_seq


# bottom up
def longest_seq_v2(root: BinaryTreeNode):
    def max_seq_from_node(node: BinaryTreeNode, cur_len, last_node_val):
        if not node:
            return cur_len
        if last_node_val + 1 == node.val:
            cur_len += 1
        else:
            cur_len = 1
        left_seq = max_seq_from_node(node.left, cur_len, node.val)
        right_seq = max_seq_from_node(node.right, cur_len, node.val)
        print('-')
        return max(cur_len, left_seq, right_seq)
    return max_seq_from_node(root, 0, root.val)


t = list_to_btree([1, None, 3, 2, 4, None, None, None, 5])
print(longest_consecutive_seq(t))
print(longest_seq_v2(t))


t = list_to_btree([2, None, 3, 2, None, 1, None])
print(longest_consecutive_seq(t))
print(longest_seq_v2(t))
