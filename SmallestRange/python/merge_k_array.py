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


def smallest_range(arrays):
    k_min_heap = []
    max_in_heap = 0
    cur_idx = {}
    for idx, array in enumerate(arrays):
        if idx is 0:
            max_in_heap = array[0]
        max_in_heap = max(max_in_heap, array[0])
        k_min_heap.append((array[0], idx))
        cur_idx[idx] = 0
    heapq.heapify(k_min_heap)
    s_range = (k_min_heap[0][0], max_in_heap)
    while k_min_heap:
        smallest, a_idx = heapq.heappop(k_min_heap)
        if max_in_heap - smallest < s_range[1] - s_range[0]:
            s_range = smallest, max_in_heap
        v_idx = cur_idx[a_idx] + 1
        if v_idx < len(arrays[a_idx]):
            cur_idx[a_idx] = v_idx
            max_in_heap = max(max_in_heap, arrays[a_idx][v_idx])
            heapq.heappush(k_min_heap, (arrays[a_idx][v_idx], a_idx))
        else:
            break
    return s_range


print(merge_sorted_arrays([[0, 9, 12, 30], [5, 18, 22, 30]]))
print(smallest_range([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
