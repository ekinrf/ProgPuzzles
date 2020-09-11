from collections import defaultdict
from typing import List


# Use a sorted list to make duplicates checking easier than map
def three_sum(nums: List[int]):
    sorted_nums = sorted(nums)
    res = []
    for i in range(len(sorted_nums) - 2):
        if nums[i] > 0:
            break
        if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
            continue
        left, right = i + 1, len(sorted_nums) - 1
        while left < right:
            if sorted_nums[i] + sorted_nums[left] < -sorted_nums[right]:
                left += 1
            elif sorted_nums[i] + sorted_nums[left] > -sorted_nums[right]:
                right -= 1
            else:
                res.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                while left < right and sorted_nums[left] == sorted_nums[left + 1]:
                    left += 1
                while left < right and sorted_nums[right] == sorted_nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return res


nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))

nums = [0, 0, 0]
print(three_sum(nums))
