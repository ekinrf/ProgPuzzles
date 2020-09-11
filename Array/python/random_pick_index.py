from random import random
from typing import List


# reservior sampling:
# pick a element and then decide on whether to swap it based on number of occu
# everytime encounter a occu, chances to keep itis n - 1/ n
# so finally retention prob is 1 * (1/2) * (2/3)... (n-1)/n
def pick(nums: List[int], target):
    counter_occu = 0
    res = -1
    for i, n in enumerate(nums):
        if n == target:
            counter_occu += 1
            res = i if random() < 1 / counter_occu else res
    return res
