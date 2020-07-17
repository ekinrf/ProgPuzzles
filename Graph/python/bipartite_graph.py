from collections import deque
from typing import List


# exceed time limit...
def is_bipartite(graph: List[List[int]]):
    set_a = set_b = frozenset()

    def dfs(vertex, set_a, set_b):
        if vertex == len(graph):
            return True

        connected_vertices_set = frozenset(graph[vertex])
        if vertex in set_a:
            if connected_vertices_set.isdisjoint(set_a):
                set_b = set_b.union(connected_vertices_set)
            else:
                return False
        elif vertex in set_b:
            if connected_vertices_set.isdisjoint(set_b):
                set_a = set_a.union(connected_vertices_set)
            else:
                return False
        else:
            if connected_vertices_set.isdisjoint(set_b) and connected_vertices_set.isdisjoint(set_a):
                set_b = set_b.union({vertex})
                set_a = set_a.union(connected_vertices_set)
                if not dfs(vertex + 1, set_a, set_b):
                    return dfs(vertex + 1, (set_a - connected_vertices_set) | {vertex},
                               set_b - {vertex} | connected_vertices_set)
            elif connected_vertices_set.isdisjoint(set_a):
                set_a = set_a.union({vertex})
                set_b = set_b.union(connected_vertices_set)
            elif connected_vertices_set.isdisjoint(set_b):
                set_b = set_b.union({vertex})
                set_a = set_a.union(connected_vertices_set)
            else:
                return False
        return dfs(vertex + 1, set_a, set_b)

    return dfs(0, set_a, set_b)


def is_bipartite2(graph: List[List[int]]):
    def dfs(cortex, valid_colour):
        if cortex in colored:
            return colored[cortex] == valid_colour
        else:
            colored[cortex] = valid_colour
            return all(dfs(neighbour, -valid_colour) for neighbour in graph[cortex])

    colored = {}

    return all(dfs(cortex, 1) for cortex in range(len(graph)) if cortex not in colored)


def is_bipartite_bfs(graph: List[List[int]]):
    colored = {}
    for cortex in range(len(graph)):
        if cortex not in colored:
            to_visit = deque([])
            to_visit.append((cortex, 1))
            while to_visit:
                cortex, valid_colour = to_visit.popleft()
                if cortex in colored:
                    if colored[cortex] != valid_colour:
                        return False
                else:
                    colored[cortex] = valid_colour
                    for neighbour in graph[cortex]:
                        to_visit.append((neighbour, -valid_colour))
    return True


