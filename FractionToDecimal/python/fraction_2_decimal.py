def frac_to_dec(numerator, denominator):
    fracs = []
    remainders = {}  # num -> index in fracs

    def div(dividend, divisor):
        _quotient = int(dividend / divisor)
        _remainder = dividend - (_quotient * divisor)
        return _quotient, _remainder * 10

    def iterate(numer, denom):
        if numer in remainders:
            i = remainders[numer]
            return i, True
        else:
            _quotient, _remainder = div(numer, denom)
            remainders[numer] = len(fracs)
            fracs.append(_quotient)
            if _remainder:
                return iterate(_remainder, denom)
            else:
                return len(fracs), False

    def stringify(nums):
        recurring = nums[1]
        index = nums[0]
        ret = ""
        for x in fracs[0:index]:
            ret += str(x)
        if recurring:
            ret += "("
        for x in fracs[index:]:
            ret += str(x)
        if recurring:
            ret += ")"
        return ret

    if not numerator:
        return "0"
    if numerator * denominator < 0:
        return "-" + frac_to_dec(abs(numerator), abs(denominator))
    if denominator:
        quotient, remainder = div(numerator, denominator)
        if remainder:
            return str(quotient) + "." + stringify(iterate(remainder, denominator))
        else:
            return str(quotient)

print(frac_to_dec(-50, 8))
print(frac_to_dec(4, 333))
print(frac_to_dec(0, 8))
print(frac_to_dec(2, 1))
print(frac_to_dec(1, 5))
