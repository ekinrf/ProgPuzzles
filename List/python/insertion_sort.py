from python.list_node import ListNode


# everytime we find the next val is smaller than cur value
# set the cur to the beginning and trying to find the insert pos
# then move cur to end of the current partially sorted list
def insertion_sort(head: ListNode):
    prev = pre_head = ListNode(0, head)
    cur = head
    while cur:
        next = cur.next
        if next and next.val < cur.val:
            while prev.next and prev.next.val < next.val:
                prev = prev.next
            prev.next, next.next, cur.next, prev = next, prev.next, next.next, pre_head
        else:
            cur = next
    return pre_head.next


# 4, 2, 1, 3
head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
print(insertion_sort(head))

head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
insertion_sort(head)