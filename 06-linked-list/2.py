
# 3 5 6     653
# 8 0 4 1  1408

# answer
# 1 6 0 2  2061

# iterate both lists at the same time
# add vals and save in a new node
# if vals > 9 carry over

# 9 9 9      999
# 9 9         99

# 8 9 0 1   1098    


def add_two_numbers(h1, h2):

    dummy = Node()
    c3 = dummy
    

    c1, c2 = h1, h2
    carry = 0

    while c1 or c2 or carry:
        a = 0 if c1 is None else c1.val
        b = 0 if c2 is None else c2.val
        s = a + b + carry

        sum_node = Node(math.mod(s, 10))
        carry = int((s)/10)
        c3.next = sum_node

        c1 = c1.next if c1 else None
        c2 = c2.next if c2 else None
        c3 = c3.next

    return dummy.next






