import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # we can use heap, then remove n-k items
        # if we use minheap, after doing the above we will have kth largest elt
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
        
        # now remove n - k elts

        for i in range(len(nums)-k):
            heapq.heappop(minHeap)
        
        return heapq.heappop(minHeap)