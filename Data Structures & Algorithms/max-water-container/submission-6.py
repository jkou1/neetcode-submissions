class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0

        l, r = 0, len(heights) - 1
        switch = True
        # if one side is greater than the other, then only 
        # inc/dec the other side, until there is at least a tie

        while l < r:
            width = r - l
            curVol = min(heights[l], heights[r]) * width
            maxVol = max(curVol, maxVol)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maxVol