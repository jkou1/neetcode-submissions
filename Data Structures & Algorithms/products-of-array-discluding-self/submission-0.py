import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            curList = nums[:i] + nums[i+1:]
            output.append(math.prod(curList))

        return output