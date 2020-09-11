from typing import List

import heapq


def k_closest(points: List[List[int]], k):
    k_heap = []
    for i, p in enumerate(points):
        distance = pow(p[0], 2) + pow(p[1], 2)
        if len(k_heap) == k:
            if k_heap[0][0] < -distance:
                heapq.heappop(k_heap)
            else:
                continue
        heapq.heappush(k_heap, (-distance, i))
    return [points[idx] for (_, idx) in k_heap]


print(k_closest([[3, 3], [5, -1], [-2, 4]], 2))
