# make sure ) always has a ( before
# remove all the ) without (
# and then go from last to the front remove ( without matching )
def min_remove_make_valid(s: str):
    res = ''
    start_parentheses_count = 0
    for ch in s:
        if ch == '(':
            start_parentheses_count += 1
            res += ch
        elif ch == ')':
            if start_parentheses_count - 1 >= 0:
                start_parentheses_count -= 1
                res += ch
        else:
            res += ch
    if start_parentheses_count == 0:
        return res
    else:
        ret = ''
        # going backwards remove first few ( s
        # not need to check if there are matching ),
        # because ) without ( are already removed
        # in the first iteration
        for idx, ch in enumerate(reversed(res)):
            if ch == '(':
                if start_parentheses_count > 0:
                    start_parentheses_count -= 1
                else:
                    ret = ch + ret
            else:
                ret = ch + ret
        return ret



def min_remove_make_valid_stack(s: str):
    start_p_stack = []
    invalid_idx = set()
    for idx, ch in enumerate(s):
        if ch == '(':
            start_p_stack.append(idx)
        elif ch == ')':
            if start_p_stack:
                start_p_stack.pop()
            else:
                invalid_idx.add(idx)
    while start_p_stack:
        invalid_idx.add(start_p_stack.pop())

    res = ''
    for idx, ch in enumerate(s):
        if idx not in invalid_idx:
            res += ch
    return res


def minRemoveToMakeValid(s: str) -> str:
        final_result = []
        opening = 0

        for ch in s:
            if ch == '(':
                opening += 1
            elif ch == ')':
                if opening > 0:
                    opening -= 1
                else:
                    continue
            final_result.append(ch)

        i = len(final_result) - 1
        while opening > 0:
            if final_result[i] == '(':
                del final_result[i]
                opening -= 1
            i -= 1

        return ''.join(final_result)


print(min_remove_make_valid('lee(t(c)o)de)'))
print(min_remove_make_valid('a)b(c)d'))
print(min_remove_make_valid('(a(b(c)d)'))

print(min_remove_make_valid_stack('lee(t(c)o)de)'))
print(min_remove_make_valid_stack('a)b(c)d'))
print(minRemoveToMakeValid('((a)((b(cd))'))
