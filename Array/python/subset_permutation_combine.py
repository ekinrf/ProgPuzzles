from typing import List, Set


# [1, 2] -> [[], [1], [2], [1, 2]]
def subset_arr(nums: List[int]):
    def dfs(idx, cur_set: List[int]):
        ret.append(cur_set.copy())
        for i in range(idx, len(nums)):
            cur_set.append(nums[i])
            dfs(i + 1, cur_set)
            cur_set.pop()

    ret = []
    dfs(0, [])
    return ret


print(subset_arr([1, 2, 3]))


# n = 4, k = 2 => [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
def combine(n: int, k: int):
    def dfs(cur_idx, cur_set):
        if len(cur_set) == k:
            ret.append(cur_set.copy())
        else:
            for i in range(cur_idx, n):
                cur_set.append(i + 1)
                dfs(i + 1, cur_set)
                cur_set.pop()

    ret = []
    dfs(0, [])
    return ret


print(combine(4, 3))


# permutation: nums no duplicate
def permute(nums: List[int]):
    def dfs(nums_to_choose: Set[int], cur_permu):
        if not nums_to_choose:
            res.append(cur_permu.copy())
        else:
            for n in nums_to_choose:
                cur_permu.append(n)
                dfs(nums_to_choose - {n}, cur_permu)
                cur_permu.pop()

    res = []
    dfs(set(nums), [])
    return res


print(permute([1, 2, 3]))