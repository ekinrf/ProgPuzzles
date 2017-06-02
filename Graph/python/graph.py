from collections import defaultdict, deque


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
        for endpoint in graph.ve[cur_vertex]:
            if endpoint not in visited:
                stack.append(cur_vertex)
                stack.append(endpoint)
                break


def bfs_graph(graph):
    visited = set()
    queue = deque()
    queue.append('A')
    while len(queue):
        cur_vertex = queue[0]
        if cur_vertex not in visited:
            visited.add(cur_vertex)
            visit(cur_vertex)
        has_unvisited = False
        for endpoint in graph.ve[cur_vertex]:
            if endpoint not in visited:
                has_unvisited = True
                visit(endpoint)
                visited.add(endpoint)
                queue.append(endpoint)
        if not has_unvisited:
            queue.popleft()


graph = GraphAdList(defaultdict(list, {'A': ['B', 'C', 'D'], 'B': ['F'], 'F': ['A'], 'C': ['H'], 'D' : ['G'], 'H': ['K']}))
#dfs_graph(graph)
#dfs_norec(graph)
bfs_graph(graph)