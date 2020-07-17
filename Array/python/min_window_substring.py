from collections import defaultdict


def min_window(s: str, t: str):
    ch_in_t = defaultdict(int)
    for c in t:
        ch_in_t[c] += 1

    num_ch_needed = len(ch_in_t)
    min_window_len = len(s) + 1
    i, j = 0, 0
    candi_left, candi_right = i, j
    while j < len(s):
        if s[j] in ch_in_t:
            ch_in_t[s[j]] -= 1
            if ch_in_t[s[j]] == 0:
                num_ch_needed -= 1
        j += 1
        while num_ch_needed == 0:
            if min_window_len > j - i:
                candi_left, candi_right = i, j
                min_window_len = j - i
            if s[i] in ch_in_t:
                ch_in_t[s[i]] += 1
                if ch_in_t[s[i]] == 1:
                    num_ch_needed += 1
            i += 1

    if min_window_len <= len(s):
        return s[candi_left: candi_right]
    else:
        return ''


S = "ADOBECODEBANC"
T = "ABC"
print(min_window(S, T))