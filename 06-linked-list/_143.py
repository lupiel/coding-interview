# d 1 2 3 4 5
#       1
#             2 

# d 1 2 3 4
#     1
#         2

# starting from dummy
# until h2 and h2.next

# example 1:
# d 1 2 3 4 5
#       1
#             2 

# 1 2 3
# 4 5

# 1 2 3
# 5 4

# 1 5 2 4 3

# example 2:
# 1 2 3 4

# 1 2       # split in two
# 3 4

# 1 2       # reverse 2nd
# 4 3

# 1 4 2 3   # merge lists

def print_list(head):
    curr = head
    ret = []

    while curr:
        ret.append(curr.val)
        curr = curr.next
    print(','.join([str(i) for i in ret]))

class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head):
    if head is None:
        return None

    dummy = Node()
    dummy.next = head

    # split in two
    h1 = h2 = dummy
    while h2 and h2.next:        
        h1 = h1.next
        h2 = h2.next.next
    
    h2 = h1.next
    h1.next = None
    h1 = head
    
    # reverse h2
    curr = h2
    prev = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    h2 = prev

    # merge h1 and h2
    # 1 5 2 4 3
    #       c 

    # 1 2 3
    #     c1
    # 5 4
    #     c2



    dummy = Node()
    curr = dummy

    c1, c2 = h1, h2
    while c1:
        curr.next = c1
        curr = curr.next
        c1 = c1.next
        if c2:
            curr.next = c2
            curr = curr.next
            c2 = c2.next

    return dummy.next

n5 = Node(5)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
head = Node(1, n2)


print_list(head)

print_list(reorder_list(head))
