import heapq


# arrays is list of list
def merge_sorted_arrays(arrays):
    k_heap = []
    merged = []
    cur_idx = {}
    for idx, array in enumerate(arrays):
        k_heap.append((array[0], idx))
        cur_idx[idx] = 0
    heapq.heapify(k_heap)
    while k_heap:
        value, a_idx = heapq.heappop(k_heap)
        merged.append(value)
        v_idx = cur_idx[a_idx] + 1
        if v_idx < len(arrays[a_idx]):
            cur_idx[a_idx] = v_idx
            heapq.heappush(k_heap, (arrays[a_idx][v_idx], a_idx))
    return merged

print(merge_sorted_arrays([[0, 9, 12, 30], [5, 18, 22, 30]]))
