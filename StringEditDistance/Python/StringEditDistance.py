def memo(fn):
    cache = {}
    missed = object()

    def query(*args):
        result = cache.get(args, missed)
        if result is missed:
            result = cache[args] = fn(*args)
        return result

    return query


@memo
def cal_edit_distance(ori, tar):
    def edit_tuple(old, distance, path):
        return old[0] + distance, old[1] + "\n" + path

    if not ori:
        return len(tar), "add %s" % tar
    if not tar:
        return len(ori), "remove %s" % ori
    ori_head, ori_rest, tar_head, tar_rest = ori[0], ori[1:], tar[0], tar[1:]
    edit_op_dis = cal_edit_distance(ori_rest, tar_rest)
    if ori_head != tar_head:
        edit_op_dis = edit_tuple(edit_op_dis, 1, "replace %s with %s" % (ori_head, tar_head))
    del_op_dis = cal_edit_distance(ori_rest, tar)
    del_op_dis = edit_tuple(del_op_dis, 1, "delete %s" % ori_head)
    add_op_dis = cal_edit_distance(ori, tar_rest)
    add_op_dis = edit_tuple(add_op_dis, 1, "add %s" % tar_head)
    return min(edit_op_dis, del_op_dis, add_op_dis, key=lambda e: e[0])


from collections import defaultdict


def edit_distance_norec(ori, tar):
    ed = defaultdict(dict)
    ed[0] = {i: i for i in range(len(tar) + 1)}
    for i in range(len(ori) + 1):
        ed[i][0] = i
    for i in range(1, len(ori) + 1):
        for j in range(1, len(tar) + 1):
            del_op = ed[i - 1][j] + 1
            add_op = ed[i][j - 1] + 1
            edit_op = ed[i - 1][j - 1] if ori[i - 1] == tar[j - 1] else ed[i - 1][j - 1] + 1
            ed[i][j] = min(del_op, add_op, edit_op)
    return ed[len(ori)][len(tar)]

if __name__ == '__main__':
    print(cal_edit_distance("fang", "renf")[0])
    print(edit_distance_norec("fang", "renf"))
