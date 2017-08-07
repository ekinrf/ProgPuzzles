def largest_div_subset(nums):
    sets = {-1: set()}  # all nums are positive set this to avoid max() arg is an empty sequence
    for num in sorted(nums):
        sets[num] = max((sets[x] for x in sets if num % x == 0), key=len) | {num}

    return list(max(sets.values(), key=len))


print(largest_div_subset([1, 2, 3, 4, 5, 8]))
