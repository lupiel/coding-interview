from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode({self.val})"
    def __repr__(self):
        return f"TreeNode({self.val})"


# 1. Depth First Search
class DFS:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return res

# 2. Iterative Depth First Search
class IDFS:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        
        return res


n7 = TreeNode(7)
n2 = TreeNode(2)
n11 = TreeNode(11, n7, n2)
n4 = TreeNode(4, n11)
n1 = TreeNode(1)
nn4 = TreeNode(4, left=None, right=n1)
n13 = TreeNode(13)
n8 = TreeNode(8, n13, nn4)
root = TreeNode(5, n4, n8)




# LeetCode 112. Path Sum
def has_path_sum(root, target_sum):
    if root is None:
        return False
    
    if(root.left is None and root.right is None and target_sum - root.val == 0):
        return True

    return has_path_sum(root.left, target_sum - root.val) or has_path_sum(root.right, target_sum - root.val)

print("DFS recursive", has_path_sum(root, 22))


#bfs solution
from collections import deque
def has_sum_bfs(root, target_sum):
    if root is None:
        return False
    
    q = deque() # [node, target_remaining]
    q.append([root, target_sum])

    while len(q) > 0:
        node, target_remaining = q.popleft()
        child_target_remaining = target_remaining - node.val

        if node.left is None and node.right is None and child_target_remaining == 0:
            return True
        if node.left:
            q.append([node.left, child_target_remaining])
        if node.right:
            q.append([node.right, child_target_remaining])
    return False

print("BFS", has_sum_bfs(root, 22))



#dfs solution
def has_sum_dfs(root, target_sum):
    if root is None:
        return False
    
    stack = [] # [node, sum_so_far]
    cur = root
    cur_sum = 0

    while cur or stack:
        while cur:
            cur_sum += cur.val
            stack.append([cur, cur_sum])
            cur = cur.left
        
        cur, cur_sum = stack.pop()
        if cur.right is None and cur.left is None:
            return True
        cur = cur.right

    return False

print("DFS", has_sum_dfs(root, 22))











































from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode({self.val})"
    def __repr__(self):
        return f"TreeNode({self.val})"


# # 1. Depth First Search
# class DFS:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []

#         def inorder(node):
#             if not node:
#                 return
            
#             inorder(node.left)
#             res.append(node.val)
#             inorder(node.right)
        
#         inorder(root)
#         return res

# # 2. Iterative Depth First Search
# class IDFS:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         stack = []
#         cur = root

#         while cur or stack:
#             while cur:
#                 stack.append(cur)
#                 cur = cur.left
#             cur = stack.pop()
#             res.append(cur.val)
#             cur = cur.right
        
#         return res


n7 = TreeNode(7)
n2 = TreeNode(2)
n11 = TreeNode(11, n7, n2)
n4 = TreeNode(4, n11)
n1 = TreeNode(1)
nn4 = TreeNode(4, left=None, right=n1)
n13 = TreeNode(13)
n8 = TreeNode(8, n13, nn4)
root = TreeNode(5, n4, n8)

def has_path_sum_bfs(root, target_sum):
    def bfs(node, sum):
        if node is None:
            return False
        if node.left is None and node.right is None:
            if sum-node.val == 0:
                return True
            else:
                return False

        return bfs(node.left, sum-node.val) or bfs(node.right, sum-node.val)


    return bfs(root, target_sum)
print("### has_path_sum_bfs")
print(has_path_sum_bfs(root, 22))
print(has_path_sum_bfs(root, 18))
print(has_path_sum_bfs(root, 27))
print(has_path_sum_bfs(root, 5))
print(has_path_sum_bfs(root, 9))
print(has_path_sum_bfs(root, 20))

def find_paths_sum_bfs(root, target_sum):
    ret, sol = [], []

    def bfs(node, sum):
        if not node:
            return

        sum = sum - node.val
        sol.append(node.val)
        if sum == 0 and node.left is None and node.right is None:
            ret.append(sol.copy())

        bfs(node.left, sum)
        bfs(node.right, sum)
        sol.pop()

    
    bfs(root, target_sum)
    return ret
print("### find_paths_sum_bfs")
print(find_paths_sum_bfs(root, 27))
print(find_paths_sum_bfs(root, 22))
print(find_paths_sum_bfs(root, 26))
print(find_paths_sum_bfs(root, 18))
print(find_paths_sum_bfs(root, 17))



#           5
#      4         8
#   11        13    4
# 7   2               1
from collections import deque

def has_path_sum_bfs(root, target_sum):
    q = deque()
    q.append([root, target_sum])

    while q:
        node, sum = q.popleft()
        if sum - node.val == target_sum and node.left is None and node.right is None:
            return True

        if node.left:
            q.append([node.left, sum - node.val])
        if node.right:
            q.append([node.right, sum - node.val])

    return False
print("### has_path_sum_bfs")
print(has_path_sum_bfs(root, 22))
print(has_path_sum_bfs(root, 18))
print(has_path_sum_bfs(root, -1))

def find_paths_sum_bfs(root, target_sum):
    if not root:
        return []
    
    q = deque()
    q.append([root, target_sum, []])
    ret = []

    while q:
        node, sum, path = q.popleft()
        path.append(node.val)
        sum -= node.val
        if node.left is None and node.right is None and sum == 0:
            ret.append(path.copy())
            continue
        if node.left:
            q.append([node.left, sum, path.copy()])
        if node.right:
            q.append([node.right, sum, path.copy()])

    return ret
print("### find_paths_sum_bfs")
print(find_paths_sum_bfs(root, 22))
print(find_paths_sum_bfs(root, 18))
print(find_paths_sum_bfs(root, -1))

