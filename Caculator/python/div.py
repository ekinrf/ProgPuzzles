# 29. Divide Two Integers
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


print(div(7, -3))
print(div(-1, -1))
print(div(-2147483648, -1))
