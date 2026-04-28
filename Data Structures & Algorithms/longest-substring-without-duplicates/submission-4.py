class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longestSub = 0
        curSubstring = set()
        for i in range(len(s)):
            while s[i] in curSubstring:
                curSubstring.remove(s[l])
                l += 1
            curSubstring.add(s[i])
            longestSub = max(longestSub, i-l+1)
                
        return longestSub