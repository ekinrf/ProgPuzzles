# how to implement the algo with adjacent list?

INF = 1000000

graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]]


def shortest_paths(graph):
    num_vertices = len(graph)
    # deep copy
    res = [[graph[i][j] for j in range(num_vertices)] for i in range(num_vertices)]

    for k in range(1, num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                res[i][j] = min(res[i][k] + res[k][j], res[i][j])

    return res

print(shortest_paths(graph))
