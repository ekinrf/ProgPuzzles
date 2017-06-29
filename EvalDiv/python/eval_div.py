# path finding in a graph

from collections import defaultdict


# the floyd warshall algorithm
# unlike floyd-warshall who finds a shortest path,
# this simply finds a path
def eval_div(equations, values, queries):
    eq_graph = defaultdict(dict)
    for (dividend, divisor), value in zip(equations, values):
        eq_graph[dividend][divisor] = value
        eq_graph[divisor][dividend] = 1 / value
        eq_graph[dividend][dividend] = eq_graph[divisor][divisor] = 1
    for k in eq_graph:
        for i in eq_graph[k]:
            for j in eq_graph[k]:
                eq_graph[i][j] = eq_graph[i][k] * eq_graph[k][j]

    for dividend, divisor in queries:
        yield eq_graph[dividend].get(divisor, -1.0)


# an union-find solution
# find if dividend and divisor are in the same set
# close to O(n) depends on the find_root function
# optimise by compact and put a smaller tree under bigger tree when union
def eval_div_union(equations, values, queries):
    # compaction can be done here
    def find_root(vtx, weight):
        parent, weight = union_find_tree[vtx][0], union_find_tree[vtx][1] * weight
        if parent is vtx:
            return vtx, weight
        else:
            return find_root(parent, weight)

    union_find_tree = {}
    for (dividend, divisor), value in zip(equations, values):
        # both vtx not in the set yet, choose one to a root
        if dividend not in union_find_tree and divisor not in union_find_tree:
            union_find_tree[dividend] = (dividend, 1)
            union_find_tree[divisor] = (dividend, value)
        elif dividend not in union_find_tree:
            union_find_tree[dividend] = (divisor, 1 / value)
        elif divisor not in union_find_tree:
            union_find_tree[divisor] = (dividend, value)
        else:  # both are in the set, try to perform an union
            dividend_root, dividend_root_weight = find_root(dividend, 1)
            divisor_root, divisor_root_weight = find_root(divisor, 1)
            if divisor_root is not dividend_root:  # not connected
                # who wants be root? traditional union find would decide by comparing the depth of each tree
                union_find_tree[divisor_root] = (dividend_root, value * dividend_root_weight / divisor_root_weight)
    for dividend, divisor in queries:
        if divisor not in union_find_tree or dividend not in union_find_tree:
            yield -1.0
        else:
            dividend_root, dividend_root_weight = find_root(dividend, 1)
            divisor_root, divisor_root_weight = find_root(divisor, 1)
            if divisor_root is not dividend_root:
                yield -1.0
            else:
                yield divisor_root_weight / dividend_root_weight


if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

    eq1 = [["a", "b"], ["e", "f"], ["b", "e"]]
    v1 = [3.4, 1.4, 2.3]
    q1 = [["b", "a"], ["a", "f"], ["f", "f"], ["e", "e"], ["c", "c"], ["a", "c"], ["f", "e"]]

    print(list(eval_div(equations, values, queries)))
    print(list(eval_div_union(equations, values, queries)))
    print(list(eval_div(eq1, v1, q1)))
    print(list(eval_div_union(eq1, v1, q1)))
