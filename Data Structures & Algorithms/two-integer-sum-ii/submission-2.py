class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        lp, rp = 0, len(numbers)-1

        while lp < rp:
            curSum = numbers[lp] + numbers[rp]
            if curSum == target:
                return [lp + 1, rp + 1]
            elif curSum > target:
                rp -= 1
            elif curSum < target:
                lp += 1 