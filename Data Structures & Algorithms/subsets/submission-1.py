class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # we can either add, or not add a given item to the cur list
        # after we have chosen y/n on all elts, take the current list and add it to the res
        # list
        resList = []
        
        def helper(curList, i):
            # we want to create a temp list, and either add cur elt to it, or skip cur elt

            if i <= len(nums)-1:
                curList.append(nums[i])
                helper(curList, i + 1)
                del curList[-1]
                helper(curList, i + 1)
            else:
                resList.append(curList[:])
                return
        
        helper([], 0)
        return resList

        