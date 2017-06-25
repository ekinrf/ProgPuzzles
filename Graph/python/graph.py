from collections import defaultdict, deque


class GraphAdList:
    def __init__(self, ve=None, undirected = False):
        if ve:
            self.ve = ve
        else:
            self.ve = defaultdict(list)
        self.undirected = undirected

    def add_edge(self, start, end, weight):
        self.ve[start].append((end, weight))
        if self.undirected:
            self.ve[end].append((start, weight))


def visit(vertex):
    print(vertex)


def dfs_graph(graph):
    def depth_visit(vertex):
        visited.add(vertex)
        visit(vertex)
        for endpoint in graph.ve[vertex]:
            if endpoint not in visited:
                depth_visit(endpoint)
                # stack.pop()

    visited = set()
    depth_visit('A')


def dfs_norec(graph):
    visited = set()
    stack = ['A']
    while len(stack):
        cur_vertex = stack.pop()
        if cur_vertex not in visited:
            visited.add(cur_vertex)
            visit(cur_vertex)
        for edge in graph.ve[cur_vertex]:
            endpoint = edge[0]
            if endpoint not in visited:
                stack.append(cur_vertex)
                stack.append(endpoint)
                break


def bfs(graph):
    visited = set()
    queue = deque()
    queue.append('A')
    visited.add('A')
    while len(queue):
        cur_vertex = queue.popleft()
        visit(cur_vertex)
        visited.add(cur_vertex)
        for edge in graph.ve[cur_vertex]:
            endpoint = edge[0]
            if endpoint not in visited:
                queue.append(endpoint)


if __name__ == '__main__':
    graph = GraphAdList(defaultdict(list,
                                    {'A': [('B', 1), ('C', 1), ('D', 1)], 'B': [('F', 1)], 'F': [('A', 1)], 'C': [('H', 1)],
                                     'D': [('G', 1)], 'H': [('K', 1)]}))
    # dfs_graph(graph)
    # dfs_norec(graph)
    bfs(graph)
