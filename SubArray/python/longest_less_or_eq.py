# all numbers in array are no less than 0:  time complexity O(n)
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
def sub_array_less_or_eq(array, target):
    pass


print(sub_array_less_or_eq_positive([3, 1, 2, 1], 4))
