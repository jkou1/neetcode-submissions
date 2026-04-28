class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # each item is prod of entire array, except itself
        output = []
        # method: 2 pass
        # 1st pass: mulitply elts together, up till cur item,
        # then place the result in cur item index
        # 2nd pass: take items after cur item, starting from right side
        # and multiply the cur res by the prevItems
        prevProd = 1
        afterProd = 1
        for i in range(len(nums)):
            output.append(prevProd)
            prevProd *= nums[i]

        print(output)
        for i in range(len(nums)-1, -1, -1):
            output[i] *= afterProd
            afterProd *= nums[i]

        return output