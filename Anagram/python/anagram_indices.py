from collections import defaultdict


# a O(n) solution given all string contains only english letters
def find_anagrams_indices(haystack, needle):
    needle_dict = defaultdict(int)
    n_len = match_count = len(needle)
    h_len = len(haystack)

    for ch in needle:
        needle_dict[ch] += 1

    indcies = []

    # sliding window
    left = right = 0
    while left <= right < h_len:
        if right - left >= n_len:
            needle_dict[haystack[left]] += 1
            if needle_dict[haystack[left]]:
                match_count += 1
            left += 1

        ch = haystack[right]
        if needle_dict[ch]:
            match_count -= 1

        needle_dict[ch] -= 1

        if match_count == 0:
            indcies.append(left)

        right += 1

    return indcies

if __name__ == '__main__':
    print(find_anagrams_indices('bbbababaaabbbb', 'ab'))