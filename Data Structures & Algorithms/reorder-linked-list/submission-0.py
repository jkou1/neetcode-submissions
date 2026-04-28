# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        sp = head
        fp = head.next
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        
        second = sp.next
        prev = sp.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        p1, p2 = head, prev
        while p2:
            temp1, temp2 = p1.next, p2.next
            p1.next = p2
            p2.next = temp1
            p1 = temp1
            p2 = temp2
        
        
            