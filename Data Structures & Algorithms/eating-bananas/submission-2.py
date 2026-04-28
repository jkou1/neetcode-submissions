import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)
        k = piles[-1]
        l, r = 1, k
        minK = -1
        while l <= r:
            # we can test the current banana rate, and if 
            # we can eat all bananas within h, then we adjust down, k = 
            curK = int((l + r) / 2)
            hRem = h
            i = 0
            # if curK is enough to eat all bananas within time h, then adjust down
            # otherwise adjust up
            # so here we check if curK can complete all banaas:
            while i < len(piles):
                timeI = math.ceil(piles[i] / curK)
                hRem -= timeI
                i += 1
            if hRem < 0:
                # then we need to increase our curK
                l = curK + 1
            else:
                # here we've found that curK works, so we can update our global min K to be curK
                r = curK - 1
                minK = curK
        return minK