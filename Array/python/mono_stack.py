import bisect

from typing import List


# -1, -1,

def daily_temp(t: List[int]) -> List[int]:
    dis = [0] * len(t)
    smaller_idx = list()
    for i in range(len(t) - 1, -1, -1):
        while smaller_idx and t[smaller_idx[-1]] <= t[i]:
            smaller_idx.pop()
        dis[i] = 0 if not smaller_idx else smaller_idx[-1] - i
        smaller_idx.append(i)
    return dis


print(daily_temp([73, 74, 75, 71, 69, 72, 76, 73]))


def next_gt_number(nums1, nums2):
    nums2_gt = {}
    gt_nums = []
    for n in reversed(nums2):
        while gt_nums and gt_nums[-1] <= n:
            gt_nums.pop()
        nums2_gt[n] = gt_nums[-1] if gt_nums else -1
        gt_nums.append(n)
    return [nums2_gt[n] for n in nums1]


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(next_gt_number(nums1, nums2))


# [1, 2, 1, 1, 2, 1]
def next_gt_number_circular(nums):
    res = [-1] * len(nums)
    gt_nums = []

    i = len(nums) * 2 - 1
    while i >= 0:
        real_i = i % len(nums)
        while gt_nums and gt_nums[-1] <= nums[real_i]:
            gt_nums.pop()
        if i < len(nums):
            res[real_i] = gt_nums[-1] if gt_nums else -1
        gt_nums.append(nums[real_i])
        i -= 1
    return res


print(next_gt_number_circular([1, 2, 1]))