class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # we can use backtracking here

        nums.sort()

        res = []
        def backTrack(curset, i):

            if i == len(nums):
                # if we have reached end of nums, append a copy of curset
                res.append(curset[:])
                return
            else:
                # first case, we include cur elt in subset, then recurse
                curset.append(nums[i])
                backTrack(curset, i + 1)

                # now we remove nums[i], and skip past all the dupes of it
                curset.remove(nums[i])
                while i < len(nums) - 1 and nums[i+1] == nums[i]:
                    i += 1
                backTrack(curset, i + 1)
        backTrack([], 0)

        return res