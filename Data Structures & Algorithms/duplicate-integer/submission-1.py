class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenNums = set()
        for number in nums:
            if number in seenNums:
                return True
            else:
                seenNums.add(number)
        return False
