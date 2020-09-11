from typing import List


# [1，2，4, 7, 7, 7, 8, 10]有序数组中，输入一个数字，返回它在数组中出现几次，比如 7=>3 ; 8=>1
def find_occ(arr: List[int], tar: int):
    s, e = 0, len(arr) - 1
    while s <= e:
        mid = s + (e - s) // 2
        if arr[mid] == tar:
            e = mid - 1
        elif arr[mid] < tar:
            s = mid + 1
        elif arr[mid] > tar:
            e = mid - 1
    if s < len(arr) and arr[s] == tar:
        left_bound = s
        e = len(arr) - 1
        while s <= e:
            mid = s + (e - s) // 2
            if arr[mid] == tar:
                s = mid + 1
            else:  # tar cannot be less than tar
                e = mid - 1
        return e - left_bound + 1
    else:
        return 0


print(find_occ([1, 2, 4, 7, 7, 7, 8, 10], 7))

print(find_occ([1, 2, 4, 7, 7, 7, 8, 10], 0))

print(find_occ([1, 2, 4, 7, 7, 7, 8, 10], 15))


print(find_occ([1, 1, 1, 1, 1, 1], 1))
