
l1 -> 1 4 8 9 9 
l2 -> 0 1 2 9 10
dummy -> 

def merge_lists(list1, list2):

    dummy = ListNode()
    curr = dummy

    while list1 and list2:

        if list1.val < list2.val:
            curr.next = list1
            curr = list1
            list1 = list1.next
        else:
            curr.next = list2
            curr = list2
            list2 = list2.next

    curr.next = list1 or list2

    return dummy.next