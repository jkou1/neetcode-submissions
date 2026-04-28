class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()

        # just return an int if the int after it is the same

        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        