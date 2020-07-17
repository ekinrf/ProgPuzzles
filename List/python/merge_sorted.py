import heapq
from typing import List

from python.list_node import ListNode


def merge_k_list(lists: List[ListNode]):
    heap_k = []
    tmp_counter = 0
    for l in lists:
        if l:
            heapq.heappush(heap_k, (l.val, tmp_counter, l))
            tmp_counter += 1
    res = None
    res_last = None
    while heap_k:
        min_val, _, node = heapq.heappop(heap_k)
        res = node if not res else res
        if node.next:
            heapq.heappush(heap_k, (node.next.val, tmp_counter, node.next))
            tmp_counter += 1
        if res_last:
            res_last.next = node
            res_last = node
        else:
            res_last = node
    return res

