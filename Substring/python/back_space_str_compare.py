# O(1) space requires doing comparison in place
# but when find a different character, we don't know if it will be deleted or not
# so we traverse backwards, then when we find a character we are sure they are not deleted.
def back_str_comp(s, t):
    i, j = len(s) - 1, len(t) - 1
    back_s = back_t = 0
    while True:
        while i >= 0 and (back_s or s[i] == '#'):
            if s[i] == '#':
                back_s += 1
            else:  # back_s > 0:
                back_s -= 1
            i -= 1
        while j >= 0 and (back_t or t[j] == '#'):
            if t[j] == '#':
                back_t += 1
            elif back_t > 0:
                back_t -= 1
            j -= 1

        if not (i >= 0 and j >= 0 and s[i] == t[j]):
            return i == j == -1
        else:
            i, j = i - 1, j - 1
