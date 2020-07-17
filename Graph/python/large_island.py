from collections import deque
from typing import List


def neighbours(x, y, x_len, y_len):
    direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for x_d, y_d in direction:
        if 0 <= x + x_d < x_len and 0 <= y + y_d < y_len:
            yield x + x_d, y + y_d


def large_island(grid: List[List[int]]):
    if grid:
        max_area = 0
        parent = [None] * len(grid) * len(grid[0])
        point_to_area = {}

        # First traverse for 1s only
        # It will find all connected 1s and their area
        # Use Parent array to store each 1's root node (where we first start the traversal)
        # Use point_to_area to store root node to connect area
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                cur_area = 0
                to_visit = deque([(i, j)])
                while to_visit:
                    x, y = to_visit.popleft()
                    if not parent[x * len(grid[0]) + y] and grid[x][y] == 1:
                        parent[x * len(grid[0]) + y] = (i, j)
                        cur_area += 1
                        for x_d, y_d in neighbours(x, y, len(grid), len((grid[0]))):
                            to_visit.append((x_d,  y_d))
                point_to_area[(i, j)] = cur_area
                max_area = max(cur_area, max_area)

        # Second traversal for 0s only
        # Find 0 then all the neighbour 1s with different connected area (distinguish by different root)
        # Sum them up to update the max area
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                connected_area_roots = set()
                if grid[i][j] == 0:
                    cur_area = 1
                    for x, y in neighbours(i, j, len(grid), len((grid[0]))):
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                            root_node_for_area = parent[x * len(grid[0]) + y]
                            if not root_node_for_area in connected_area_roots:
                                connected_area_roots.add(root_node_for_area)
                                cur_area += point_to_area[root_node_for_area]
                    max_area = max(cur_area, max_area)

        return max_area


# print(large_island([[1, 1], [1, 0]]))
print(large_island([[0, 0], [0, 1]]))
print(large_island(
    [[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 0, 0], [0, 1, 1, 1, 1, 0, 0]]))
