class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        numsCount = defaultdict(int)
        for i in range(len(nums)):
            numsCount[nums[i]] += 1
        
        sortedDict = dict(sorted(numsCount.items(), key = lambda item: item[1], reverse=True))
        return list(sortedDict.keys())[:k]