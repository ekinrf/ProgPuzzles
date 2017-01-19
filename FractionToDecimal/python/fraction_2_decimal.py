def frac_to_dec(numerator, denominator):
    fracs = []
    remainders = []

    def div(dividend, divisor):
        _whole = int(dividend / divisor)
        _remainder = dividend - (_whole * divisor)
        return _whole, _remainder * 10

    def iterate(numer, denom):
        if numer in remainders:
            i = remainders.index(numer)
            return i, True
        else:
            whole, remainder = div(numer, denom)
            remainders.append(numer)
            fracs.append(whole)
            if remainder:
                return iterate(remainder, denom)
            else:
                return len(fracs), False

    def stringfy(nums):
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
        whole, remainder = div(numerator, denominator)
        if whole:
            if remainder:
                return str(whole) + "." + stringfy(iterate(remainder, denominator))
            else:
                return str(whole)
        else:
            return "0." + stringfy(iterate(remainder, denominator))

print(frac_to_dec(-50, 8))
