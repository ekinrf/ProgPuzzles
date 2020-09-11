from tree import BinaryTreeNode


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# find mid and then recursively build up the tree
# or convert the list to array to make it more efficient in find the mid
# However, a more clever solution is to simulate in order traversal
# the start of list is always the left most child of the tree;
# and its parent is the root;
# and next one, depends on how big the sub tree is (sub tree will need to be half size of the list),
# a right child or the root of a root
def sorted_list_to_bst(l_node: ListNode):
    def _build_tree(s, e):
        if e < s:
            return None
        nonlocal l_node
        mid = s + (e - s) // 2
        left = _build_tree(s, mid - 1)
        root = BinaryTreeNode(l_node.val)
        root.left = left
        l_node = l_node.next
        root.right = _build_tree(mid + 1, e)
        return root

    if not l_node:
        return None
    end = 0
    temp = l_node
    while temp.next:
        temp = temp.next
        end += 1
    return _build_tree(0, end)


def sorted_list_to_bst_arr(l_node: ListNode):
    def _build_tree(arr):
        if not arr:
            return None
        mid = (0 + len(arr)) // 2
        root = BinaryTreeNode(arr[mid])
        root.left = _build_tree(arr[0:mid - 1])
        root.right = _build_tree(arr[mid + 1: len(arr)])
        return root

    arr = [l_node.val]
    while l_node.next:
        l_node = l_node.next
        arr.append(l_node.val)
    return _build_tree(arr)