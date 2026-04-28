# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import defaultdict
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        nodeCounts = defaultdict(int)

        while head:
            nodeCounts[head.val] += 1
            if nodeCounts[head.val] > 1:
                return True
            head = head.next
        return False