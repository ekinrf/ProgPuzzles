from typing import List


# [4, 5, 6, 1, 3]
# [4, 1, 3]
# no duplicates allowed
def find_min(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1
    return nums[right]


# [3, 3, 1, 3]
# [3, 1, 3, 3]
# [1, 2, 3]
# [1, 3, 3]
def find_min_dup(nums: List[int]) -> int:
    def _find_min_rec(left, right):
        if left >= right:
            return nums[left]
        mid = left + (right - left) // 2
        if nums[mid] < nums[right]:
            return _find_min_rec(left, mid)
        elif nums[mid] > nums[left] and nums[mid] != nums[right]:
            return _find_min_rec(mid + 1, right)
        else:
            return min(_find_min_rec(left, mid - 1), _find_min_rec(mid + 1, right))

    return _find_min_rec(0, len(nums) - 1)


# print(find_min([4, 5, 6, 7, 0, 1, 2]))
print(find_min_dup([4, 5, 6, 7, 0, 1, 2]))
print(find_min_dup([3, 3, 1, 3]))
print(find_min_dup([3, 1, 3, 3]))
print(find_min_dup([1, 3, 3]))