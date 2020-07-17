import heapq


def kth_largest_elem(nums, k):
    nums_heap = []
    for n in nums:
        heapq.heappush(nums_heap, n)
        if len(nums_heap) > k:
            heapq.heappop(nums_heap)
    return heapq.heappop(nums_heap)


print(kth_largest_elem([3,2,3,1,2,4,5,5,6], 4))