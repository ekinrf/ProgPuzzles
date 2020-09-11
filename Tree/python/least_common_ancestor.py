from tree import BinaryTreeNode


# p and q exists in the tree
# All of the nodes' values will be unique.
# 1) one of the p and q is the lca of another, so when visit, they are on the same branch
# 2) they share a different one, so one is on left and the other is one right branch
# and the root of the sub tree is the lca
# so, we return whenever find the a p or q,
# and then search the branch, if found another p or q, then the root is the lcs
# or p or q found is the lcs
def lca(root: BinaryTreeNode, p: BinaryTreeNode, q: BinaryTreeNode):
    if not root:
        return False
    if root.val == p.val or root.val == q.val:
        return root
    potential_lca_from_left = lca(root.left, p, q)
    potential_lca_from_right = lca(root.right, p, q)
    if potential_lca_from_left and potential_lca_from_right:
        return root
    else:
        return potential_lca_from_left if potential_lca_from_left else potential_lca_from_right


# A recursive solution with early termination
# recursively find number of targets in the subtree
# and terminate when the number reaches reaches 2
def lca1(root: BinaryTreeNode, p: BinaryTreeNode, q: BinaryTreeNode):
    def _lca(node: BinaryTreeNode):
        if not node:
            return 0, None
        target_found = 1 if node.val == p.val or node.val == q.val else 0
        from_left, potential_lca = _lca(node.left)
        if potential_lca:
            return 2, potential_lca
        target_found += from_left
        if target_found == 2:
            return 2, node
        from_right, potential_lca = _lca(node.right)
        if potential_lca:
            return 2, potential_lca
        target_found += from_right
        if target_found == 2:
            return 2, node
        return target_found, None

    return _lca(root)[1]


# find parents of the each node
# build a set of p parents
# traverse q parents and return the first match
def lca2(root: BinaryTreeNode, p: BinaryTreeNode, q: BinaryTreeNode):
    def dfs(node):
        if node.left:
            parent[node.left] = node
            dfs(node.left)
        if node.right:
            parent[node.right] = node
            dfs(node.right)

    parent = {root: None}
    dfs(root)
    p_parents = set()
    while p:
        p_parents.add(p)
        p = parent[p]

    while q not in p_parents:
        q = parent[q]
    return q
