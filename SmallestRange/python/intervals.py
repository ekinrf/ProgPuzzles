from typing import List


def insert_intervals(intervals: List[List[int]], new_interval: List[int]):
    idx = 0
    res = []
    while idx < len(intervals) and intervals[idx][1] < new_interval[0]:
        res.append(intervals[idx])
        idx += 1

    while idx < len(intervals) and intervals[idx][0] <= new_interval[1]:
        new_interval[0] = min(intervals[idx][0], new_interval[0])
        new_interval[1] = max(intervals[idx][1], new_interval[1])
        idx += 1

    res.append(new_interval)

    while idx < len(intervals):
        res.append(intervals[idx])
        idx += 1

    return res


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
# intervals = [[0,2],[3,3],[6,11]]
newInterval = [9, 15]
print(insert_intervals(intervals, newInterval))


def merge_intervals(intervals: List[List[int]]):
    if not intervals:
        return []

    sorted_i_by_start = sorted(intervals, key=lambda i: i[0])
    res = [sorted_i_by_start[0]]

    for i in sorted_i_by_start[1:]:
        if i[0] <= res[-1][1]:
            res[-1][1] = max(i[1], res[-1][1])
        else:
            res.append(i)
    return res


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))
print('----')


# https://leetcode.com/problems/interval-list-intersections/
# 986
def intersect_intervals(a, b):
    a_idx = b_idx = 0
    res = []

    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx][1] < b[b_idx][0]:
            a_idx += 1
        elif b[b_idx][1] < a[a_idx][0]:
            b_idx += 1
        else:
            res.append([max(a[a_idx][0], b[b_idx][0]), min(a[a_idx][1], b[b_idx][1])])
            if a[a_idx][1] > b[b_idx][1]:
                b_idx += 1
            else:
                a_idx += 1

    return res


# sorted by end time
# start traverse, check the neighours if overlapping, keep only 1
def min_remove_to_make_non_overlapping(intervals: List[List[int]]):
    # sorted by end time
    sorted_i_by_end = sorted(intervals, key=lambda x: x[1])
    i, j = 0, 1
    removed = 0
    while j < len(sorted_i_by_end):
        if sorted_i_by_end[i][1] > sorted_i_by_end[j][0]:
            removed += 1
        else:
            i = j
        j += 1
    return removed


print(min_remove_to_make_non_overlapping([[1, 2], [1, 2], [1, 2]]))
print(min_remove_to_make_non_overlapping([[1, 2], [2, 3], [3, 4], [1, 3]]))
print(min_remove_to_make_non_overlapping([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]))
