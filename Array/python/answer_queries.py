from typing import List

import bisect


def answer_quires(quires: List[List[int]], n: int):
    true_states = []
    res = []
    for q in quires:
        if q[0] == 1:
            bisect.insort(true_states, q[1])
        else:
            ans = -1
            if true_states:
                pos = bisect.bisect_left(true_states, q[1])
                if pos != len(true_states):
                    ans = true_states[pos]
            res.append(ans)
    return res


print(answer_quires([[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]], 5))
