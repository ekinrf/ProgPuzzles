# recursion only, takes too much time
# can improve using cache
def num_of_ways(s: str):
    if not s:
        return 1
    elif s[0] == '0':
        return 0
    else:
        res = num_of_ways(s[1:])
        if len(s) > 1:
            if s[0] == '1':
                res += num_of_ways(s[2:])
            elif s[0] == '2' and int(s[1]) <= 6:
                res += num_of_ways(s[2:])
        return res


print(num_of_ways('22262'))
print(num_of_ways('2101'))
print(num_of_ways('1201234'))
print(num_of_ways('123123'))

# dp[i] = dp[i + 1] + dp[i + 2] if s[i] != '0' or dp[i + 2] if valid
# dp[n] = 1 if dp[0] != '0' or 0
# dp[n - 1] = 0 if s[n] = 0 or 1
def num_of_ways_dp(s: str):
    if s[0] == '0':
        return 0
    if len(s) == 1:
        return 1
    if len(s) >= 2:
        plus_1, plus_2 = 2, 1
        if s[-1] == '0':
            plus_2 = 0
            plus_1 = 1
        if s[-2] == '0':
            plus_1 = 0
        elif int(s[-2:]) > 26:
            plus_1 = 0 if s[-1] == '0' else 1

        i = len(s) - 3
        while i >= 0:
            _plus_2 = plus_1
            if s[i] == '0':
                plus_1 = 0
            elif s[i] == '2' and int(s[i + 1]) <= 6:
                plus_1 = plus_1 + plus_2
            elif s[i] == '1':
                plus_1 = plus_1 + plus_2
            else:
                plus_1 = plus_1
            plus_2 = _plus_2
            i -= 1
        return plus_1

print('====')

print(num_of_ways_dp('22262'))
#
print(num_of_ways_dp("11111111"))

print(num_of_ways_dp('2101'))
#
print(num_of_ways_dp('1201234'))
print(num_of_ways_dp('123123'))
print(num_of_ways_dp('230'))
