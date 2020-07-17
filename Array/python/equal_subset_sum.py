from typing import List

# tar[i][t] = tar[i - 1][t] | tar[i - 1][t - nums[i]]
# tar[0][nums[0]]


def memo(fn):
    cache = {}
    missed = object()

    def query(*args):
        res = cache.get(args, missed)
        if res is missed:
            res = cache[args] = fn(*args)
        return res

    return query


def can_partition(nums: List[int]):
    @memo
    def _find_sum(i, tar):
        if tar < 0 or i == len(nums):
            return False
        if nums[i] == tar:
            return True
        else:
            return _find_sum(i + 1, tar - nums[i]) or _find_sum(i + 1, tar)

    sum_n = sum(nums)
    if sum_n % 2:
        return False
    else:
        par_target = sum_n / 2
        return _find_sum(0, par_target)


print(can_partition([1, 5, 11, 5]))
