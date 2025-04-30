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

from collections import deque

def is_same_tree(a, b):
    print("a")
    a.print_tree()
    print("b")
    b.print_tree()
    
    
    if a is None and b is None:
        return True

    if ((a is None and b) or
        (b is None and a)):
        return False

    q_a , q_b = deque(), deque()
    q_a.append(a)
    q_b.append(b)

    while q_a :
        node_a = q_a.popleft()
        node_b = q_b.popleft()

        if node_a.val != node_b.val:
            return False

        if node_a.left and node_b.left:
            q_a.append(node_a.left)
            q_b.append(node_b.left)
        elif node_a.left is None and node_b.left is None:
            pass
        else:
            return False

        if node_a.right and node_b.right:
            q_a.append(node_a.right)
            q_b.append(node_b.right)
        elif node_a.right is None and node_b.right is None:
            pass
        else:
            return False

    return len(q_b) == 0

print(is_same_tree(root, root))
print(is_same_tree(root, n4))
print(is_same_tree(n4, root))
print(is_same_tree(n8, n1))



def is_same_tree_dfs(t1, t2):
    if not t1 and not t2:
        return True
    
    if ((not t1 and t2) or (not t2 and t1)):
        return False

    if t1.val != t2.val:
        return False
    
    return is_same_tree_dfs(t1.left, t2.left) and is_same_tree_dfs(t1.right, t2.right)


print(is_same_tree_dfs(root, root))
print(is_same_tree_dfs(root, n4))
print(is_same_tree_dfs(n4, root))
print(is_same_tree_dfs(n8, n1))
