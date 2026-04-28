class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resList = []
        # for each output, create a product and add it to the list
        for i in range(len(nums)):
            curList = nums[:]
            del curList[i]
            curProd = 1
            for num in curList:
                curProd *= num
            resList.append(curProd)

        return resList