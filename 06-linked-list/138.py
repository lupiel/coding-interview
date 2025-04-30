# original:
#      1 2 3 4 5 6 null
# addr a b c d e f


# copy:
#      1 2 3 4 5 6 null
# addr A B C D E F

# hash_map = {
#     a: A,
#     b: B,
#     ...
# }

def deep_copy_random_list(head):
    if head == None:
        return None

    node_map = {}

    curr = head
    while curr:
        node_map[curr] = ListNode(curr.val)
        curr = curr.next

    curr = head
    while curr:
        node_map[curr].next = node_map[curr.next]
        node_map[curr].rand = node_map[curr.rand]
        curr = curr.next


    return node_map[head]