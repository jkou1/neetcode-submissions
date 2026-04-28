class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 32
        num = n
        res = 0
        while i >= 0:
            curDigit = 2 ** i
            if curDigit <= num:
                num -= curDigit
                res += 1
            i -= 1
        return res
