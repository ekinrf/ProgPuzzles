from typing import List


# use additional space
def set_matrix_zeros(matrix: List[List[int]]):
    z_rows = set()
    z_cols = set()
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == 0:
                z_rows.add(x)
                z_cols.add(y)

    for r in z_rows:
        matrix[r] = [0] * len(matrix[0])
    for c in z_cols:
        for x in range(len(matrix)):
            matrix[x][c] = 0
    return matrix


# set the start of row and col to 0 to mark the entire row/col needs to be 0s
# then second traversal the key is to not touch the first row / col,
# so traversing from row 1 col 1
# at last, handle first row and first col
# because of the way we mark 0s in the first traversal
# and we need to figure out if first col/row has 0 in the first traversal
def set_matrix_zeros2(matrix: List[List[int]]):
    first_col_has_zero, first_row_has_zero = False, False
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == 0:
                matrix[0][y] = 0
                matrix[x][0] = 0
                if not first_row_has_zero and x == 0:
                    first_row_has_zero = True
                if not first_col_has_zero and y == 0:
                    first_col_has_zero = True

    for x in range(1, len(matrix)):
        for y in range(1, len(matrix[0])):
            if matrix[x][0] == 0 or matrix[0][y] == 0:
                matrix[x][y] = 0

    if first_row_has_zero:
        matrix[0] = [0] * len(matrix[0])
    if first_col_has_zero:
        for x in range(len(matrix)):
            matrix[x][0] = 0
    return matrix


m = [[1,1,1],[1,0,1],[1,1,1]]
print(set_matrix_zeros(m))
m = [[1,1,1],[1,0,1],[1,1,1]]
print(set_matrix_zeros2(m))


m = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(set_matrix_zeros(m))
m = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(set_matrix_zeros2(m))

m = [[1,1,1],[0,1,2]]
print(set_matrix_zeros(m))
m = [[1,1,1],[0,1,2]]
print(set_matrix_zeros2(m))

