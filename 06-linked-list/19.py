
#         v
# D 1 2 3 4 5
#       l     r

#   v
# D 4
# l   r

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
head = ListNode(1, n2)


def remove_nth(head, n):
    dummy = ListNode(0, head)
    left = dummy
    right = head

    # move fast pointer forward
    for _ in range(n):
        if right:
            right = right.next
        else:
            return head

    while right:
        right = right.next
        left = left.next
    
    left.next = left.next.next
    return dummy.next

head = remove_nth(head, 2)
while head:
    print(head.val)
    head = head.next


head = remove_nth(n5, 1)
print(head)
