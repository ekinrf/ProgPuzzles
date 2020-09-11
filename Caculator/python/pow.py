# x to the power of n
def my_pow(x: float, n: int):
    if n == 0:
        return 1
    if n < 0:
        return 1 / my_pow(x, -n)
    if n % 2:
        return x * my_pow(x, n - 1)
    return my_pow(x * x, n/2)


def my_pow_iter(x: float, n: int):
    negative = n < 0
    n = abs(n)
    res, tmp = 1, x
    while n > 0:
        if n % 2:
            res = res * tmp
        tmp *= tmp
        n = n // 2
    return 1 / res if negative else res


print(my_pow(2, -10))
print(my_pow_iter(2, 10))