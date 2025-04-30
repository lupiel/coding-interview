def has_cycle(head):

    curr = head
    seen = set()

    while curr:
        if curr in seen:
            return True

        seen.add(curr)
        cur = cur.next

    return False