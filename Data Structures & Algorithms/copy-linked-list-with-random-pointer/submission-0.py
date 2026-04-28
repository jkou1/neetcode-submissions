"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create a hashmap of which nodes point to which copies

        orig2Cpy = {}
        # just copy original nodes and their next pointers
        shlwHead = head
        while shlwHead:
            orig2Cpy[shlwHead] = Node(shlwHead.val)
            shlwHead = shlwHead.next
        # just map none to none
        orig2Cpy[None] = None


        cur = head
        
        while cur:
            # want to give each node the next and random ptrs
            copy = orig2Cpy[cur]
            copy.next = orig2Cpy[cur.next]
            copy.random = orig2Cpy[cur.random]
            cur = cur.next
        return orig2Cpy[head]
