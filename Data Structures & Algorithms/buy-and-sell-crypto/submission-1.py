class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        maxx = 0
        for p in prices:
            if low > p:
                low = p

            if p - low > maxx:
                maxx = p - low  
        return maxx