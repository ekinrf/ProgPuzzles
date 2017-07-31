def mco(array):
    num_co = 0
    cur_co = 0
    for num in array:
        if num is 0:
            num_co = max(num_co, cur_co)
            cur_co = 0
        else:
            cur_co += 1
    return max(cur_co, num_co)


print(mco([1, 1, 0, 1, 1, 1]))
