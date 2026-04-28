class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        resList = []

        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum == target:
                resList = [l+1, r + 1]
                break
            if curSum > target:
                r -= 1
            if curSum < target:
                l += 1
        return resList