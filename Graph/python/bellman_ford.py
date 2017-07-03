from graph import GraphAdList


def bellman_ford(ori, dst, graph):
    distance = {ori: 0}
    # will have duplicates for undirected graph
    # because both edges would included
    # however does not affect the results just make the time complexity doubled
    edges = [(v, u, w) for v in graph.ve for (u, w) in graph.ve[v]]
    for u, v, w in edges:
        if u in distance:
            if v in distance:
                distance[v] = min(distance[v], distance[u] + w)
            else:
                distance[v] = distance[u] + w

    # one more iteration for negative cycle detection
    for u, v, w in edges:
        if u in distance:
            if distance[v] > distance[u] + w:
                print('negative cycle between {} and {}. Result is not valid'.format(ori, v))
        else:
            print('{} not connected to {}'.format(ori, u))

    return distance  #distance[dst]


graph = GraphAdList(None)
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
print(bellman_ford(0, 3, graph))
