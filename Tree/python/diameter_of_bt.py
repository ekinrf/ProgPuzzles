from tree import list_to_btree


# max of the all sub trees: (left depth + right depth)
def diameter_of_binary_tree(tree):
    def weight_and_max_diameter(tree, max_diameter):
        left_depth = right_depth = 0
        if tree.left:
            left_depth, max_diameter = weight_and_max_diameter(tree.left, max_diameter)
            left_depth += 1
        if tree.right:
            right_depth, max_diameter = weight_and_max_diameter(tree.right, max_diameter)
            right_depth += 1
        diameter = left_depth + right_depth
        if diameter > max_diameter:
            max_diameter = diameter
        return max(left_depth, right_depth), max_diameter

    max_diameter = 0
    if tree:
        weight, max_diameter = weight_and_max_diameter(tree, 0)
    return max_diameter


if __name__ == '__main__':
    a = list_to_btree([3, 1, None, None, 2])
    print(diameter_of_binary_tree(a))

    b = list_to_btree([1, 2, 3, 4, 5])
    print(diameter_of_binary_tree(b))

    c = list_to_btree([4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5,
                       None, 9, None, None, -1, -4, None, None, None, -2])
    print(diameter_of_binary_tree(c))
