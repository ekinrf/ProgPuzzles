def memo(x, y, f):
    cache = {}

    def query():
        if (x, y) not in cache:
            cache[(x, y)] = f(x, y)
        return cache[(x, y)]
    return query()


def cal_edit_distance(ori, tar):

    def edit_tuple(old, distance, path):
        return old[0] + distance, old[1] + "\n" + path

    if not ori:
        return len(tar), "add %s" % tar
    if not tar:
        return len(ori), "remove %s" % ori
    ori_head, ori_rest, tar_head, tar_rest = ori[0], ori[1:], tar[0], tar[1:]
    edit_op_dis = memo(ori_rest, tar_rest, cal_edit_distance)
    if ori_head != tar_head:
        edit_op_dis = edit_tuple(edit_op_dis, 1, "replace %s with %s" % (ori_head, tar_head))
    del_op_dis = memo(ori_rest, tar, cal_edit_distance)
    del_op_dis = edit_tuple(del_op_dis, 1, "delete %s" % ori_head)
    add_op_dis = memo(ori, tar_rest, cal_edit_distance)
    add_op_dis = edit_tuple(add_op_dis, 1, "add %s" % tar_head)
    return min(edit_op_dis, del_op_dis, add_op_dis, key=lambda e: e[0])

print(cal_edit_distance("kitten", "sitting")[1])

