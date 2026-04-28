# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # when we are at a node, we can return it's value plus some current sum 
        # if we have a left and right, then we add them both to ourself, then check if that sum
        # is greater than the max that we've seen
        # then, we can't return the same sum, we just can only return our current node plus the greater of the left and right
        
        # need to do a dfs approach
        pathMax = float('-inf')
        def dfs(curNode):
            if curNode == None:
                return 0
                
            nonlocal pathMax
            left = dfs(curNode.left)
            right = dfs(curNode.right)
            if left < 0:
                left = 0
            if right < 0:
                right = 0

            curSum = curNode.val + left + right
            pathMax = max(pathMax, curSum)
            return curNode.val + max(left, right)
        
        dfs(root)
        return pathMax

