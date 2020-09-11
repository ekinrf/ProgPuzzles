def remove_dup(s: str):
    s_stack = []
    for ch in s:
        if s_stack and s_stack[-1] == ch:
            s_stack.pop()
        else:
            s_stack.append(ch)
    return ''.join(s_stack)


print(remove_dup('abbaca'))


# follow up, remove only if find duplicates occurring at the k times
# 2 stacks, one for number, the other for occurrence
def remove_dup_k(s, k):
    count_stack = []
    ch_stack = []
    for ch in s:
        if ch_stack and ch_stack[-1] == ch:
            if count_stack[-1] == k - 1:
                dup_count = count_stack.pop()
                ch_stack = ch_stack[:-dup_count]
                continue
            else:
                count_stack[-1] += 1
        else:
            count_stack.append(1)
        ch_stack.append(ch)
    return ''.join(ch_stack)


def remove_dup_k_2pt(s, k):
    ch_arr = list(s)
    left = right = 0
    while right < len(s):
        right += 1
        occ_count = 1
        while right < len(s) and ch_arr[right] == ch_arr[left]:
            occ_count += 1
            right += 1
            if occ_count == k:
                ch_arr[left] = ch_arr[right]
                left -= 1
                occ_count = 1
        left += 1
    return ch_arr[0:left]


print(remove_dup_k('abbaca', 2))
print(remove_dup_k_2pt('abbaca', 2))

print(remove_dup_k('abbbaaca', 3))
print(remove_dup_k_2pt('abbbaaca', 3))
