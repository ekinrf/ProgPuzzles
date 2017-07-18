# allows equal a <= b >= c <= d >= e
# O(n)
def wiggle_sort(nums):
    def swap(a, b):
        tmp = nums[a]
        nums[a] = nums[b]
        nums[b] = tmp

    idx = 0
    while idx < len(nums):
        if idx + 1 < len(nums):
            if nums[idx + 1] < nums[idx]:
                swap(idx + 1, idx)
            if idx + 2 < len(nums):
                if nums[idx + 1] < nums[idx + 2]:
                    swap(idx + 1, idx + 2)
        idx += 2

    return nums


# no equals allowed
# O(n*logn + n)
def wiggle_sort_2(nums):
    sorted_nums = nums[:]
    sorted_nums.sort()
    median = int((len(nums) - 1) / 2)
    count = 0
    while count <= median:
        nums[count * 2] = sorted_nums[median - count]
        if 2 * count + 1 < len(nums):
            nums[2 * count + 1] = sorted_nums[len(nums) - 1 - count]
        count += 1
    return nums


print(wiggle_sort_2([1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2]))
print(wiggle_sort_2([1, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1, 2, 1, 2, 1, 1, 2]))
