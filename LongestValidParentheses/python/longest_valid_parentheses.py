from collections import deque


def longest_valid_parentheses(input_seq):
    par_stack = []
    for i, c in enumerate(input_seq):
        poped = False
        if c == ')':
            if par_stack:
                head_idx = par_stack[-1]
                if input_seq[head_idx] is not c:
                    par_stack.pop()
                    poped = True
        if not poped:
            par_stack.append(i)
    max_lvp = 0
    prev_idx = seq_len = len(input_seq)
    if par_stack:
        while par_stack:
            idx = par_stack.pop()
            max_lvp = max(max_lvp, prev_idx - idx - 1)
            prev_idx = idx
        max_lvp = max(prev_idx, max_lvp)
    else:
        max_lvp = seq_len

    return max_lvp

print(longest_valid_parentheses('()()()()()(())(((()'))
print(longest_valid_parentheses(')'))

