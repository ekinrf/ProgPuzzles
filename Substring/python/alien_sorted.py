from typing import List


def is_alien_sorted(words: List[str], order: str):
    orders = {c:i for i, c in enumerate(order)}

    for w1, w2 in zip(words, words[1:]):
        if len(w1) > len(w2) and w1[:len(w2)] == w2:
            return False
        for c1, c2 in zip(w1, w2):
            if orders[c1] > orders[c2]:
                return False
            if orders[c1] < orders[c2]:
                break
    return True
