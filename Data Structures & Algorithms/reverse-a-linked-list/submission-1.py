# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return None

        remaining = head
        head = None

        while remaining:
            # we want to take all elts after the elt we are checking, store them as remaining
            # we want to make cur elt point to our head as next
            # last, update our head the cur elt
            curElt = remaining
            remaining = remaining.next
            curElt.next = head
            head = ListNode(curElt.val, curElt.next)

        return head