from python.list_node import ListNode


def reverse(head: ListNode):
    prev = None
    cur = head
    while cur:
        # next = cur.next
        # cur.next = prev
        # prev = cur
        # cur = next
        prev, cur, cur.next = cur, cur.next, prev
    return prev


# a -> b -> c
def reverse_between(head: ListNode, m, n):
    fake_head = ListNode(0, head)
    counter = 1
    rev_head, cur = fake_head, head
    while counter < m:
        counter += 1
        rev_head = cur
        cur = cur.next
    prev, rev_start = None, cur
    while counter < n:
        counter += 1
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    rev_head.next = cur
    rev_start.next = cur.next
    if prev:
        cur.next = prev
    return fake_head.next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reverse_between(head, 2, 4)

head = ListNode(3, ListNode(5))
reverse_between(head, 1, 2)
