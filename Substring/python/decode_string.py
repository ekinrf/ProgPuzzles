from collections import deque


# using a global queue to keep on where we are when traversing the string
def decode_str(s: str):
    def _decode(s_queue, repeater):
        if not repeater:
            repeater = 1
        repeating_seq = ''
        next_repeater = 0
        while s_queue:
            c = s_queue.popleft()
            if c.isdigit():
                next_repeater = next_repeater * 10 + int(c)
            elif c == '[':
                repeating_seq += _decode(s_queue, next_repeater)
                next_repeater = 0
            elif c == ']':
                return repeater * repeating_seq
            else:
                repeating_seq += c
        return repeater * repeating_seq

    s_queue = deque(s)
    return _decode(s_queue, 1)


def decode_str_stack(s: str):
    cur_num = 0
    cur_str = ''
    a_stack = []
    for c in s:
        if c.isdigit():
            cur_num = cur_num * 10 + int(c)
        elif c == '[':
            a_stack.append(cur_num)
            a_stack.append(cur_str)
            cur_num = 0
            cur_str = ''
        elif c == ']':
            pre_str = a_stack.pop()
            pre_num = a_stack.pop()
            cur_str = pre_str + pre_num * cur_str
        else:
            cur_str += c
    return cur_str


print(decode_str("3[a2[c]]"))
print(decode_str("abc3[cd]xyz"))
print(decode_str("3[a]2[bc]"))

print(decode_str("100[leetcode]"))

print(decode_str_stack("abc3[cd]xyz"))
print(decode_str_stack("3[a2[c]]"))
