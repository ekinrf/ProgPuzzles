def letter_combination(digits: str):
    letter_mapping = {
        2: list('abc'),
        3: list('def'),
        4: list('ghi'),
        5: list('jkl'),
        6: list('mno'),
        7: list('pqs'),
        8: list('tuv'),
        9: list('wxyz')
    }

    def _gen_comb(cur_comb, cur_idx):
        if cur_idx == len(digits):
            res.append(cur_comb)
        else:
            for l in letter_mapping[int(digits[cur_idx])]:
                _gen_comb(cur_comb + l, cur_idx + 1)

    res = []
    _gen_comb('', 0)
    return res


print(letter_combination('23'))