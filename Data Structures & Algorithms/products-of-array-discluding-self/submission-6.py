class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # o(n) means we need to perform operations in place, per index
        # we can repeat the same operation some constant number of times
        # first, pass over the array and store all products up to, but not including the current index

        res_list = [1] * len(nums)

        right_product = 1
        for i in range(1, len(nums)):
            right_product = nums[i-1] * right_product 
            res_list[i] = right_product


        # now we'll reverse back over the list
        left_product = 1
        for i in range(len(nums)-2, -1, -1):
            left_product = nums[i+1] * left_product
            res_list[i] *= left_product
        
        return res_list