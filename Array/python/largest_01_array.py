def largest_01_array(array):
    max_len, max_ending_at = 0, 0
    max_len_ending_at = [0] * len(array)
    for i in range(1, len(array)):
        if array[i] != array[i - 1]:
            max_len_ending_at[i] = 2
        if i - 1 - max_len_ending_at[i - 1] >= 0 and array[i - 1 - max_len_ending_at[i - 1]] != array[i]:
            max_len_ending_at[i] = max_len_ending_at[i - 1] + 2
            if i - max_len_ending_at[i] > 0:
                max_len_ending_at[i] += max_len_ending_at[i - max_len_ending_at[i]]
        if max_len_ending_at[i] > max_len:
            max_len = max_len_ending_at[i]
            max_ending_at = i
    # print(max_len_ending_at)
    return max_ending_at - max_len + 1, max_ending_at, max_len

print(largest_01_array([1, 0, 0, 1, 0, 1, 1]))
print(largest_01_array([0, 0, 1, 1, 0]))
print(largest_01_array([1, 1, 1, 1, 0]))
print(largest_01_array([1, 0, 1, 1, 1, 0, 0]))
print(largest_01_array([0, 0, 0, 1, 0, 1, 0, 1, 1]))
