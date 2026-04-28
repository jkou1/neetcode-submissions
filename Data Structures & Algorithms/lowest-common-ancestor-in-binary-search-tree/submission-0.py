# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        # if our values of p and q are both greater than our cur val, we can move cur to the right
        # if p and q vals are both less than cur val, move cur left
        # otherwise we just return cur
        # why? bc if either p or q is equal to cur, then cur is our least common ancestor
        # if q is greater, p is less, or vice versa, then cur is still our lca, bc moving it left or right wouldn't make any sense
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
