from typing import List


def new_arr_mul(nums: List[int]):
    all_mul = 1
    for n in nums:
        if n != 0:
            all_mul *= n
    return [all_mul / n if n != 0 else all_mul for n in nums]


print(new_arr_mul([1, 2, 3, 4, 5]))

print(new_arr_mul([1, 0, 3, 4, 5]))
