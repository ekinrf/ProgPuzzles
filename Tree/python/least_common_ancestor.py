from tree import BinaryTreeNode


# assumption n1 and n2 exists in the tree
# either n1 or n2 is a root of the other
# or they are on different branch
def lca(root, n1, n2):
    if not root:
        return root
    if root == n1 or root == n2:
        return root
    left = lca(root, n1, n2)
    right = lca(root, n1, n2)

    if left and right:
        return root
    if not left and not right:
        return left  # null
    if left:
        return left
    else:
        return right
