
def find_positions(arr, x):
    # Write your code here
    iter = idx = 0
    res = []
    while iter < x:
        counter = 0
        cur_max, max_idx = -1, -1
        while counter < min(x, len(arr) - iter):
            idx = idx % len(arr)
            if arr[idx] >= 0:
                if cur_max < arr[idx]:
                    cur_max = arr[idx]
                    max_idx = idx
                arr[idx] = max(arr[idx] - 1, 0)
                counter += 1
            idx += 1

        print(arr[max_idx])
        arr[max_idx] = -1
        res.append(max_idx + 1)
        iter += 1

    return res


print(find_positions([1, 2, 2, 3, 4, 5], 5))
# print(find_positions([2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4], 4))