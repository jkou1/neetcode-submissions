class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l, r  = 0, len(heights)-1
        tf = True
        while l < r:
            height = min(heights[l], heights[r])
            curWater = height * (r-l)

            maxWater = max(curWater, maxWater)
            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                if tf:
                    l += 1
                    tf = False
                else:
                    r -= 1
                    tf = True
                
        return maxWater