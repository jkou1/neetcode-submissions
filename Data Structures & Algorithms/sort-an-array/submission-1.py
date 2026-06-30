class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sortedList = [nums[0]]
        
        for n in nums[1:]:
            # if the new item is less than middle value, put it in right side
            # else, put it in left side. 
            # repeat this for the sublists until you find a correct spot for it.

            left_idx = len(sortedList)
            right_idx = 0
            mid_idx = 0
            while right_idx < left_idx:
                mid_idx = (right_idx + left_idx) // 2
                midElt = sortedList[mid_idx]
                if n < midElt:
                    left_idx = mid_idx
                else:
                    right_idx = mid_idx + 1


            sortedList = sortedList[:right_idx] + [n] + sortedList[right_idx:]

        return sortedList

