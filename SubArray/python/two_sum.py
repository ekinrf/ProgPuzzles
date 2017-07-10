def two_sum(nums, target):
    quick_lookup = {}
    for idx, num in enumerate(nums):
        if target - num in quick_lookup:
            return quick_lookup[target - num], idx
        else:
            quick_lookup[num] = idx
    return -1, -1

print(two_sum([2, 7, 11, 15], 9))
