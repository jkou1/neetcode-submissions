class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])


        maxNo1 = maxNoLast = 0

        # setup excluding the 1st elt:
        ind = len(nums)-3
        curSum = 0
        aloneSum = max(nums[-1], nums[-2])
        prevSum = nums[-1]
        while ind > 0:
            curSum = max(nums[ind] + prevSum, aloneSum)
            prevSum = aloneSum
            aloneSum = curSum
            ind -= 1

        maxNo1 = max(curSum, aloneSum)

        # setup excluding the last elt:
        ind = len(nums)-4
        curSum = 0
        aloneSum = max(nums[-2], nums[-3])
        prevSum = nums[-2]
        while ind > -1:
            curSum = max(nums[ind] + prevSum, aloneSum)
            prevSum = aloneSum
            aloneSum = curSum
            ind -= 1

        maxNoLast = max(curSum, aloneSum)

        return max(maxNo1, maxNoLast)
        


        




        