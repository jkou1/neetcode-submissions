# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.numGoods = 0

        # track the largest val we've seen so far on a given path.
        # get to a node, if largest val is less than it's val, add one to numGoods
        # update it's val to be the largest
        def inorder(curNode, curMax):
            if not curNode:
                return
            if curNode.val >= curMax:
                self.numGoods += 1
                curMax = curNode.val
            if curNode.left:
                inorder(curNode.left, curMax)
            if curNode.right:
                inorder(curNode.right, curMax)
        inorder(root, float('-inf'))

        return self.numGoods
