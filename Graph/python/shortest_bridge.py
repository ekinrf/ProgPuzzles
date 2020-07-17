from collections import deque
from typing import List

from python.large_island import neighbours


def shortest_bridge(graph: List[List[int]]):
    def dfs_visit(x, y):
        graph[x][y] = 2
        for x_n, y_n in neighbours(x, y, x_len, y_len):
            if graph[x_n][y_n] == 1:
                dfs_visit(x_n, y_n)
            elif graph[x_n][y_n] == 0:
                graph[x_n][y_n] = -1
                boundary.append((x_n, y_n, 1))

    x_len, y_len = len(graph), len(graph[0])
    boundary = deque([])

    # Find the first island, mark all with 2
    # also mark its boundary along the way using -1
    for x, y in ((n1, n2) for n1 in range(x_len) for n2 in range(y_len)):
        if graph[x][y] == 1:
            dfs_visit(x, y)
            break

    min_0_needed = 1

    while boundary:
        x, y, min_0_needed = boundary.popleft()
        for x_n, y_n in neighbours(x, y, x_len, y_len):
            if graph[x_n][y_n] == 1:
                return min_0_needed
            elif graph[x_n][y_n] == 0:
                boundary.append((x_n, y_n, min_0_needed + 1))
                graph[x_n][y_n] = -1

    return min_0_needed


print(shortest_bridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]))
print(shortest_bridge([[0,1,0],[0,0,0],[0,0,1]]))

print(shortest_bridge([[1,1,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))

print(shortest_bridge([[1,0,1,1,1,0],[0,1,1,1,0,0],[1,1,1,0,0,0],[0,1,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]))