from typing import List


# going from right to left, prune when not equal
def is_solvable(words: List[str], result: str):
    # ch_pos_to_end is like a row number, iter_idx is the column number
    def backtrack(ch_pos_to_end, num_choices, iter_idx, lhs, rhs):
        if ch_pos_to_end > len(result):
            print(num_mappings)
            return True

        mul = pow(10, ch_pos_to_end - 1)
        if iter_idx < len(words):
            word = words[iter_idx]
            idx = len(word) - ch_pos_to_end
            if idx >= 0:
                if word[idx] not in num_mappings:
                    for n in num_choices:
                        if n == 0 and word[idx] == word[0]:
                            continue
                        num_mappings[word[idx]] = n
                        if backtrack(ch_pos_to_end, num_choices - {n}, iter_idx + 1,
                                     lhs + num_mappings[word[idx]] * mul,
                                     rhs):
                            return True
                        del num_mappings[word[idx]]
                else:
                    return backtrack(ch_pos_to_end, num_choices, iter_idx + 1, lhs + num_mappings[word[idx]] * mul, rhs)
            else:
                return backtrack(ch_pos_to_end, num_choices, iter_idx + 1, lhs, rhs)
        elif iter_idx == len(words):
            idx = len(result) - ch_pos_to_end
            if result[idx] not in num_mappings:
                for n in num_choices:
                    if n == 0 and result[idx] == result[0]:
                        continue
                    new_rhs = rhs + n * mul
                    if not str(lhs).endswith(str(new_rhs)):  # consider using //10 to optimise
                        continue
                    num_mappings[result[idx]] = n
                    if backtrack(ch_pos_to_end + 1, num_choices - {n}, 0, lhs, new_rhs):
                        return True
                    del num_mappings[result[idx]]
            else:
                added = num_mappings[result[idx]]
                if not str(lhs).endswith(str(rhs + added * mul)):
                    return False
                return backtrack(ch_pos_to_end + 1, num_choices, 0, lhs, rhs + added * mul)
        return False

    max_len_words = max([len(w) for w in words])
    if max_len_words > len(result):
        return False
    num_mappings = {}
    nums = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0}
    # num_mappings = {'S': 6, 'I': 5, 'X': 0, 'E': 8, 'V': 7, 'N': 2, 'T': 1}
    # nums = {3, 4}
    return backtrack(1, nums, 0, 0, 0)


words = ["AA", "BB"]
result = "AA"
print(is_solvable(words, result))

words = ["AB", "AB"]
result = "CD"
print(is_solvable(words, result))

words = ["SEND", "MORE"]
result = "MONEY"
print(is_solvable(words, result))

words = ["SIX", "SEVEN", "SEVEN"]
result = "TWENTY"
print(is_solvable(words, result))

words = ["THIS", "IS", "TOO"]
result = "FUNNY"
print(is_solvable(words, result))

words = ["LEET", "CODE"]
result = "POINT"
print(is_solvable(words, result))

words = ["BUT", "ITS", "STILL"]
result = "FUNNY"
print(is_solvable(words, result))
