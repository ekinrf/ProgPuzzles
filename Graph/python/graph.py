from collections import defaultdict


class GraphAdList:
    def __init__(self, ve=None):
        if ve:
            self.ve = ve
        else:
            self.ve = defaultdict(list)

    def add_edge(self, start, end):
        self.ve[start].append(end)


def visit(vertex):
    print(vertex)


def dps_graph(graph):
    def depth_visit(vertex):
        visited.add(vertex)
        visit(vertex)
        for endpoint in graph.ve[vertex]:
            if endpoint not in visited:
                depth_visit(endpoint)
        # stack.pop()

    visited = set()
    depth_visit('A')


def dps_norec(graph):
    visited = set()
    stack = ['A']
    while len(stack):
        cur_vertex = stack.pop()
        if cur_vertex not in visited:
            visited.add(cur_vertex)
            visit(cur_vertex)
            for endpoint in graph.ve[cur_vertex]:
                if endpoint not in visited:
                    stack.append(endpoint)


graph = GraphAdList(defaultdict(list, {'A': ['B', 'C', 'D'], 'B': ['F'], 'F': ['A'], 'C': ['B'], 'D' : ['C']}))
# dps_graph(graph)
dps_norec(graph)