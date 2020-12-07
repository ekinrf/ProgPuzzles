from collections import defaultdict, deque
from typing import List


# build edges between character
# then topological sort the graph
def find_alien_order(words: List[str]):
    def dfs(c):
        visited.add(c)
        for child in graph[c]:
            if child not in visited:
                dfs(child)
        sorted_list.appendleft(c)

    graph = defaultdict(set)

    # zip the words, so we can compare 2 adjacent word easier
    for w1, w2 in zip(words, words[1:]):
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                graph[c1].add(c2)

    # avoid runtime error (change dictionary while iterating)
    keys = list(graph.keys())
    visited = set()
    sorted_list = deque()
    for c in keys:
        if c not in visited:
            dfs(c)
    return sorted_list


words = [
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
]
print(find_alien_order(words))

words = ["baa", "abcd", "abca", "cab", "cad"]
print(find_alien_order(words))
