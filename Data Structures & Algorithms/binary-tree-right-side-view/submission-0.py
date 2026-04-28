# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        resList = []

        self.heightLists = defaultdict(list)

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
            if len(val) >= 1:
                resList.append(val[-1])
        return resList
