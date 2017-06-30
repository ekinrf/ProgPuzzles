# stones is a set of tuples with (weight, value)


# Unbounded KP. Why greedy does not work??
# Python’s default arguments are evaluated once when the function is defined, not each time the function is called
def kp(weight_limit, stones, kp_cache=None):
    if kp_cache is None:
        kp_cache = {}
    if weight_limit not in kp_cache:
        if weight_limit <= 0:
            return 0
        else:
            kp_cache[weight_limit] = max(
                [kp(weight_limit - w, stones, kp_cache) + v for w, v in stones if weight_limit >= w], default=0)
    return kp_cache[weight_limit]


# 01KP
# use a list instead of set here
# so we can use the length of the list
# to identify the state of the list
# since we always remove the last from the list
def kp_01(weight_limit, stones, kp_cache=None):
    from collections import defaultdict
    if not kp_cache:
        kp_cache = defaultdict(dict)
    if weight_limit <= 0 or not stones:
        return 0
    elif len(stones) not in kp_cache[weight_limit]:
        stones_left = len(stones)
        last_stone = stones[-1]
        kp_cache[weight_limit][stones_left] = max(kp_01(weight_limit, stones[:-1]),
                                                  kp_01(weight_limit - last_stone[0], stones[:-1]) + last_stone[1]
                                                  if weight_limit - last_stone[0] >= 0 else 0)
    return kp_cache[weight_limit][stones_left]


print(kp(8, {(1, 10), (3, 40), (4, 50), (5, 70)}))
print(kp(17, {(6, 6), (10, 9), (5, 1)}))

print(kp_01(10, [(4, 9), (3, 6), (5, 1), (2, 4), (5, 1)]))
print(kp_01(9, [(4, 20), (3, 6), (4, 20), (2, 4)]))
print(kp_01(10, [(2, 6), (2, 3), (6, 5), (5, 4), (4, 6)]))
