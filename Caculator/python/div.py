# 29. Divide Two Integers
# Binary Search: Give dividend / divisor = 1
# if divisor + divisor > dividend and divisor < dividend
# we keep grow the real divisor by timing 2 (adding itself)
def div(dividend: int, divisor: int) -> int:
    def _div_rec(dividend, divisor):
        if divisor > dividend:
            return 0
        else:
            res = 1
            cur_sum = divisor
            while cur_sum + cur_sum < dividend:
                cur_sum += cur_sum
                res += res
            return res + _div_rec(dividend - cur_sum, divisor)

    if dividend < -2147483648 or dividend > 2147483647:
        return 2147483647
    elif dividend == -2147483648 and divisor == -1:
        return 2147483647
    equal_sign = (dividend > 0) == (divisor > 0)
    dividend = abs(dividend)
    divisor = abs(divisor)

    res = _div_rec(dividend, divisor)
    return res if equal_sign else -res


# Same idea but use less space
def div_2(dividend, divisor):
    ret = 0
    sign = (dividend > 0) == (divisor > 0)
    dividend, divisor = abs(dividend), abs(divisor)
    while dividend >= divisor:
        divisor_to_try, multiplier = divisor, 1
        while dividend >= divisor_to_try:
            dividend -= divisor_to_try
            ret += multiplier
            divisor_to_try += divisor_to_try
            multiplier += multiplier
    return ret if sign else -ret


print(div(7, -3))
print(div_2(7, -3))

print(div(-1, -1))
print(div_2(-1, -1))

print(div(-2147483648, -1))
print(div_2(-2147483648, -1))
