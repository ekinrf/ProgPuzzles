from typing import List

# scan to find all sorted array
# then do a k merge sorted array using heap
import heapq


def sort_partial(nums: List[int]):
    sub_arr = {}
    s, e = 0, 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            sub_arr[e] = s
            s = i + 1
        e += 1
    sub_arr[e] = s
    a_heap = []
    for arr_e, arr_s in sub_arr.items():
        heapq.heappush(a_heap, (nums[arr_s], arr_s, arr_e))

    res = []
    while a_heap:
        num, arr_idx, arr_e = heapq.heappop(a_heap)
        res.append(num)
        if arr_idx != arr_e:
            heapq.heappush(a_heap, (nums[arr_idx + 1], arr_idx + 1, arr_e))

    return res


print(sort_partial([1, 2, 3, 2, 3, 4, 1, 5, 6, 5, 6, 9]))
