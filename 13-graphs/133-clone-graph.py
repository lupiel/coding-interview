# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(copy_from_node):
    # dfs to create hash map of nodes (DON'T VISIT NODE TWICE!)
    # for each node in hash map update neighbors using hash map

    node_hash_map = {}

    def dfs(node):
        if node in node_hash_map.keys():
            return

        node_hash_map[node] = Node(node.val)

        for n in node.neighbors:
            dfs(n)
        
    dfs(copy_from_node)

    for x in node_hash_map.keys():
        x.neighbors = [node_hash_map[n] for n in x.neighbors]

    return node_hash_map[copy_from_node]