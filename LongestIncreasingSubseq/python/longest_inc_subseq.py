def longest_inc_subseq(array):
    def lis_ending_at_index(i):
        if i is 0:
            return 1, i  # length, index
        else:
            lis_list = [lis_ending_at_index(index) for index in range(0, i) if array[index] < array[i]]
            if lis_list:
                length, index = max(lis_list, key=lambda x: x[0])
                return length + 1, i
            else:
                return 1, i

    lis_list = [lis_ending_at_index(x) for x in range(0, len(array))]
    return max(lis_list, key=lambda x: x[0])


def lis_quick_search(array):
    import bisect

    length = len(array)
    memo = [0] * length
    longest_len = 0

    for number in array:
        i = bisect.bisect_left(memo, number, 0, longest_len)
        if i:
            new_len = i + 1
        else:
            new_len = 1

        longest_len = max(longest_len, new_len)
        memo[i] = number

    return longest_len

import timeit

print(longest_inc_subseq([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
print(lis_quick_search([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
t1 = timeit.Timer("longest_inc_subseq([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])",
                  "from __main__ import longest_inc_subseq")
t2 = timeit.Timer("lis_quick_search([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])",
                  "from __main__ import lis_quick_search")

print(t1.timeit(1000))
print(t2.timeit(1000))

