class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def traverse_and_validate(cur, prev): #, visit_stack):
    if not cur:
        return True, prev
    # visit_stack.append(cur)
    if cur.left:
        valid, prev = traverse_and_validate(cur.left, prev) #, visit_stack):
        if not valid:
            return False, None

    # node = visit_stack.pop()
    if prev and not cur.val > prev.val:
        return False, None

    if cur.right:
        return traverse_and_validate(cur.right, cur)#, visit_stack)
    else:
        return True, cur


def validate_bst(root):
    valid, biggest = traverse_and_validate(root, None)
    return valid
