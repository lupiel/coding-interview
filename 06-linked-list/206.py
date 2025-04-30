#    h
#    A->B->C->
# p  c  t


#    h
#  <-A  B->C->
# p  c  t


def reverse_list(head):

    prev = None
    curr = head
    
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    return prev

