from collections import defaultdict


def sub_array_sum(nums, k):
    sums = defaultdict(int)
    accu_sum = res = 0
    sums[0] = 1
    for n in nums:
        accu_sum += n
        tar = accu_sum - k
        res += sums[tar]
        sums[accu_sum] += 1

    return res


print(sub_array_sum([1, 1, 1], 2))