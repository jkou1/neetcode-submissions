class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # can sort strings in python
        # so take s2, and search through it with a window of s1 size
        # if the sorted version of the window matches the sorted version of s1, we have match
        # else, return false

        s1 = list(s1)
        s1.sort()

        l, r = 0, len(s1)

        while r <= len(s2):
            # we need to use l and r to find the window of s2 to sort and check
            s2Slice = s2[l:r]
            s2Slice = list(s2Slice)
            s2Slice.sort()
            if s2Slice == s1:
                return True
            l += 1
            r += 1


        return False