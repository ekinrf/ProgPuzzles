# O(logN) and space O(1)
def single_elem_in_sorted(nums):
    if len(nums) is 1:
        return nums[0]
    mid = int(len(nums) / 2)
    in_left = False
    if nums[mid + 1] == nums[mid]:
        if (len(nums) - mid) % 2 == 0:
            in_left = True
    elif nums[mid - 1] == nums[mid]:  # don't need boundary check
        if (mid + 1) % 2 != 0:
            in_left = True
        mid += 1
    else:
        return nums[mid]
    if in_left:
        return single_elem_in_sorted(nums[0: mid])
    else:
        return single_elem_in_sorted(nums[mid: len(nums)])


print(single_elem_in_sorted([1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(single_elem_in_sorted([3, 3, 7, 7, 10, 11, 11]))
