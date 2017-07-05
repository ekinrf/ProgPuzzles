from graph import GraphAdList
import heapq

# graph is an adjacent list
def shortest_path(ori, dst, graph):
    # def get_next_to_visit():
    #     unvisited = {v: w for v, w in shortest_to.items() if v not in visited}
    #     if unvisited:
    #         return min(unvisited, key=unvisited.get)
    #     else:
    #         return None

    shortest_to = {ori: 0}
    priority_queue = []
    queue_vertex_finder = set()
    heapq.heappush(priority_queue, (0, ori))
    queue_vertex_finder.add(ori)

    while len(priority_queue):
        cur_vertex = heapq.heappop(priority_queue)[1]
        if cur_vertex is dst:
            return shortest_to
        if cur_vertex in queue_vertex_finder:
            queue_vertex_finder.remove(cur_vertex)
            for (v1, w1) in graph.ve[cur_vertex]:
                if v1 not in shortest_to or w1 + shortest_to[cur_vertex] < shortest_to[v1]:
                    shortest_to[v1] = w1 + shortest_to[cur_vertex]
                    heapq.heappush(priority_queue, (shortest_to[v1], v1))
                    queue_vertex_finder.add(v1)
                    # cur_vertex = get_next_to_visit()
    print('Ori and Dst is not linked')
    return shortest_to


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
print(shortest_path(0, 6, graph))
