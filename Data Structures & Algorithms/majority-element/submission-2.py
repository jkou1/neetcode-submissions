from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_occurences = defaultdict(int)
        majority = len(nums) // 2

        for i in range(len(nums)):
            nums_occurences[nums[i]] += 1
            if nums_occurences[nums[i]] > majority:
                return nums[i]