# n & n - 1 always sets the least 1 to 0
def hamming_weight(n):
    cnt = 0
    while n:
        cnt += 1
        n = n & (n - 1)
    return cnt
