import heapq


def trapping_water(heights):
    h_heap = []
    visited = [False] * len(heights)
    for i, h in enumerate(heights):
        visited[i] = True
        if h:
            heapq.heappush(h_heap, (h, i))
            break
    for i in reversed(range(len(heights))):
        visited[i] = True
        if heights[i]:
            heapq.heappush(h_heap, (heights[i], i))
            break
    water_level = water_trapped = 0
    while h_heap:
        h, i = heapq.heappop(h_heap)
        if h > water_level:
            water_level = h
        water_trapped += water_level - h
        if i - 1 > 0 and not visited[i - 1]:
            heapq.heappush(h_heap, (heights[i - 1], i - 1))
            visited[i - 1] = True
        if i + 1 < len(heights) and not visited[i + 1]:
            heapq.heappush(h_heap, (heights[i + 1], i + 1))
            visited[i + 1] = True
    return water_trapped


print(trapping_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
