from graph import GraphAdList
from collections import defaultdict
import heapq


def kruskal(graph):
    def find_root(e):
        if e not in mst:
            return e
        if mst[e] is e:
            return e
        else:
            return find_root(mst[e])

    def swap_parent(child, parent): # let child be the parent
        if child is not parent:
            grand_pa = mst[parent]
            mst[parent] = child
            swap_parent(parent, grand_pa)

    edges_dict = {}  # help for undirected graph
    edges = []
    for v in graph.ve:
        for e in graph.ve[v]:
            if (e[0], v) not in edges_dict:  # no need for checking (v, e[0])
                edges_dict[(v, e[0])] = e[1]
                edges.append((v, e[0], e[1]))
    edges.sort(key=lambda e: e[2])
    # using dict for tree, where each item keeps a reference to its direct parent
    mst = defaultdict(dict)
    for e in edges:
        p0 = find_root(e[0])
        p1 = find_root(e[1])

        # awkward and inefficient due to the mst data structure also used for union-find
        # should have used a separate tree structure for mst
        if p0 is not p1:
            if p0 is e[0] and p1 is e[1]:
                mst[e[0]] = e[1]
                mst[e[1]] = e[1]  # in case e[1] is not in the mst yet
            elif p1 is e[1]:
                mst[e[1]] = e[0]
            elif p0 is e[0]:
                mst[e[0]] = e[1]
            else:
                swap_parent(e[0], mst[e[0]])
                mst[e[0]] = e[1]

    return mst, edges_dict


def prim(graph):
    # not the best data structure for a tree
    # a dict where value is the direct parent of the key
    mst = defaultdict(dict)

    edges_from_tree = []
    current_node = next(iter(graph.ve))
    mst[current_node] = current_node
    tree_edges = {}
    done = False
    while not done:
        for (v, w) in graph.ve[current_node]:
            if v not in mst:
                heapq.heappush(edges_from_tree, (w, v))
        while edges_from_tree:
            edge_weight, next_node = heapq.heappop(edges_from_tree)
            if next_node not in mst:
                mst[next_node] = current_node
                tree_edges[(next_node, current_node)] = edge_weight
                current_node = next_node
                break
        done = not edges_from_tree # either finished or the graph is not connected
    return mst, tree_edges


def print_mst(graph, algo):
    mst, edges = algo(graph)
    print(mst)
    total_weight = 0
    for (v, p) in mst.items():
        if p is not v:
            if (v, p) in edges:
                total_weight += edges[(v, p)]
            else:
                total_weight += edges[(p, v)]
    print('total weight is {}'.format(total_weight))

if __name__ == '__main__':
    graph = GraphAdList(None, True)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 8, 2)
    graph.add_edge(2, 5, 4)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)

    graphB = GraphAdList(None, True)
    graphB.add_edge(0, 1, 10)
    graphB.add_edge(0, 2, 6)
    graphB.add_edge(0, 3, 5)
    graphB.add_edge(1, 3, 15)
    graphB.add_edge(2, 3, 4)

    print_mst(graph, kruskal)
    print_mst(graphB, kruskal)

    print_mst(graph, prim)
    print_mst(graphB, prim)
