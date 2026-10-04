class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:


        # when we find an occurence of non-val, we increment k, and then swap it with ptr, then decrement ptr
        # let's go from left to right, and when we find a non-val value, we update the pointer, swap, and increase

        k = 0
        tmp = []
        for i in range(len(nums)):
            if nums[i] != val:
                k += 1
                tmp.append(nums[i])

        for i in range(k):
            nums[i] = tmp[i]

                    
            

        return k