def longest_inc_subseq(array):
    def lis_ending_at_index(i):
        if i is 0:
            return 1, i
        else:
            lis_list = [lis_ending_at_index(index) for index in range(0, i) if array[index] < array[i]]
            if lis_list:
                length, index = max(lis_list, key=lambda x: x[0])
                return length + 1, i
            else:
                return 1, i

    lis_list = [lis_ending_at_index(x) for x in range(0, len(array))]
    return max(lis_list, key=lambda x: x[0])

print(longest_inc_subseq([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
