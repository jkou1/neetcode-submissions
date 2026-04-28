# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # if we are at a new level, create a new list and add the elts ONLY
        # at the current level to it, and add to result list
        # make a curHeight var, and incremement it whenever you call recursive func?
        self.heightLists = defaultdict(list)
        resList = []
        curNode = root
        def inorder(curNode, height):
            if not curNode:
                return
            self.heightLists[height].append(curNode.val)
            if curNode.left:
                inorder(curNode.left, height + 1)
            if curNode.right:
                inorder(curNode.right, height + 1)
            
        
        inorder(curNode, 0)
        for val in self.heightLists.values():
            curList = []
            for num in val:
                curList.append(num)
            resList.append(curList)
        return resList

