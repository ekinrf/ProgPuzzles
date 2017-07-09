from bst_validator import bfs_list_to_binary_tree


def del_bst_node(root, tar_key):
    def merge(left, right):
        if right:
            find_leaf(right, True).left = left
            return right
        elif left:
            find_leaf(left, False).right = right
            return left

    def find_key_and_del(cur_node, parent):
        if not cur_node:
            return False
        elif cur_node.val < tar_key:
            if cur_node.right:
                next_node = cur_node.right
                if next_node.val == tar_key:
                    cur_node.right = None
                    cur_node.right = merge(next_node.left, next_node.right)
                    return True
            else:
                return False, cur_node, parent
        else:  # >tar_key
            if cur_node.left:
                next_node = cur_node.left
                if next_node.val == tar_key:
                    cur_node.left = None
                    cur_node.left = merge(next_node.left, next_node.right)
                    return True
            else:
                return False
        return find_key_and_del(next_node, cur_node)

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
            find_key_and_del(root, None)
    return root


if __name__ == '__main__':
    tree = bfs_list_to_binary_tree([5, 3, 6, 2, 4, None, 7])
    print(del_bst_node(tree, 3))
