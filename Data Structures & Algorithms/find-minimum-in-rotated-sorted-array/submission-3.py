class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we can look at the items in nums
        # is our right greater than our left? then we can look
        # at left half
        # otherwise, we look at right half
        # keep doing this till we just have 1 elt

        # finally, return that elt

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]



