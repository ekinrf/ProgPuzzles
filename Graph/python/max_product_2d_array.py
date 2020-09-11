from typing import List


# because the product of 2 negative numbers could be bigger
# so in our recursion function we can return 2 numbers
# one is the smallest number (negative), one is the largest number
def max_product_path(arr: List[List[int]]):
    if not arr:
        return 0
    res = 0
    # https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
    dp = [v[:] for v in [[(0, 0)] * len(arr[0])] * len(arr)]
    dp[0][0] = (arr[0][0], arr[0][0])
    for i in range(1, len(arr[0])):
        dp[0][i] = (arr[0][i] * arr[0][i - 1], arr[0][i] * arr[0][i - 1])
    for i in range(1, len(arr)):
        dp[i][0] = (arr[i][0] * arr[i - 1][0], arr[i][0] * arr[i - 1][0])
    for x in range(1, len(arr[0])):
        for y in range(1, len(arr)):
            possible_vals = [arr[x][y] * val for val in [*dp[x - 1][y], *dp[x][y - 1]]]
            dp[x][y] = (min(possible_vals), max(possible_vals))
            res = max(dp[x][y][1], res)
    return res


print(max_product_path([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(max_product_path([[1, -2, 3], [4, -5, 6], [-7, -8, 9]]))
