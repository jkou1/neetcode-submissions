# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # so we have various lists to link together. 
        # luckily they're all sorted!
        # just need to link then together
        # create a dummy node, which we return the next of
        # loop thru lists: find the min of all heads, then insert, and advance that head
        # if a head is None, just ignore it

        dummy = ListNode()
        curPtr = dummy
        numLists = len(lists)
        doneLists = 0
        while True:
            if doneLists == numLists:
                break
            minInd = -1
            curMin = float('inf')
            for l in range(len(lists)):
                # find the min amongst heads, add it as the next elt
                # then increment that head ptr
                if lists[l] == None:
                    continue
                if lists[l].val < curMin:
                    curMin = lists[l].val
                    minInd = l
            # make a temp and insert it
            temp = lists[minInd]
            curPtr.next = temp
            curPtr = curPtr.next
            lists[minInd] = lists[minInd].next
            if lists[minInd] == None:
                doneLists += 1
            

        return dummy.next

