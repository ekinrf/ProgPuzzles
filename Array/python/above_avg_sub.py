from typing import List


#O(n2)
def above_avg_sub(nums: List[int]):
    if not nums:
        return []
    cum_sum = [0] * (len(nums) + 1)
    for i, n in enumerate(nums):
        cum_sum[i + 1] = cum_sum[i] + n

    avg = cum_sum[len(nums)] / len(nums)
    i, j = 0, 1
    res = []
    while i < len(nums):
        for j in range(i + 1, len(nums) + 1):
            sub_arr_sum = cum_sum[j] - cum_sum[i]
            sub_arr_avg = sub_arr_sum / (j - i)
            if sub_arr_avg > avg:
                res.append([i + 1, j])
        i += 1
    # full array would always be valid
    res.append([1, len(nums)])
    return res


print(above_avg_sub([3, 4, 2, 3]))


def num_of_subarray_gt_avg(arr: List[int], k, threshold):
    cum_sum = [0] * (len(arr) + 1)
    for i, n in enumerate(arr):
        cum_sum[i + 1] = cum_sum[i] + n
    sum_threshold = k * threshold

    ret = 0
    for i, sub_sum in enumerate(cum_sum):
        if (i + k) < len(cum_sum):
            if cum_sum[i + k] - cum_sum[i] >= sum_threshold:
                ret += 1
    return ret


print(num_of_subarray_gt_avg([2,2,2,2,5,5,5,8], 3, 4))