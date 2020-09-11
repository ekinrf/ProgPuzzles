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


def trapping_water_alt(heights):
    if not heights:
        return 0
    highest_so_far = heights[0]
    left_bound = []
    right_bound = []
    for h in heights:
        if highest_so_far < h:
            highest_so_far = h
        left_bound.append(highest_so_far)
    highest_so_far = heights[-1]
    for h in reversed(heights):
        if highest_so_far < h:
            highest_so_far = h
        right_bound.append(highest_so_far)
    water_trapped = 0
    for i, (l, r) in enumerate(zip(left_bound, reversed(right_bound))):
        water_trapped += min(l, r) - heights[i]
    return water_trapped


def trapping_water_stack(heights):
    stack = []
    water_trapped = 0
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] < h:
            bar_to_fill = stack.pop()
            if stack:
                water_trapped += (min(heights[stack[-1]], h) - heights[bar_to_fill]) * (i - stack[-1] - 1)
        stack.append(i)
    return water_trapped


def trap_water(heights):
    l_max = r_max = 0
    i, j = 0, len(heights) - 1
    res = 0
    while i < j:
        l_max = max(l_max, heights[i])
        r_max = max(r_max, heights[j])
        if l_max < r_max:
            i += 1
            res += max(0, l_max - heights[i])
        else:
            j -= 1
            res += max(0, r_max - heights[j])
    return res


print(trapping_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(trapping_water_alt([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(trapping_water_alt([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 3, 2]))
print(trapping_water_stack([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 3, 2]))
print(trapping_water_stack([4, 2, 3]))

print(trap_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(trap_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 3, 2]))
print(trap_water([4, 2, 3]))
