class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        maxLen = 1
        nums.sort()
        lastSeen = nums[0]
        curLen = 1
        for i in range(1, len(nums)):
            if nums[i] == lastSeen:
                # skip duplicates
                continue
            if nums[i] == lastSeen + 1:
                curLen += 1
                maxLen = max(curLen, maxLen)
            else:
                curLen = 1
            lastSeen = nums[i]
            

        return maxLen