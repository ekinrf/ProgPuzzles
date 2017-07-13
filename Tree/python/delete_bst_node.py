from tree import bfs_list_to_binary_tree


def del_bst_node(root, tar_key):
    def merge(left, right):
        if right:
            find_leaf(right, True).left = left
            return right
        elif left:
            find_leaf(left, False).right = right
            return left

    def find_leaf(node, left):
        if left:
            subtree = node.left
        else:
            subtree = node.right

        if subtree:
            return find_leaf(subtree, left)
        else:
            return node

    if root:
        if root.val == tar_key:
            return merge(root.left, root.right)
        else:
            if root.val < tar_key:
                root.right = del_bst_node(root.right, tar_key)
            else:
                root.left = del_bst_node(root.left, tar_key)
    return root


if __name__ == '__main__':
    tree = bfs_list_to_binary_tree([5, 3, 6, 2, 4, None, 7])
    # tree.visualise()
    tree = del_bst_node(tree, 3)
    tree.visualise()
