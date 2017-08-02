import functools


def remove_overlapped(ranges):
    def is_overlapped(r1, r2):
        return r2[0] <= r1[0] < r2[1] or r1[0] <= r2[0] <= r1[1]

    def merge(r1, r2):
        return min(r1[0], r2[0]), max(r1[1], r2[1])

    def reduce_ranges(reduced_ranges, next_range):
        if is_overlapped(reduced_ranges[-1], next_range):
            merged = merge(reduced_ranges[-1], next_range)
            reduced_ranges[-1] = merged
        else:
            reduced_ranges.append(next_range)
        return reduced_ranges

    sorted_ranges = sorted(ranges)
    return functools.reduce(reduce_ranges, sorted_ranges, [sorted_ranges[0]])

print(remove_overlapped([(1, 3), (12, 14), (2, 4), (13, 15), (5, 10)]))
