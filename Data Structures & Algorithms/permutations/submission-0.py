class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        baseperms = self.permute(nums[1:])
        res = []

        for bp in baseperms:
            for i in range(len(bp)+1):
                bp.insert(i, nums[0])
                res.append(bp.copy())
                bp.remove(nums[0])


        return res