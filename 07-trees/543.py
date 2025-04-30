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


#         A
#       B   
#     D   E
#    H     F
#   I       G
#            J

# I H D B E F G J
# to do return max(f(root.left), f(root.right))


def diameter(root):
    longest_paht_seen = [0]

    def max_depth(node, curr_depth = 0):
        if node is None:
            return 0
        curr_depth += 1
        if node.left is None and node.right is None:
            return curr_depth

        return max(
            max_depth(node.left, curr_depth),
            max_depth(node.right, curr_depth)
        )

    def max_path(root):
        if root is None:
            return 0
        
        if root.left is None:
            n_left = 0
        else:
            n_left = max_depth(root.left)

        if root.right is None:
            n_right = 0
        else:
            n_right = max_depth(root.right)

        max_p = n_left + n_right
        longest_paht_seen[0] = max(longest_paht_seen[0], max_p)
        return max_p

    max_path(root.left)
    max_path(root.right)
    return longest_paht_seen[0]

print(diameter(root))











def diameter2(root):
    longest_paht_seen = [0]


    def dfs(node):
        if node is None:
            return 0
        
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)
        diameter = left_depth + right_depth
        longest_paht_seen[0] = max(longest_paht_seen[0], diameter)

        return 1 + max(
            left_depth,
            right_depth
        )
    
    dfs(root.left)
    dfs(root.right)
    return longest_paht_seen[0]
            


print(diameter2(root))