class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenmap = {}
        for i, j in enumerate(nums):
            diff = target - j
            if target - j in seenmap:
                return [seenmap[diff], i]
            seenmap[j] = i
            
