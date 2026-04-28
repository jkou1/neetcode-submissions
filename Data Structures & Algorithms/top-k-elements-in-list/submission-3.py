class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # list of ints
        resList = []
        numCount = {}

        for num in nums:
            if num in numCount:
                numCount[num] += 1
            else:
                numCount[num] = 1
        # now sort dict by descending value amounts

        numCount = dict(sorted(numCount.items(), key = lambda item: item[1], reverse = True))


        # just add first k keys from dict
        i = 0
        numkeys = numCount.keys()
        for key in numkeys:
            resList.append(key)
            i += 1
            if i + 1 > k:
                break
        return resList

