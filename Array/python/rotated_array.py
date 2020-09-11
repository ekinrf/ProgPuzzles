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

print('===============')


# No Duplicates
def search(nums: List[int], target: int):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            if nums[mid] > nums[left] or nums[right] >= target:
                left = mid + 1
            else:
                right = mid - 1
        elif nums[mid] > target:
            if nums[left] <= target or nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
    return -1


# allows duplicate
def search_dup(nums: List[int], target: int):
    def search(l, r):
        if r < l:
            return False
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return True
        while l < mid and nums[mid] == nums[l]: # don't know which part is sorted
            l += 1
        # left hand side is sorted!
        if nums[mid] >= nums[l]:
            if nums[l] <= target < nums[mid]:
                return search(l, mid - 1)
            else:
                return search(mid + 1, r)
         # right side is sorted!
        elif nums[mid] < nums[l]:
            if nums[mid] < target <= nums[r]:
                return search(mid + 1, r)
            else:
                return search(l, mid - 1)
    return search(0, len(nums) - 1)


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(nums, target))

target = 3
print(search(nums, target))

nums = [4, 5, 6, 7, 8, 1, 2, 3]
target = 8
print(search(nums, target))
