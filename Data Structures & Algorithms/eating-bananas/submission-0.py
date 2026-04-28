import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # using binary search, test values of bananas and adjust till we've found the lowest one

        l, r = 1, max(piles)
        k = max(piles)
        
        while l <= r:
            # first checking if we can decrease k
            # but really checking to see if we can get the final pile to 0 before the hours taken runs out
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / k)
            
            if hours <= h:
                r = k - 1
            else:
                l = k + 1
        
        return l

                
            

