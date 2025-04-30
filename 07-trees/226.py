class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode({self.val})"
    def __repr__(self):
        return f"TreeNode({self.val})"

    def print_tree(self):
        this_level = [self]
        while this_level:
            next_level = []
            str_level = []
            for n in this_level:
                str_level.append(n.val)
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            print(','.join([str(i) for i in str_level]))
            this_level = next_level
        print()



n7 = TreeNode(7)
n2 = TreeNode(2)
n11 = TreeNode(11, n7, n2)
n4 = TreeNode(4, n11)
n1 = TreeNode(1)
nn4 = TreeNode(4, left=None, right=n1)
n13 = TreeNode(13)
n8 = TreeNode(8, n13, nn4)
root = TreeNode(5, n4, n8)
root.print_tree()



#        4
#     2     7
#    1  3    9

# q [4]
# q [2, 7]
# q [7, 1, 3]
# q [1, 3, 9]
# q [3, 9]
# q [9]
# q []

from collections import deque

def bfs_invert(root):
    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

        node.left, node.right = node.right, node.left

    return root

bfs_invert(root).print_tree()