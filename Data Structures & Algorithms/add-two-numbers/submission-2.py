# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        cur1 = l1
        cur2 = l2
        dummy = ListNode()
        tail = dummy

        while cur1 or cur2 or (carry > 0):
            # we want to go through each digit and add the numbers, then take carry if needed,
            # and store the result in the current digit spot

            # we might not have any digit at cur1 or cur2, in which case we just say that they are 0
            tail.next = ListNode()
            tail = tail.next
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0

            curSum = val1 + val2 + carry
            carry = 0
            if curSum >= 10:
                carry = 1
            curSum = curSum % 10
            tail.val = curSum
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next

        return dummy.next


