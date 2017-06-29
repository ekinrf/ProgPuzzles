

# all numbers in array are no less than 0
# O(n)
def sub_array_less_or_eq_positive(array, target):
    start = end = max_start = max_len = sum = 0

    while end < len(array) and start < len(array):
        sum += array[end]
        if sum <= target:
            end += 1
        else:
            cur_len = end - start
            if cur_len > max_len:
                max_len = cur_len
                max_start = start
            sum -= array[start]
            sum -= array[end]
            start += 1

    if sum <= target:  # case where last element included
        cur_len = end - start
        if cur_len > max_len:
            max_len = cur_len
            max_start = start

    return max_start, max_start + max_len - 1


# array contains any numbers negative or positive
# O(n*logn)
def sub_array_less_or_eq(array, target):
    import bisect

    sum = [array[0]] * len(array)
    max_sum = [array[0]] * len(array)
    max_len, max_ending = 0, -1
    for i in range(1, len(array)):
        sum[i] = sum[i - 1] + array[i]
        max_sum[i] = max(max_sum[i - 1], max_sum[i - 1] + array[i])
        prev_target = sum[i] - target
        lt_eq_prev_idx = bisect.bisect_left(max_sum, prev_target, 0, i)
        if lt_eq_prev_idx is 0 and array[0] is not prev_target:
            # the key is to find a max_sum[k] < prev_target, then k + 1 will be the start
            # hence the special case at index 0
            lt_eq_prev_idx += 1
        if i - lt_eq_prev_idx + 1 > max_len:
            max_len = i - lt_eq_prev_idx + 1
            max_ending = i
    return max_ending - max_len + 1, max_ending, max_len


print(sub_array_less_or_eq_positive([3, 3, 2, 1], 7))
print(sub_array_less_or_eq_positive([1, 2, 3, 4], 8))

print(sub_array_less_or_eq([3, 5, -3, 3, 2, 0], 7))
print(sub_array_less_or_eq([3, 3, 2, 1], 7))
