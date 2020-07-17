from typing import List


# binary search log(n)
def peak_elem(nums: List[int]):
    l, h = 0, len(nums) - 1
    while l <= h:
        mid = l + (h - l) // 2
        if h - l == 1:
            return h if nums[h] > nums[l] else l
        elif mid - 1 < 0 or mid + 1 > len(nums) - 1:
            return mid
        elif nums[mid - 1] < nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid] < nums[mid - 1]:
            h = mid - 1
        elif nums[mid] < nums[mid + 1]:
            l = mid + 1
    return -1


print(peak_elem([1, 2, 3, 1]))
print(peak_elem([1, 2, 1, 3, 5, 6, 4]))

print(peak_elem([1, 2]))
