"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']: 
        seenMap = {}
        
        def dfs(node):
            if not node:
                return None
            elif node in seenMap:
                return seenMap[node]
            
            copy = Node(node.val)
            seenMap[node] = copy

            # now we copy the neighbors over, in a dfs manner
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        return dfs(node)