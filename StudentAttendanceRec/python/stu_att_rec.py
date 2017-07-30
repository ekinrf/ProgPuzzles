from math import pow

mod_fac = 1000000007


# f(n) = p(n) + l(n) + a(n)
# p(n) = p(n - 1) + l(n - 1) + a(n - 1)
# l(n) = p(n - 1) + a(n - 1) + p(a - 2) + a(n - 2)
# NOTE l(n) = p(n - 1) + a(n - 1) + l(n - 1) - l(n - 2) is WRONG
# a(n) = no_a_p(n - 1) + no_a_l(n - 1)
# no_a_p(n) = no_a_p(n - 1) + no_a_l(n - 1)
# so -> a(n) = no_a_p(n)
# no_a_l(n) = no_a_p(n - 1) + no_a_p(n - 2)
# so -> a(n) = a(n - 1) + a(n - 2) + a(n - 3)
# p(1) = 1
# l(1) = 1; l(2) = 3
# a(1) = 1; a(2) = 2; a(3) = 4


def memo(fn):
    cache = {}
    missed = object()

    def query(*args):
        result = cache.get(args, missed)
        if result is missed:
            result = cache[args] = fn(*args)
        return result

    return query


def num_rewardable_rec(n):
    @memo
    def a(n):
        if n < 3:
            return n
        elif n is 3:
            return 4
        else:
            return a(n - 1) % mod_fac + a(n - 2) % mod_fac + a(n - 3) % mod_fac

    @memo
    def l(n):
        if n is 1:
            return 1
        elif n is 2:
            return 3
        else:
            return p(n - 1) % mod_fac + a(n - 1) % mod_fac + a(n - 2) % mod_fac + p(n - 2) % mod_fac

    @memo
    def p(n):
        if n is 1:
            return 1
        else:
            return p(n - 1) % mod_fac + l(n - 1) % mod_fac + a(n - 1) % mod_fac

    return a(n) + l(n) + p(n)


def num_rewardable_no_rec(n):
    k = n
    if n < 3:
        k = 3

    a = [0] * (k + 1)
    l = [0] * (k + 1)
    p = [0] * (k + 1)
    a[1] = p[1] = l[1] = 1
    a[2] = 2
    a[3] = 4
    l[2] = 3

    for i in range(2, k + 1):
        a[i - 1] %= mod_fac
        l[i - 1] %= mod_fac
        p[i - 1] %= mod_fac

        if i > 3:
            a[i] = a[i - 1] + a[i - 2] + a[i - 3]
        if i > 2:
            l[i] = p[i - 1] + a[i - 1] + a[i - 2] + p[i - 2]
        p[i] = p[i - 1] + a[i - 1] + l[i - 1]

    return (a[n] + l[n] + p[n]) % mod_fac


# NonA(n) = NonA(n - 1) +  XXXP
#           NonA(n - 2) +  XXPL
#           NonA(n - 3)    XPLL
#           XLLL is invalid
# NonA(0) = 1  not accurate but for A(n) purpose
# NonA(1) = 2
# NonA(2) = 4
# NonA(3) = 7 (pow(2, 3) - 1 )
# A(n) = sum(NonA(i) * NonA(n - i - 1)) where i = {0 to n - 1}
# A(0) = 1
# f(n) = NonA(n) + A(n)
def num_rewardable(n):
    mod_fac = 1000000007
    if n is 0:
        return 0
    if n is 1:
        return 3

    non_a = [1, 2, 4]
    i = 3
    while i <= n:
        non_a.append((non_a[i - 1] + non_a[i - 2] + non_a[i - 3]) % mod_fac)
        i += 1
    result = non_a[n]
    for i in range(n):
        result += non_a[i] * non_a[n - i - 1] % mod_fac
        result %= mod_fac
    return result


def check_record(record):
    found_a = False
    continuous_l_count = 0
    for c in record:
        if c.upper() == 'L':
            continuous_l_count += 1
            if continuous_l_count >= 3:
                return False
        elif c.upper() == 'A':
            continuous_l_count = 0
            if found_a:
                return False
            else:
                found_a = True
        else:
            continuous_l_count = 0
    return True

# print(num_rewardable_rec(3))
# print(num_rewardable_rec(2))
# print(num_rewardable_rec(4))
print(num_rewardable_no_rec(61))
print(num_rewardable_no_rec(100))
print(num_rewardable_no_rec(98765))

print(num_rewardable(100))
print(check_record('PPALLL'))