print(is_bipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
print(is_bipartite2([[1, 3], [0, 2], [1, 3], [0, 2]]))
print(is_bipartite_bfs([[1, 3], [0, 2], [1, 3], [0, 2]]))

print(is_bipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
print(is_bipartite2([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
print(is_bipartite_bfs([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))

print(is_bipartite([[3], [2, 4], [1], [0, 4], [1, 3]]))
print(is_bipartite2([[3], [2, 4], [1], [0, 4], [1, 3]]))
print(is_bipartite_bfs([[3], [2, 4], [1], [0, 4], [1, 3]]))

# print(is_bipartite([[2, 4], [2, 3, 4], [0, 1], [1], [0, 1], [7], [9], [5], [], [6], [12, 14], [], [10], [], [10], [19], [18], [], [16],
#  [15], [23], [23], [], [20, 21], [], [], [27], [26], [], [], [34], [33, 34], [], [31], [30, 31], [38, 39], [37, 38, 39],
#  [36], [35, 36], [35, 36], [43], [], [], [40], [], [49], [47, 48, 49], [46, 48, 49], [46, 47, 49], [45, 46, 47, 48]]))
print(is_bipartite2(
    [[2, 4], [2, 3, 4], [0, 1], [1], [0, 1], [7], [9], [5], [], [6], [12, 14], [], [10], [], [10], [19], [18], [], [16],
     [15], [23], [23], [], [20, 21], [], [], [27], [26], [], [], [34], [33, 34], [], [31], [30, 31], [38, 39],
     [37, 38, 39],
     [36], [35, 36], [35, 36], [43], [], [], [40], [], [49], [47, 48, 49], [46, 48, 49], [46, 47, 49],
     [45, 46, 47, 48]]))
print(is_bipartite_bfs(
    [[2, 4], [2, 3, 4], [0, 1], [1], [0, 1], [7], [9], [5], [], [6], [12, 14], [], [10], [], [10], [19], [18], [], [16],
     [15], [23], [23], [], [20, 21], [], [], [27], [26], [], [], [34], [33, 34], [], [31], [30, 31], [38, 39],
     [37, 38, 39],
     [36], [35, 36], [35, 36], [43], [], [], [40], [], [49], [47, 48, 49], [46, 48, 49], [46, 47, 49],
     [45, 46, 47, 48]]))


# connect dislike persons with an edge
# and then try to bipartie the graph
# dfs is implemented in bad way see above is_bipartite2 for a better version
def possible_bipartite(n, dislikes: List[List[int]]):
    def dfs(person):
        for dislike_p in graph[person]:
            if dislike_p in grouped:
                if grouped[dislike_p] == grouped[person]:
                    return False
            else:
                grouped[dislike_p] = -grouped[person]
                if not dfs(dislike_p):
                    return False
        return True

    graph = [[] for _ in range(n)]
    for dislike_pair in dislikes:
        graph[dislike_pair[0] - 1].append(dislike_pair[1] - 1)
        graph[dislike_pair[1] - 1].append(dislike_pair[0] - 1)

    grouped = {}
    for person in range(n):
        if person not in grouped:
            grouped[person] = 1
            if not dfs(person):
                return False
    return True


print('------------------')
dislikes = [[1, 2], [1, 3], [2, 4]]
n = 4
print(possible_bipartite(n, dislikes))

dislikes = [[1, 2], [1, 3], [2, 3]]
n = 3
print(possible_bipartite(n, dislikes))

dislikes = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
n = 5
print(possible_bipartite(n, dislikes))

n = 50
dislikes = [[21, 47], [4, 41], [2, 41], [36, 42], [32, 45], [26, 28], [32, 44], [5, 41], [29, 44], [10, 46], [1, 6],
            [7, 42], [46, 49], [17, 46], [32, 35], [11, 48], [37, 48], [37, 43], [8, 41], [16, 22], [41, 43], [11, 27],
            [22, 44], [22, 28], [18, 37], [5, 11], [18, 46], [22, 48], [1, 17], [2, 32], [21, 37], [7, 22], [23, 41],
            [30, 39], [6, 41], [10, 22], [36, 41], [22, 25], [1, 12], [2, 11], [45, 46], [2, 22], [1, 38], [47, 50],
            [11, 15], [2, 37], [1, 43], [30, 45], [4, 32], [28, 37], [1, 21], [23, 37], [5, 37], [29, 40], [6, 42],
            [3, 11], [40, 42], [26, 49], [41, 50], [13, 41], [20, 47], [15, 26], [47, 49], [5, 30], [4, 42], [10, 30],
            [6, 29], [20, 42], [4, 37], [28, 42], [1, 16], [8, 32], [16, 29], [31, 47], [15, 47], [1, 5], [7, 37],
            [14, 47], [30, 48], [1, 10], [26, 43], [15, 46], [42, 45], [18, 42], [25, 42], [38, 41], [32, 39], [6, 30],
            [29, 33], [34, 37], [26, 38], [3, 22], [18, 47], [42, 48], [22, 49], [26, 34], [22, 36], [29, 36], [11, 25],
            [41, 44], [6, 46], [13, 22], [11, 16], [10, 37], [42, 43], [12, 32], [1, 48], [26, 40], [22, 50], [17, 26],
            [4, 22], [11, 14], [26, 39], [7, 11], [23, 26], [1, 20], [32, 33], [30, 33], [1, 25], [2, 30], [2, 46],
            [26, 45], [47, 48], [5, 29], [3, 37], [22, 34], [20, 22], [9, 47], [1, 4], [36, 46], [30, 49]]
print(possible_bipartite(n, dislikes))
