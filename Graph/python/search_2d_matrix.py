from typing import List


def search_matrix(matrix: List[List[int]], target):
    def translate_1d_idx_to_coord(idx):
        return idx // num_x, idx % num_x

    if not matrix:
        return False
    num_x, num_y = len(matrix[0]), len(matrix)
    start, end = 0, num_x * num_y - 1
    while start <= end:
        mid = start + (end - start) // 2
        mid_x, mid_y = translate_1d_idx_to_coord(mid)
        if matrix[mid_x][mid_y] == target:
            return True
        elif matrix[mid_x][mid_y] < target:
            start = mid + 1
        elif matrix[mid_x][mid_y] > target:
            end = mid - 1
    return False


matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
target = 3
print(search_matrix(matrix, target))

matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
target = 13
print(search_matrix(matrix, target))
