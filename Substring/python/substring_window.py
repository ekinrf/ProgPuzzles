from collections import defaultdict


def min_window(s, t):
    t_map = defaultdict(int)
    t_counter = len(t)
    for c in t:
        t_map[c] += 1
    start = end = 0
    min_window_len = len(s) + 1
    min_start = 0
    min_end = len(s)
    while end < len(s):
        if t_map[s[end]] > 0:
            t_counter -= 1
        t_map[s[end]] -= 1
        end += 1
        while t_counter is 0:
            if end - start < min_window_len:
                min_window_len = end - start
                min_start = start
                min_end = end

            if t_map[s[start]] >= 0:
                t_counter += 1
            t_map[s[start]] += 1
            start += 1
    if min_window_len > len(s):
        return ''
    else:
        return s[min_start: min_end]


def longest_substring_2_distinct_char(s):
    counter = start = end = 0
    s_map = defaultdict(int)
    max_start = max_end = max_len = 0
    while end < len(s):
        if s_map[s[end]] == 0:
            counter += 1
        s_map[s[end]] -= 1
        end += 1

        while counter > 2 and start < end:
            s_map[s[start]] += 1
            if s_map[s[start]] is 0:
                counter -= 1
            start += 1

        if counter is 2:
            if end - start > max_len:
                max_end = end
                max_start = start
                max_len = end - start

    return s[max_start: max_end]


def longest_substring_without_rep(s):
    start = end = counter = max_len = max_start = max_end = 0
    s_map = defaultdict(int)
    while end < len(s):
        if s_map[s[end]] < 0:
            counter += 1
        s_map[s[end]] -= 1
        end += 1
        while counter > 0 and start < end:
            if s_map[s[start]] < 0:
                counter -= 1
            s_map[s[start]] += 1
            start += 1
        if counter is 0 and end - start > max_len:
            max_len = end - start
            max_end = end
            max_start = start
    return s[max_start: max_end]


print(min_window('ADOBECODEBANC', 'ABC'))
print(longest_substring_2_distinct_char('abcbbbbcccbdddadacb'))
print(longest_substring_without_rep('abcabcbb'))
