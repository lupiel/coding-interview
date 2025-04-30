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




def is_sub_tree(tree, sub_tree):
    def is_same_tree(t1, t2):
        if not t1 and not t2:
            return True

        if ((not t1 and t2) or (t1 and not t2)):
            return False

        if t1.val != t2.val:
            return False

        return is_same_tree(t1.left, t2.left) and is_same_tree(t1.right, t2.right)

    def found_sub_tree(t, s):
        if not t:
            return False
        if is_same_tree(t, s):
            return True

        return (is_same_tree(t.left, s)
            or is_same_tree(t.right, s))

    return found_sub_tree(tree, sub_tree)

print(is_sub_tree(root, root))
print(is_sub_tree(root, root.left))
print(is_sub_tree(root.right, root))
print(is_sub_tree(root, n4))
print(is_sub_tree(root, None))
print(is_sub_tree(None, None))
print(is_sub_tree(None, root))



