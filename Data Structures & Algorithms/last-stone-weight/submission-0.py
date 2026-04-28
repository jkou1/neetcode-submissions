class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            heaviestStone = heapq.heappop(stones)
            nextHeaviestStone = heapq.heappop(stones)
            # if our second smallest stone is lesser than the largest:
            if nextHeaviestStone > heaviestStone:
                heapq.heappush(stones, heaviestStone - nextHeaviestStone)
        
        if len(stones) == 1:
            return abs(stones[0])
        return 0