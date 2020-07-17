from typing import List


def find_missing_kth(nums: List[int], k):
    left, right = 0, len(nums) - 1
    while right - left > 1:
        mid = left + (right - left) // 2
        num_count_left_without_missing = nums[mid] - nums[left] + 1
        num_count_left = mid - left + 1
        count_delta_left = num_count_left_without_missing - num_count_left
        if count_delta_left >= k:
            right = mid
        elif count_delta_left < k:
            k -= count_delta_left
            left = mid

    if k >= nums[right] - nums[left]:
        return nums[left] + k + 1
    else:
        return nums[left] + k


print(find_missing_kth([4,7,9,10], 1))
print(find_missing_kth([4,7,9,10], 3))
print(find_missing_kth([1, 2, 4], 3))

print(find_missing_kth([0, 1, 2, 4], 2))

print(find_missing_kth([0, 5, 6, 10], 2))